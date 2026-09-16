# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: ClinicQueue
def migrate_to_v2(app):
    """Миграция с v1 -> v2: добавляем поле patient_notes и нормализуем статусы."""
    if not hasattr(app, 'queue'):
        return
    q = app.queue
    new_queue = []
    for item in q:
        new_item = {
            'id': item['id'],
            'patient': item['patient'],
            'arrival_time': item['arrival_time'],
            'status': item['status'],
            'patient_notes': item.get('patient_notes', ''),
        }
        new_queue.append(new_item)
    app.queue = new_queue
