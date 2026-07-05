# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: ClinicQueue
def search_patients(query: str) -> list[dict]:
    if not query.strip():
        return []
    q = query.lower()
    results = [p for p in patients.values() if (q in p.get('name', '').lower() or 
                                                 q in p.get('phone', '').replace('-', '') or 
                                                 q in p.get('notes', '').lower())]
    return sorted(results, key=lambda x: x['appointment_time'])
