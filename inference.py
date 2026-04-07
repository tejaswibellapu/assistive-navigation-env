import os
from my_env.env import AssistiveEnv
from my_env.models import Action

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")

MAX_STEPS = 8


def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}")


def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")


def log_end(success, steps, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}")


# 🔥 RULE-BASED AGENT (no API needed)
def get_action(obs_text):
    text = obs_text.lower()

    # Safety first
    if "red" in text:
        return "WAIT"

    if "approaching" in text or "crosses" in text:
        return "STOP"

    if "blocked" in text:
        if "left" in text:
            return "TURN_LEFT"
        elif "right" in text:
            return "TURN_RIGHT"

    if "clear" in text or "green" in text:
        return "MOVE_FORWARD"

    # default fallback
    return "STOP"


def run_task(task_name):
    env = AssistiveEnv(task_name=task_name)
    obs = env.reset()

    rewards = []
    steps = 0

    log_start(task_name, "assistive_navigation_env", MODEL_NAME)

    for step in range(1, MAX_STEPS + 1):
        action_str = get_action(obs.description)

        result = env.step(Action(action=action_str))

        rewards.append(result.reward)
        steps = step

        log_step(step, action_str, result.reward, result.done)

        obs = result.observation

        if result.done:
            break

    success = sum(rewards) > 0
    log_end(success, steps, rewards)


if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        run_task(task)