# === Stage 17: Добавь группировку записей по категориям ===
# Project: ClinicQueue
def _group_appointments(self):
        by_category = {}
        for appt in self.appointments:
            cat = appt.category or 'General'
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(appt)
        return dict(sorted(by_category.items(), key=lambda x: list(x[1])[0].scheduled_at))
