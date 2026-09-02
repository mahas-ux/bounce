# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: ClinicQueue
import unittest


class TestClinicQueue(unittest.TestCase):

    def test_add_patient(self):
        q = ClinicQueue()
        q.add_patient("Иванов", "14:00", "Ожидание", "Док")
        self.assertEqual(len(q), 1)

    def test_add_multiple_patients(self):
        q = ClinicQueue()
        q.add_patient("Петров", "14:00", "Ожидание", "Док")
        q.add_patient("Сидоров", "14:15", "Ожидание", "Док")
        q.add_patient("Кузнецов", "14:30", "Ожидание", "Док")
        self.assertEqual(len(q), 3)

    def test_get_next_patient(self):
        q = ClinicQueue()
        q.add_patient("Иванов", "14:00", "Ожидание", "Док")
        q.add_patient("Петров", "14:15", "Ожидание", "Док")
        q.get_next_patient("Иванов")
        self.assertEqual(q.current_patient, "Петров")
        self.assertEqual(q.next_patient, "Кузнецов")

    def test_add_note(self):
        q = ClinicQueue()
        q.add_patient("Иванов", "14:00", "Ожидание", "Док")
        q.add_note("Иванов", "Пришёл с сыном")
        self.assertIn("Пришёл с сыном", q.notes.get("Иванов", []))

    def test_cancel_patient(self):
        q = ClinicQueue()
        q.add_patient("Иванов", "14:00", "Ожидание", "Док")
        q.add_patient("Петров", "14:15", "Ожидание", "Док")
        q.cancel_patient("Иванов")
        self.assertNotIn("Иванов", q.patients)

    def test_finish_patient(self):
        q = ClinicQueue()
        q.add_patient("Иванов", "14:00", "Ожидание", "Док")
        q.finish_patient("Иванов")
        self.assertEqual(q.current_patient, None)
        self.assertEqual(q.next_patient, "Петров")


if __name__ == "__main__":
    unittest.main()
