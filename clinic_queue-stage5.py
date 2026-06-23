# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: ClinicQueue
def remove_appointment(app_id: str) -> bool:
    """Удаление записи по ID с проверкой существования."""
    if app_id not in appointments:
        print(f"Ошибка: запись #{app_id} не найдена.")
        return False
    
    del appointments[app_id]
    print(f"Запись #{app_id} успешно удалена.")
    return True

def handle_missing_appointment(app_id: str) -> None:
    """Обработка случая отсутствия записи с информированием пользователя."""
    if app_id not in appointments:
        print(f"Предупреждение: попытка удалить несуществующую запись #{app_id}.")
