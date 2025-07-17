# utils/logger.py
import datetime
import os

def log_action(mode, user_input, result):
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, f"{mode.lower().replace(' ', '_')}_log.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n[{timestamp}] MODE: {mode}\n")
        f.write(f"USER: {user_input}\n")
        f.write(f"RESULT: {str(result)}\n")
        f.write("="*50)
