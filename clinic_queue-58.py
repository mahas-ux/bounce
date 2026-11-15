# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: ClinicQueue
def register_view(name, func):
    if name in VIEW_REGISTRY:
        raise ValueError(f"Представление {name} уже существует")
    VIEW_REGISTRY[name] = func
    return func

def render_view(name, data):
    if name not in VIEW_REGISTRY:
        raise KeyError(f"Представление {name} не найдено")
    return VIEW_REGISTRY[name](data)
