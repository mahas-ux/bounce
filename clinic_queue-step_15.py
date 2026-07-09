# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: ClinicQueue
def weekly_stats(appointments):
    """Returns dict: week_start_date -> list of appointment count & avg duration."""
    if not appointments:
        return {}
    from datetime import timedelta
    weeks = {}
    for ap in appointments:
        dt = ap.get("date", ap["datetime"])
        if isinstance(dt, str):
            dt = datetime.fromisoformat(dt)
        week_start = (dt.date() - timedelta(days=dt.weekday())).isoformat()
        weeks.setdefault(week_start, {"count": 0, "total_min": 0})[week_start]["count"] += 1
        if ap.get("duration"):
            weeks[week_start]["total_min"] += ap["duration"]
    return {w: {"count": d["count"], "avg_min": round(d["total_min"] / d["count"])} for w, d in weeks.items()}
