# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: ClinicQueue
import json, sys

INITIAL_DATA = '''
[{"id": 1, "name": "Иванов И.И.", "time": "09:30", "status": "ожидание", "notes": "Жалобы на головную боль"}, {"id": 2, "name": "Петров П.П.", "time": "09:45", "status": "в_приеме", "notes": ""}, {"id": 3, "name": "Сидоров С.С.", "time": "10:00", "status": "ожидание", "notes": "Требуется консультация кардиолога"}]
'''

def load_initial_data():
    try:
        return json.loads(INITIAL_DATA)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга начальных данных: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    patients = load_initial_data()
