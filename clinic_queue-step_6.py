# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: ClinicQueue
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record.get('status') != status:
            continue
        if category and record.get('category') != category:
            continue
        if tags is not None:
            rec_tags = set(record.get('tags', []))
            if not any(t in rec_tags for t in tags):
                continue
        filtered.append(record)
    return filtered

def search_records(query=None, limit=10):
    results = []
    query_lower = query.lower() if query else ''
    for record in records:
        text = f"{record.get('name', '')} {record.get('notes', '')}".lower()
        if query_lower and query_lower not in text:
            continue
        status, category, tags = filter_records(record['status'], record['category'], record['tags'])
        results.append(record)
    return results[:limit]
