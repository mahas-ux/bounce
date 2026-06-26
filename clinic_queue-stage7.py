# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: ClinicQueue
def sort_queue(records, key='date'):
    if not records: return []
    reverse = {'priority': True}.get(key, False)
    def _sort_key(r):
        val = r.get(key or 'date', 0)
        if isinstance(val, str):
            try: val = datetime.strptime(val, '%Y-%m-%d %H:%M').timestamp()
            except ValueError: pass
        return (val is None, -1 if reverse else 1, val)
    return sorted(records, key=_sort_key)
