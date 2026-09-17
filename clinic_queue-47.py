# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: ClinicQueue
def demo():
    print("=== ClinicQueue Demo ===")
    queue = Queue()
    for i in range(1, 6):
        queue.add(Patient(name=f"Пациент {i}", time=f"10:0{i}", note="Обычный визит"))
    queue.add(Patient(name="Срочный", time="09:30", note="Срочный случай"))
    print(f"Очередь: {queue}")
    queue.next()
    print(f"Текущий: {queue.current}")
    queue.next()
    print(f"Текущий: {queue.current}")
    queue.next()
    print(f"Текущий: {queue.current}")
    print(f"Всего обслужено: {queue.served}")
    print("=== Demo finished ===")
