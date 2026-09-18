# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: ClinicQueue
import re
from datetime import datetime, timedelta

def parse_datetime(s):
    """Парсит строку в формат 'DD.MM.YYYY HH:MM' или 'YYYY-MM-DD HH:MM'."""
    for fmt in ('%d.%m.%Y %H:%M', '%Y-%m-%d %H:%M'):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    raise ValueError(f"Не распознанный формат даты: {s}")

def format_datetime(dt):
    """Форматирует datetime в 'DD.MM.YYYY HH:MM'."""
    return dt.strftime('%d.%m.%Y %H:%M')

def is_overlap(start1, end1, start2, end2):
    """Проверяет, пересекаются ли два интервала."""
    return start1 < end2 and start2 < end1

def format_status(status):
    """Форматирует статус: 'Ожидание', 'Приём', 'Готов', 'Отмена'."""
    return status.capitalize()

def extract_notes(text):
    """Извлекает заметки из текста."""
    notes = []
    if text:
        notes = [line.strip() for line in text.split('\n') if line.strip()]
    return notes
