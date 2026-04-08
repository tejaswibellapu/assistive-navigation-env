def compute_reward(action, correct_action, step_idx, total_steps):
    # Always start from middle (safe)
    reward = 0.5

    if action == correct_action:
        reward += 0.2
    else:
        reward -= 0.1

    if correct_action in ["STOP", "WAIT"] and action == "MOVE_FORWARD":
        reward -= 0.1

    progress = (step_idx + 1) / max(total_steps, 1)
    reward += 0.1 * progress

    # NEVER allow extremes
    reward = max(0.2, min(reward, 0.8))

    return reward