import random

OBSTACLES = [
    ("A pole is directly ahead.", "STOP"),
    ("A bicycle is approaching from right.", "STOP"),
    ("A dog suddenly crosses your path.", "STOP"),
]

PATHS = [
    ("Path ahead is blocked. Left side is clear.", "TURN_LEFT"),
    ("Path ahead is blocked. Right side is clear.", "TURN_RIGHT"),
]

SIGNALS = [
    ("You are at a crosswalk. Signal is red.", "WAIT"),
    ("Signal turned green. Safe to cross.", "MOVE_FORWARD"),
]


def generate_scenario(difficulty="easy"):
    steps = []

    if difficulty == "easy":
        desc, action = random.choice(OBSTACLES)
        steps.append({"description": desc, "correct_action": action})

    elif difficulty == "medium":
        desc1, act1 = random.choice(PATHS)
        steps.append({"description": desc1, "correct_action": act1})
        steps.append({"description": "Path is now clear.", "correct_action": "MOVE_FORWARD"})

    elif difficulty == "hard":
        steps.append({"description": SIGNALS[0][0], "correct_action": SIGNALS[0][1]})
        steps.append({"description": SIGNALS[1][0], "correct_action": SIGNALS[1][1]})
        desc, action = random.choice(OBSTACLES)
        steps.append({"description": desc, "correct_action": action})

    return steps