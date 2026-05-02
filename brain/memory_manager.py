import os
import json
from datetime import datetime

BASE_PATH = "./memory/users/"

def ensure_user(user_id):
    path = os.path.join(BASE_PATH, user_id)
    os.makedirs(path, exist_ok=True)

    log_path = os.path.join(path, "log.jsonl")
    state_path = os.path.join(path, "state.json")

    if not os.path.exists(log_path):
        open(log_path, "w").close()

    if not os.path.exists(state_path):
        with open(state_path, "w") as f:
            json.dump({
                "relationship": "unknown",
                "tone": "neutral",
                "familiarity": 0.0,
                "traits": []
            }, f, indent=2)


def load_state(user_id):
    path = os.path.join(BASE_PATH, user_id, "state.json")
    with open(path, "r") as f:
        return json.load(f)


def save_state(user_id, state):
    path = os.path.join(BASE_PATH, user_id, "state.json")
    with open(path, "w") as f:
        json.dump(state, f, indent=2)


def append_log(user_id, role, text):
    path = os.path.join(BASE_PATH, user_id, "log.jsonl")

    if text != "i couldn't think of anything...":
        
        entry = {
            "role": role,
            "text": text,
            "timestamp": datetime.utcnow().isoformat()
        }

        with open(path, "a") as f:
            f.write(json.dumps(entry) + "\n")


def load_recent_chat(user_id, limit=10):
    path = os.path.join(BASE_PATH, user_id, "log.jsonl")

    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        lines = f.readlines()[-limit:]

    return [json.loads(l) for l in lines]