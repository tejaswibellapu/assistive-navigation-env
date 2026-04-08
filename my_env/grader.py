def compute_reward(action, correct_action, step_idx, total_steps):
    # base score
    reward = 0.5

    # correctness
    if action == correct_action:
        reward += 0.3
    else:
        reward -= 0.2

    # safety penalty
    if correct_action in ["STOP", "WAIT"] and action == "MOVE_FORWARD":
        reward -= 0.2

    # progress bonus
    progress = (step_idx + 1) / max(total_steps, 1)
    if action == correct_action:
        reward += 0.2 * progress

    # STRICT CLAMP (NEVER 0 or 1)
    reward = max(0.1, min(reward, 0.9))

    return reward