# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: ClinicQueue
from datetime import date, timedelta

def monthly_stats(queue):
    """Return a dict: month_name -> {'count': int, 'avg_duration': float}."""
    stats = {}
    for entry in queue:
        d = date(entry['start_date'])
        key = f"{d.month}/{d.year}"
        if key not in stats:
            stats[key] = {'count': 0, 'total_minutes': 0}
        stats[key]['count'] += 1
        stats[key]['total_minutes'] += entry.get('duration', 0)
    result = {}
    for k, v in stats.items():
        result[k] = {
            'count': v['count'],
            'avg_duration': round(v['total_minutes'] / v['count'], 1) if v['count'] else 0.0
        }
    return result

def print_monthly_report(stats):
    """Pretty-print the monthly statistics."""
    if not stats:
        print("No data available.")
        return
    for month, info in sorted(stats.items()):
        avg = f"{info['avg_duration']} мин" if info['count'] else "0 мин"
        print(f"{month}: {info['count']} приёмов (среднее: {avg})")

# Пример: вычислить и вывести статистику за текущий месяц
if __name__ == "__main__":
    sample_queue = [
        {'start_date': '2024-10-05', 'duration': 30},
        {'start_date': '2024-10-12', 'duration': 45},
        {'start_date': '2024-11-01', 'duration': 60},
    ]
    s = monthly_stats(sample_queue)
    print_monthly_report(s)
