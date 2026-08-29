# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: ClinicQueue
def recommend_next_action(queue: list[dict], current_patient: dict | None = None) -> str:
    """Генерирует рекомендацию следующего действия на основе состояния очереди."""
    if not queue:
        return "Очередь пуста. Предложите пациенту записаться на приём или обновить данные."

    statuses = {"Ожидание": 0, "Приём": 0, "Завершён": 0, "Отменён": 0}
    for item in queue:
        s = item.get("status", "Ожидание")
        statuses[s] = statuses.get(s, 0) + 1

    total = len(queue)
    active = statuses.get("Ожидание", 0) + statuses.get("Приём", 0)

    if active == 0 and statuses.get("Завершён", 0) == total:
        return "Все приёмы завершены. Очередь очищена. Можно начать новый день."

    if statuses.get("Отменён", 0) == total:
        return "Все приёмы отменены. Проверьте записи и обновите статусы."

    if current_patient and current_patient.get("status") == "Приём":
        return "Текущий пациент принимает. Следующий пациент готов к приёму или ждёт очереди."

    if active == total:
        return "Все пациенты в очереди. Рекомендую начать приём первого пациента."

    if active == 0:
        return "Пациентов нет в очереди. Предложите записаться или отмените текущий."

    waiting = statuses.get("Ожидание", 0)
    if waiting > 0:
        return f"В очереди {waiting} пациентов. Следующий — следующий в списке ожидания."

    return "Пациент на приёме. Следующий — в ожидании."
