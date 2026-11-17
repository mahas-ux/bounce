# === Stage 59: Добавь диагностику производительности основных операций ===
# Project: ClinicQueue
def benchmark_queue():
    from timeit import default_timer as timer

    print("== Диагностика производительности ClinicQueue ==")

    # --- Настройка тестового набора данных ---
    patients = [
        {"id": i, "name": f"Пациент {i}", "time": "09:00", "status": "new",
         "notes": ""} for i in range(500)
    ]
    queue = {"new": patients}

    # --- Очистка кэша для точного измерения ---
    import sys
    for mod in list(sys.modules):
        if mod in ("clinicqueue", "clinicqueue.core", "clinicqueue.db"):
            del sys.modules[mod]

    import clinicqueue.core as cq

    # --- Warm-up ---
    cq.enqueue(queue, {"id": 99999, "name": "Тест", "time": "10:00", "status": "new", "notes": ""})
    cq.dequeue(queue, "new")
    cq.update(queue, 99998, {"status": "waiting"})
    cq.search(queue, "Пациент")

    # --- Измерение enqueue (append) ---
    n = 1000
    t0 = timer()
    for i in range(n):
        cq.enqueue(queue, {"id": i, "name": f"P{i}", "time": "09:00", "status": "new", "notes": ""})
    t1 = timer()
    print(f"enqueue (append):  {t1 - t0:.4f}c / {n} = {(t1 - t0) / n * 1e6:.2f} мкс/вызв")

    # --- Измерение dequeue (pop) ---
    t0 = timer()
    for _ in range(n):
        cq.dequeue(queue, "new")
    t1 = timer()
    print(f"dequeue (pop):    {t1 - t0:.4f}c / {n} = {(t1 - t0) / n * 1e6:.2f} мкс/вызв")

    # --- Измерение update (поиск по id) ---
    t0 = timer()
    for i in range(n):
        cq.update(queue, i, {"status": "waiting"})
    t1 = timer()
    print(f"update (по id):   {t1 - t0:.4f}c / {n} = {(t1 - t0) / n * 1e6:.2f} мкс/вызв")

    # --- Измерение search (линейный поиск) ---
    t0 = timer()
    for _ in range(n):
        cq.search(queue, "Пациент")
    t1 = timer()
    print(f"search (линейн.): {t1 - t0:.4f}c / {n} = {(t1 - t0) / n * 1e6:.2f} мкс/вызв")

    print("== Диагностика завершена ==")
