# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: ClinicQueue
def print_metrics():
    """Print key project metrics."""
    total_appointments = len(appointments)
    completed = sum(1 for a in appointments if a.status == "completed")
    pending = sum(1 for a in appointments if a.status == "pending")
    active = sum(1 for a in appointments if a.status in ("in_progress",))
    cancelled = sum(1 for a in appointments if a.status == "cancelled")

    print(f"Total: {total_appointments}")
    print(f"  Completed: {completed} ({completed / total_appointments * 100:.1f}%)" if total_appointments else "  No data yet.")
    print(f"  Pending:   {pending}")
    print(f"  In progress:{active}")
    print(f"  Cancelled: {cancelled}")

    # Average duration of completed appointments (in minutes)
    if completed > 0:
        avg_dur = sum(
            (a.end - a.start).total_seconds() / 60 for a in appointments if a.status == "completed"
        ) / completed
        print(f"Average duration (completed): {avg_dur:.1f} min")

    # Count patients with notes
    noted_patients = sum(1 for a in appointments if a.note)
    print(f"Patients with notes: {noted_patients}/{total_appointments}")


print_metrics()
