# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: ClinicQueue
def batch_delete(app, confirm=True):
    appointments = app.queues['default'].get_appointments()
    if not appointments:
        print("Нет приёмов для удаления.")
        return
    ids = [a['id'] for a in appointments]
    print("Доступные приёмы:")
    for a in appointments:
        print(f"  {a['id']}. {a['patient']} ({a['status']})")
    print("Введите ID через запятую или 'all' для всех, или 'q' чтобы отменить.")
    choice = input("Выбор: ").strip()
    if choice == 'q':
        print("Отменено.")
        return
    if choice == 'all':
        targets = set(ids)
    else:
        targets = set()
        for part in choice.split(','):
            part = part.strip()
            if not part:
                continue
            if part not in ids:
                print(f"ID '{part}' не найден, пропущен.")
                continue
            targets.add(int(part))
    if not targets:
        print("Ничего не выбрано.")
        return
    if confirm:
        print(f"Удалить приёмов: {sorted(targets)}? (y/n)")
        if input("Подтверждение: ").strip().lower() != 'y':
            print("Отменено.")
            return
    for tid in targets:
        removed = app.queues['default'].delete_appointment(tid)
        if removed:
            print(f"Удалён приём #{tid}.")
        else:
            print(f"Приём #{tid} не найден.")
