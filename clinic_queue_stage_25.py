# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: ClinicQueue
def parse_date(date_str):
    """Парсит дату в формате ГГГГ-ММ-ДД, возвращает datetime.date или None."""
    if not date_str or len(date_str.split('-')) != 3:
        return None
    try:
        parts = [int(x) for x in date_str.split('-')]
        if len(parts) != 3 or not (1 <= parts[0] <= 9999 and 1 <= parts[1] <= 12 and 1 <= parts[2] <= 31):
            return None
        import datetime as dt
        return dt.date(parts[0], parts[1], parts[2])
    except Exception:
        return None

def format_error(msg, field=None):
    """Формирует понятное сообщение об ошибке."""
    if field:
        return f"Ошибка в поле '{field}': {msg}"
    return msg
