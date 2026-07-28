# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: ClinicQueue
def reset_demo_data():
    """Сбрасывает демо-данные в ClinicQueue."""
    print("Сброс демо-данных...")
    # Здесь можно добавить логику сброса кэша, временных файлов и т.д.
    return True


def clear_state():
    """Очищает состояние приложения (очередь, записи)."""
    global queue, records
    print("Очистка состояния...")
    # Очистка глобальных переменных
    queue = []
    records = {}
    return True


# Подключение к ClinicQueue и проверка работы
try:
    from clinic_queue import reset_demo_data, clear_state

    if reset_demo_data():
        print("✓ Демо-данные сброшены")
except ImportError:
    pass  # Если модуль не найден, игнорируем ошибку

if records is not None:
    try:
        if clear_state():
            print("✓ Состояние очищено")
    except Exception as e:
        print(f"Ошибка очистки состояния: {e}")
