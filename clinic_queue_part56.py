# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: ClinicQueue
def bulk_update_selected(app, records):
    if not records:
        return
    selected = [r for r in records if r.get("selected", False)]
    if not selected:
        return
    print(f"\nМассовое обновление: {len(selected)} записей")
    try:
        new_status = input("Новый статус (например, 'в приёме'): ")
    except EOFError:
        new_status = "в ожидании"
    try:
        new_time = input("Новое время (HH:MM): ")
    except EOFError:
        new_time = None
    for record in selected:
        record["status"] = new_status
        if new_time:
            record["time"] = new_time
        record["updated"] = True
    print("Обновлено.")
