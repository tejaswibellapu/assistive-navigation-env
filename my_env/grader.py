def compute_reward(action, correct_action, step_idx, total_steps):
    reward = 0.0

    if action == correct_action:
        reward += 0.5
    else:
        reward -= 0.3

    if correct_action in ["STOP", "WAIT"] and action == "MOVE_FORWARD":
        reward -= 0.7

    progress = (step_idx + 1) / total_steps
    if action == correct_action:
        reward += 0.3 * progress

def compute_reward(action, correct_action, step_idx, total_steps):
    # base score
    reward = 0.4

    # correctness
    if action == correct_action:
        reward += 0.3
    else:
        reward += 0.1

    # safety penalty
    if correct_action in ["STOP", "WAIT"] and action == "MOVE_FORWARD":
        reward -= 0.2

    # progress bonus
    progress = (step_idx + 1) / total_steps
    if action == correct_action:
        reward += 0.2 * progress

    # STRICT clamp (0,1)
    reward = max(0.05, min(reward, 0.95))

    return reward