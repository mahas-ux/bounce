# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: ClinicQueue
def find_duplicate_appointments(new_appt):
    for appt in appointments:
        if appt.get("patient_id") == new_appt.get("patient_id") and appt.get("appointment_time") == new_appt.get("appointment_time"):
            return appt
    return None


def create_appointment(patient_id, appointment_time, notes=""):
    existing_dup = find_duplicate_appointments({"patient_id": patient_id, "appointment_time": appointment_time})
    if existing_dup:
        print(f"Запись уже существует для пациента {patient_id} в {appointment_time}")
        return None
    new_appt = {"patient_id": patient_id, "appointment_time": appointment_time, "status": "pending", "notes": notes}
    appointments.append(new_appt)
    print(f"Запись создана: пациент {patient_id} на {appointment_time}")
    return new_appt
