# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: ClinicQueue
class Patient:
    def __init__(self, name: str, arrival_time: int, notes: str = "") -> None:
        self.name = name.strip() or "Без имени"
        self.arrival_time = arrival_time
        self.notes = notes.strip() if notes else ""

def validate_patient_input(name: str, time_str: str) -> tuple[Patient | None, list[str]]:
    errors = []
    try:
        hour, minute = map(int, time_str.split(':'))
        if not (0 <= hour < 24 and 0 <= minute < 60):
            raise ValueError("Неверное время")
        arrival_time = hour * 60 + minute
        patient = Patient(name, arrival_time)
    except Exception:
        errors.append("Ошибка формата времени или имени пациента.")
        return None, errors
    if not name.strip():
        errors.append("Имя не может быть пустым.")
        return None, errors
    return patient, []
