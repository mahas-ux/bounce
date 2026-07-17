# === Stage 20: Добавь восстановление записей из архива ===
# Project: ClinicQueue
def restore_from_archive(archive_path: str, queue: list) -> int:
    """Восстанавливает записи из текстового архива в очередь."""
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            lines = [ln.strip() for ln in f if ln.strip()]
    except FileNotFoundError:
        print(f"Архив '{archive_path}' не найден")
        return 0

    count = 0
    for line in lines:
        parts = line.split('|')
        if len(parts) != 4:
            continue
        name, time_str, status, note = [p.strip() for p in parts]
        queue.append({'name': name, 'time': time_str, 'status': status, 'note': note})
        count += 1

    print(f"Восстановлено {count} записей из архива.")
    return count
