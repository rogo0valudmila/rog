import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Saved JSON to {path}")

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    cfg = load_config()
    data = {"message": "Hello JSON!"}
    save_json(data, cfg["default_path"])
    print("Loaded back:", read_json(cfg["default_path"]))
