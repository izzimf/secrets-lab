import os
import json

def load_config():
    if os.path.exists("config.json"):
        with open("config.json") as f:
            return json.load(f)
    return {}

def main():
    secret_env = os.getenv("API_KEY")
    config = load_config()
    secret_config = config.get("API_KEY")  # ключ должен совпадать с именем в config.json

    print("ENV secret:", secret_env)
    print("Config-file secret:", secret_config)

if __name__ == "__main__":
    main()
