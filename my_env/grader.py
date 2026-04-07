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

    return max(min(reward, 1.0), -1.0)