# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: ClinicQueue
import json, random, datetime as dt
from dataclasses import dataclass, field, asdict
from typing import Optional

@dataclass
class Patient:
    id: int
    name: str
    arrival_time: dt.datetime
    status: str = "waiting"
    notes: str = ""

def generate_demo_data() -> list[Patient]:
    base_time = dt.datetime.now().replace(hour=9, minute=0)
    patients = []
    for i in range(1, 6):
        arrival_offset = random.randint(0, 30) * 60
        p = Patient(id=i, name=f"Пациент {i}", arrival_time=base_time + dt.timedelta(minutes=arrival_offset))
        if i % 2 == 0:
            p.status = "in_progress"
            p.notes = random.choice(["Жалобы на головную боль", "Контроль давления"])
        else:
            p.notes = ""
        patients.append(p)
    return patients

if __name__ == "__main__":
    demo_patients = generate_demo_data()
    for p in demo_patients:
        print(f"[{p.status.upper()}] {p.name} ({p.arrival_time.strftime('%H:%M')}) - Заметка: {p.notes or '-'}")
