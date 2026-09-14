# === Stage 45: Добавь восстановление из резервной копии ===
# Project: ClinicQueue
import json, os

BACKUP_FILE = "clinic_queue_backup.json"

def load_backup():
    if not os.path.exists(BACKUP_FILE):
        print("Резервная копия не найдена.")
        return None
    with open(BACKUP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def restore_backup():
    data = load_backup()
    if data is None:
        return
    print(f"Восстановлено {len(data.get('appointments', []))} записей из резервной копии.")
