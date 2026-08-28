# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: ClinicQueue
TEMPLATE_PRESETS = {
    'checkup': {'duration': 15, 'status': 'pending', 'note': 'Routine checkup'},
    'flu': {'duration': 10, 'status': 'pending', 'note': 'Flu shot'},
    'surgery': {'duration': 120, 'status': 'pending', 'note': 'Surgery scheduled'},
    'consult': {'duration': 30, 'status': 'pending', 'note': 'Consultation'},
}

def apply_template(visit, template_name):
    if template_name in TEMPLATE_PRESETS:
        for key, value in TEMPLATE_PRESETS[template_name].items():
            if key in visit:
                visit[key] = value
        return visit
    return visit
