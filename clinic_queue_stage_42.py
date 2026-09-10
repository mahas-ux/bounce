# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: ClinicQueue
import sys

ANSI = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
}

def colorize(text, color):
    if os.environ.get('NO_COLOR'):
        return text
    return ANSI.get(color, '') + text + ANSI['reset']

def print_status(status, patient):
    color_map = {
        'waiting': 'cyan',
        'in_progress': 'blue',
        'completed': 'green',
        'cancelled': 'red',
        'no-show': 'yellow',
    }
    bg = ANSI['bg_green'] if status == 'completed' else ''
    print(colorize(bg + f"[{status.upper()}]", 'green') + f" {patient.name} - {patient.time}")
