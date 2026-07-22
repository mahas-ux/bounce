# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: ClinicQueue
def print_table(appointments):
    if not appointments:
        print("Очередь пуста.")
        return
    headers = ["#", "ФИО", "Дата/Время", "Статус", "Заметка"]
    widths = [2, 40, 28, 16, 50]
    for i, h in enumerate(headers):
        w = max(widths[i], len(h)) if i < len(appointments[0]) else min(w, len(h) * 3)
        widths[i] = w
    print(" | ".join(f"{h:<{widths[i]}}" for i, h in enumerate(headers)))
    print("-+-".join("=" * widths[i] for i in range(len(headers))))
    fmt = " | ".join(f"{{:<{widths[i]}}}" for i in range(len(headers)))
    for idx, appt in enumerate(appointments):
        row = [str(idx + 1)]
        if len(appt) >= 2: row.append(str(appt[1]))
        if len(appt) >= 3: row.append(str(appt[2]))
        else: row.append("")
        if len(appt) >= 4: row.append(str(appt[3]))
        else: row.append("")
        if len(appt) >= 5: row.append(str(appt[4]) or "")
        print(fmt.format(*row))

print_table(appointments)
