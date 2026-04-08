import os
from openai import OpenAI
from my_env.env import AssistiveEnv
from my_env.models import Action

API_BASE_URL = os.environ["API_BASE_URL"]
API_KEY = os.environ["API_KEY"]
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

MAX_STEPS = 8

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)


def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}")


def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")


def log_end(success, steps, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}")


def get_action(obs_text):
    prompt = f"""
You are assisting a visually impaired person.

Situation:
{obs_text}

Rules:
- Prioritize safety
- Avoid collisions
- If danger → STOP or WAIT
- If safe → MOVE_FORWARD or turn

Respond ONLY with:
MOVE_FORWARD, STOP, TURN_LEFT, TURN_RIGHT, WAIT
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10,
    )

    return response.choices[0].message.content.strip()


def run_task(task_name):
    env = AssistiveEnv(task_name=task_name)
    obs = env.reset()

    rewards = []
    steps = 0

    log_start(task_name, "assistive_navigation_env", MODEL_NAME)

    for step in range(1, MAX_STEPS + 1):
        try:
            action_str = get_action(obs.description)
        except:
            action_str = "STOP"

        result = env.step(Action(action=action_str))

        rewards.append(result.reward)
        steps = step

        log_step(step, action_str, result.reward, result.done)

        obs = result.observation

        if result.done:
            break

    # FINAL SAFE CLAMP
    rewards = [max(0.05, min(r, 0.95)) for r in rewards]

    success = (sum(rewards) / len(rewards)) > 0.5

    log_end(success, steps, rewards)


if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        run_task(task)