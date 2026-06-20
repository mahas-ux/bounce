# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: ClinicQueue
class ClinicQueue:
    def __init__(self):
        self._records = []
    
    def add_patient(self, name: str, arrival_time: float, status: str = "waiting", note: str = "") -> dict:
        record = {
            "id": len(self._records) + 1,
            "name": name,
            "arrival_time": arrival_time,
            "status": status,
            "note": note,
            "created_at": self._get_current_timestamp()
        }
        self._records.append(record)
        return record
    
    def _get_current_timestamp(self) -> float:
        import time
        return time.time()

if __name__ == "__main__":
    queue = ClinicQueue()
    p1 = queue.add_patient("Иванов", 1704067200.5, "waiting")
    print(f"Добавлен пациент: {p1['id']}, имя: {p1['name']}")
