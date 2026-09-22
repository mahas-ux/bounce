# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: ClinicQueue
import time


class AuditLog:
    def __init__(self):
        self._entries = []

    def record(self, action, subject, details=""):
        self._entries.append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "subject": subject,
            "details": details,
        })

    def get(self):
        return list(self._entries)
