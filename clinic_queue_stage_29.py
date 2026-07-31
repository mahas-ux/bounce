# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: ClinicQueue
import json, os

APP_DIR = "clinic_queue"
CONFIG_FILE = f"{APP_DIR}/config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_default_config()
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_default_config():
    default = {
        "app_name": "ClinicQueue",
        "version": 29,
        "max_queue_size": 100,
        "recipients": ["Dr. Smith", "Dr. Jones"],
        "work_hours": {"start": "08:00", "end": "20:00"},
        "timezone": "Europe/Moscow",
        "language": "ru"
    }
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(default, f, indent=2, ensure_ascii=False)

def update_config(key, value):
    config = load_config()
    config[key] = value
    save_default_config()  # временно перезаписываем для простоты
