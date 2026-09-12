# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: ClinicQueue
import json, os, sys, datetime

def backup_data_file(data_file="clinic_queue_data.json", backup_dir="backups"):
    """Создаёт резервную копию файла данных в директорию backups."""
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"clinic_queue_backup_{timestamp}.json")
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        with open(backup_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"[OK] Backup saved to {backup_path}")
    except FileNotFoundError:
        print("[WARN] Data file not found, skipping backup.")
    except Exception as e:
        print(f"[ERROR] Backup failed: {e}")
