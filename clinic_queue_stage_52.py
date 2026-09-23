# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: ClinicQueue
def export_report(clinic_queue):
    lines = []
    lines.append("ClinicQueue Report")
    lines.append("=" * 30)
    for i, appointment in enumerate(clinic_queue, start=1):
        status = appointment["status"]
        if status == "confirmed":
            lines.append(f"{i}. {appointment['name']} - {appointment['time']}")
        elif status == "cancelled":
            lines.append(f"{i}. {appointment['name']} - {appointment['time']} (cancelled)")
        elif status == "completed":
            lines.append(f"{i}. {appointment['name']} - {appointment['time']} (completed)")
    return "\n".join(lines)
