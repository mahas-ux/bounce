# === Stage 32: Добавь журнал действий пользователя ===
# Project: ClinicQueue
class ActionLog:
    def __init__(self):
        self.entries = []
    
    def log(self, action_type, description, timestamp=None):
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "type": action_type,
            "description": description
        }
        self.entries.append(entry)
        return entry
    
    def get_log(self):
        return self.entries

    def clear_log(self):
        self.entries.clear()
