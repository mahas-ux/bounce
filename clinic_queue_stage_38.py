# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: ClinicQueue
import unittest
from clinic_queue import ClinicQueue, Patient, Appointment


class TestEdgeCases(unittest.TestCase):

    def setUp(self):
        self.queue = ClinicQueue()
        self.patient1 = Patient("Иванов", "2025-12-01 10:00", "ожидание", "первый")
        self.patient2 = Patient("Петров", "2025-12-01 10:30", "ожидание", "второй")
        self.patient3 = Patient("Сидоров", "2025-12-01 11:00", "ожидание", "третий")

    def test_add_duplicate_patient(self):
        self.queue.add_patient(self.patient1)
        with self.assertRaises(ValueError):
            self.queue.add_patient(self.patient1)

    def test_add_patient_with_empty_name(self):
        empty_patient = Patient("", "2025-12-01 10:00", "ожидание", "")
        with self.assertRaises(ValueError):
            self.queue.add_patient(empty_patient)

    def test_add_patient_with_empty_time(self):
        empty_time_patient = Patient("Иванов", "", "ожидание", "первый")
        with self.assertRaises(ValueError):
            self.queue.add_patient(empty_time_patient)

    def test_add_patient_with_invalid_time(self):
        invalid_time_patient = Patient("Иванов", "2025-13-01 10:00", "ожидание", "первый")
        with self.assertRaises(ValueError):
            self.queue.add_patient(invalid_time_patient)

    def test_add_patient_with_empty_note(self):
        empty_note_patient = Patient("Иванов", "2025-12-01 10:00", "ожидание", "")
        with self.assertRaises(ValueError):
            self.queue.add_patient(empty_note_patient)

    def test_remove_nonexistent_patient(self):
        self.queue.add_patient(self.patient1)
        with self.assertRaises(ValueError):
            self.queue.remove_patient("Не существующий пациент")

    def test_remove_patient_not_in_queue(self):
        self.queue.add_patient(self.patient1)
        with self.assertRaises(ValueError):
            self.queue.remove_patient(self.patient2)

    def test_remove_all_patients(self):
        self.queue.add_patient(self.patient1)
        self.queue.add_patient(self.patient2)
        self.queue.add_patient(self.patient3)
        self.queue.remove_patient(self.patient1)
        self.queue.remove_patient(self.patient2)
        self.queue.remove_patient(self.patient3)
        self.assertEqual(len(self.queue.patients), 0)

    def test_remove_patient_with_empty_name(self):
        self.queue.add_patient(self.patient1)
        with self.assertRaises(ValueError):
            self.queue.remove_patient(Patient("", "", "ожидание", ""))

    def test_remove_patient_with_empty_time(self):
        self.queue.add_patient(self.patient1)
        with self.assertRaises(ValueError):
            self.queue.remove_patient(Patient("Петров", "", "ожидание", ""))

    def test_remove_patient_with_empty_note(self):
        self.queue.add_patient(self.patient1)
        with self.assertRaises(ValueError):
            self.queue.remove_patient(Patient("Петров", "2025-12-01 10:00", "ожидание", ""))

    def test_remove_patient_with_invalid_time(self):
        self.queue.add_patient(self.patient1)
        with self.assertRaises(ValueError):
            self.queue.remove_patient(Patient("Петров", "2025-13-01 10:00", "ожидание", ""))

    def test_add_patient_with_empty_surname(self):
        empty_surname_patient = Patient("", "2025-12-01 10:00", "ожидание", "первый")
        with self.assertRaises(ValueError):
            self.queue.add_patient(empty_surname_patient)

    def test_add_patient_with_empty_surname_and_note(self):
        empty_patient = Patient("", "", "ожидание", "")
        with self.assertRaises(ValueError):
            self.queue.add_patient(empty_patient)

    def test_add_patient_with_only_surname(self):
        partial_patient = Patient("Иванов", "", "ожидание", "")
        with self.assertRaises(ValueError):
            self.queue.add_patient(partial_patient)

    def test_add_patient_with_only_time(self):
        partial_patient = Patient("", "2025-12-01 10:00", "ожидание", "")
        with self.assertRaises(ValueError):
            self.queue.add_patient(partial_patient)

    def test_add_patient_with_only_note(self):
        partial_patient = Patient("", "", "ожидание", "первый")
        with self.assertRaises(ValueError):
            self.queue.add_patient(partial_patient)


if __name__ == "__main__":
    unittest.main()
