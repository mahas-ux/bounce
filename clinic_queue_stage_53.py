# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: ClinicQueue
def load_records(path):
    """Загружает записи из текстового файла в список словарей.

    Формат каждой строки:
    id|имя|дата|время|статус|заметка
    """
    records = []
    if not path or not os.path.exists(path):
        return records
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fields = line.split("|")
            if len(fields) < 5:
                continue
            rec = {
                "id": fields[0].strip(),
                "name": fields[1].strip(),
                "date": fields[2].strip(),
                "time": fields[3].strip(),
                "status": fields[4].strip(),
                "note": fields[5].strip() if len(fields) > 5 else "",
            }
            records.append(rec)
    return records
