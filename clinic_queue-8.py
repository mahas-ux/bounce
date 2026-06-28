# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: ClinicQueue
def show_menu():
    print("\n=== Меню ClinicQueue ===")
    print("1. Добавить пациента")
    print("2. Показать очередь")
    print("3. Изменить статус приёма")
    print("4. Удалить запись")
    print("5. Выход")

def run_command(cmd):
    if cmd == "1":
        name = input("Имя пациента: ")
        time_str = input("Время (HH:MM): ")
        notes = input("Заметки (Enter для пропуска): ").strip() or "-"
        patients.append({"name": name, "time": time_str, "status": "Ожидание", "notes": notes})
        print(f"Пациент {name} добавлен.")
    elif cmd == "2":
        if not patients:
            print("Очередь пуста.")
        else:
            for i, p in enumerate(patients):
                print(f"{i+1}. [{p['status']}] {p['name']} ({p['time']}) - {p['notes']}")
    elif cmd == "3":
        idx = int(input("Номер записи в очереди: ")) - 1
        if 0 <= idx < len(patients):
            new_status = input("Новый статус: ")
            patients[idx]["status"] = new_status
            print(f"Статус изменён на {new_status}.")
    elif cmd == "4":
        idx = int(input("Номер записи для удаления: ")) - 1
        if 0 <= idx < len(patients):
            del patients[idx]
            print("Запись удалена.")
    elif cmd == "5":
        exit()

while True:
    show_menu()
    cmd = input("\nВаш выбор (1-5): ")
    try:
        run_command(cmd)
    except ValueError:
        print("Неверный ввод, попробуйте снова.")
