# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: ClinicQueue
from datetime import date, timedelta
import random

def generate_reminders():
    """Generates a list of reminder dictionaries with dates and messages."""
    reminders = []
    for i in range(10):
        reminder_date = (date.today() + timedelta(days=random.randint(1, 30))).isoformat()
        reminder_text = random.choice([
            "Follow up with patient",
            "Call lab results back",
            "Send appointment confirmation",
            "Request medical records",
            "Schedule follow-up visit"
        ])
        reminders.append({
            "reminder_id": i + 1,
            "date": reminder_date,
            "message": reminder_text
        })
    return reminders

def display_reminders(reminders):
    """Displays the list of reminders in a formatted table."""
    if not reminders:
        print("No reminders scheduled.")
        return
    
    print("\n--- Reminders ---")
    for r in reminders:
        print(f"ID: {r['reminder_id']} | Date: {r['date']} | Message: {r['message']}")

# Example usage
if __name__ == "__main__":
    reminder_list = generate_reminders()
    display_reminders(reminder_list)
