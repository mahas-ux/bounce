# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: ClinicQueue
def export_queue_to_json(queue_data):
    import json
    try:
        return json.dumps(queue_data, ensure_ascii=False, indent=2)
    except TypeError as e:
        raise ValueError(f"Ошибка сериализации данных в JSON: {e}")
