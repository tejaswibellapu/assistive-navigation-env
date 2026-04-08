def compute_reward(action, correct_action, step_idx, total_steps):
    reward = 0.5

    if action == correct_action:
        reward += 0.25
    else:
        reward -= 0.15

    if correct_action in ["STOP", "WAIT"] and action == "MOVE_FORWARD":
        reward -= 0.2

    progress = (step_idx + 1) / max(total_steps, 1)
    if action == correct_action:
        reward += 0.2 * progress

    # STRICT CLAMP
    if reward <= 0:
        reward = 0.05
    elif reward >= 1:
        reward = 0.95

    return reward