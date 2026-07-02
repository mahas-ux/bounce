# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: ClinicQueue
import json, os
DATA_FILE = "clinic_queue.json"

def save_to_json(queue_data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(queue_data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[Error] Failed to save data: {e}")
        return False

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []
