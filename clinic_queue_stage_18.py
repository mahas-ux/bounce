# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: ClinicQueue
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"


class Appointment:
    def __init__(self, patient_name, time, status="pending", note="", tags=None):
        self.patient_name = patient_name
        self.time = time
        self.status = status
        self.note = note
        self.tags = tags if isinstance(tags, list) else []

    def add_tag(self, tag_name):
        new_tag = Tag(tag_name)
        if not any(t.name == new_tag.name for t in self.tags):
            self.tags.append(new_tag)
        return self

    def remove_tag(self, tag_name):
        if tag_name:
            self.tags = [t for t in self.tags if t.name != tag_name]
        return self


class ClinicQueue:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, patient_name, time, status="pending", note="", tags=None):
        appointment = Appointment(patient_name, time, status, note, tags)
        self.appointments.append(appointment)
        return appointment

    def get_appointments_by_status(self, status):
        return [a for a in self.appointments if a.status == status]

    def remove_appointment(self, index):
        if 0 <= index < len(self.appointments):
            removed = self.appointments.pop(index)
            print(f"Appointment with {removed.patient_name} at {removed.time} has been removed.")
            return removed
        else:
            raise IndexError("Appointments list is empty or index is out of range")

    def get_appointment_count(self):
        return len(self.appointments)


clinic_queue = ClinicQueue()
appointment1 = clinic_queue.add_appointment("John Doe", "2024-06-15 09:00", note="First visit")
print(f"Added appointment for {appointment1.patient_name}")

appointment2 = clinic_queue.add_appointment("Jane Smith", "2024-06-15 10:00", tags=["urgent", "follow-up"])
print(f"Appointment for {appointment2.patient_name} has tags: {[t.name for t in appointment2.tags]}")

appointment3 = clinic_queue.add_appointment("Bob Johnson", "2024-06-15 11:00", tags=["regular"])
appointment3.remove_tag("regular")
print(f"Appointment for {appointment3.patient_name} has no tags now.")

urgent_appointments = clinic_queue.get_appointments_by_status("pending")
print(f"Pending appointments: {[a.patient_name for a in urgent_appointments]}")
