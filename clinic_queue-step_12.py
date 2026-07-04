# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: ClinicQueue
def load_from_json(file_path):
    try:
        import json
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [Patient(**item) for item in data]
        raise ValueError("JSON должен содержать массив пациентов")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {file_path}: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных из {file_path}: {type(e).__name__}")
        return []
