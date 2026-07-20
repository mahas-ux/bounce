# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: ClinicQueue
import time as _time

def check_overdue_reminders(queue, current_time=_time.time()):
    """Проверяет напоминания и возвращает список просроченных."""
    overdue = []
    for patient in queue:
        if patient.get("reminder"):
            reminder_time = patient["reminder"]
            if _time.time() > reminder_time:
                patient.setdefault("status", "pending")
                patient["status"] = "overdue"
                overdue.append(patient)
    return overdue
