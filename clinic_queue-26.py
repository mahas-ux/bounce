# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: ClinicQueue
def demo_quick_test():
    """Демо: создаём 3 пациента, ставим в очередь, меняем статусы, потом выводим."""
    from clinic_queue import Patient, Appointment, ClinicQueue
    q = ClinicQueue()
    
    # Создаём пациентов
    p1 = Patient("Алексей", "Мужской", 45)
    p2 = Patient("Мария", "Женский", 38)
    p3 = Patient("Дмитрий", "Мужской", 62)
    
    # Записываем приёмы с разными статусами и заметками
    a1 = Appointment(p1, datetime.datetime.now(), "Плановый", "Первичный осмотр")
    a2 = Appointment(p2, datetime.datetime.now() + timedelta(minutes=30), "Срочный", "Головная боль")
    a3 = Appointment(p3, datetime.datetime.now() + timedelta(hours=1), "Консультация", "")
    
    # Добавляем в очередь
    q.add_appointment(a1)
    q.add_appointment(a2)
    q.add_appointment(a3)
    
    print(f"В очереди: {len(q.appointments)} приёмов")
    for appt in q.appointments:
        print(f"  - {appt.patient.name} | Статус: {appt.status} | Заметка: {appt.notes}")
    
    # Меняем статусы
    a1.set_status("Плановый", "Выполнен")
    print(f"\nСтатус Алексея изменён на: {a1.status}")
    
    # Ищем срочный пациент и выводим его
    urgent = q.find_appointment_by_status("Срочный")
    if urgent:
        print(f"Срочный пациент: {urgent.patient.name}, заметка: {urgent.notes}")
