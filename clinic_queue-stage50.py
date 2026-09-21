# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: ClinicQueue
def print_queue_report(queue: Queue, patient: Patient) -> None:
    """Отображает отчёт по очереди: статусы, время ожидания, заметки."""
    print(f"\n{'='*60}")
    print(f"ОТЧЁТ ПО ОЧЕРЕДИ ПРИЁМА")
    print(f"{'='*60}")

    print(f"Пациент: {patient.name}")
    print(f"Статус: {patient.status.value}")
    print(f"Время ожидания: {patient.wait_time} минут")
    if patient.note:
        print(f"Заметка: {patient.note}")
    print(f"{'='*60}")
