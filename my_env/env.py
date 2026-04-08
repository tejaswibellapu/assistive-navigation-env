from my_env.models import Observation, Action, StepResult
from my_env.scenarios import generate_scenario
from my_env.grader import compute_reward


class AssistiveEnv:
    def __init__(self, task_name="easy"):
        self.task_name = task_name
        self.steps = []
        self.current_step = 0
        self.done = False
        self.history = []

    def reset(self):
        self.steps = generate_scenario(self.task_name)
        self.current_step = 0
        self.done = False
        self.history = []
        return self._get_obs()

    def _get_obs(self):
        step = self.steps[self.current_step]
        return Observation(
            description=step["description"],
            step_count=self.current_step,
            history=self.history[-3:]
        )

    def step(self, action: Action):
        # FINAL STEP CASE (IMPORTANT)
        if self.done:
            return StepResult(
                observation=self._get_obs(),
                reward=0.5,   # NEVER 0 or 1
                done=True
            )

        step_data = self.steps[self.current_step]
        correct_action = step_data["correct_action"]

        reward = compute_reward(
            action.action,
            correct_action,
            self.current_step,
            len(self.steps)
        )

        # 🔥 HARD CLAMP EVERY TIME
        reward = 0.5 + (reward - 0.5) * 0.8   # compress into safe range
        reward = max(0.1, min(reward, 0.9))   # STRICT (0,1)

        self.history.append(f"{action.action} -> {correct_action}")

        if action.action == correct_action:
            self.current_step += 1

        if self.current_step >= len(self.steps):
            self.done = True

        return StepResult(
            observation=self._get_obs() if not self.done else Observation(
                description="Navigation completed safely.",
                step_count=self.current_step,
                history=self.history
            ),
            reward=reward,
            done=self.done,
            info={"correct_action": correct_action}
        )

    def state(self):
        return {
            "task": self.task_name,
            "step": self.current_step,
            "history": self.history,
            "done": self.done
        }