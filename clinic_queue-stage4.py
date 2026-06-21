# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: ClinicQueue
def edit_patient_record(record_id: int, updates: dict) -> bool | None:
    if not (record := next((r for r in patients if r['id'] == record_id), None)):
        return False
    updated = {**record}
    for key, value in updates.items():
        if key in ['name', 'age', 'status', 'notes']:
            updated[key] = value
    idx = next(i for i, r in enumerate(patients) if r['id'] == record_id)
    patients[idx] = updated
    return True
