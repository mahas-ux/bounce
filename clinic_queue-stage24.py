# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: ClinicQueue
def print_record(record):
    """Компактный вывод одной записи очереди."""
    status_map = {0: "Ожидание", 1: "В работе", 2: "Завершён"}
    s = status_map.get(record["status"], "Неизвестный")
    print(f"ID: {record['id']} | Пациент: {record['name']}")
    print(f"  Время прибытия: {record['arrival_time']:.0f} мин")
    if record.get("duration"):
        duration = record["duration"]
        print(f"  Длительность: {duration/60.0:.1f} ч ({duration} мин)")
    else:
        print(f"  Время завершения: {record['end_time']:.0f} мин")
    if record.get("notes"):
        print(f"  Заметка: {record['notes']}")
    if record.get("priority", False):
        print(f"  ⚠ Приоритетный пациент")
    print(f"  Статус: {s}")

# Пример вызова (разкомментируй после добавления записей)
# records = [
#     {"id": 1, "name": "Иван Иванов", "arrival_time": 0, "duration": None, "end_time": 60, "status": 2, "notes": "Срочно, температура", "priority": True},
#     {"id": 2, "name": "Мария Петрова", "arrival_time": 15, "duration": None, "end_time": 90, "status": 1, "notes": "", "priority": False},
# ]
# for r in records:
#     print_record(r)
