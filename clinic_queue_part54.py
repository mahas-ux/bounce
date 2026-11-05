# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: ClinicQueue
import json

def load_favorites():
    try:
        with open("clinic_favorites.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_favorites(favorites):
    with open("clinic_favorites.json", "w", encoding="utf-8") as f:
        json.dump(favorites, f, ensure_ascii=False, indent=2)

def toggle_favorite(appointments, appt_id):
    favorites = load_favorites()
    if appt_id in favorites:
        favorites.remove(appt_id)
    else:
        favorites.append(appt_id)
    save_favorites(favorites)
    return favorites

def get_favorites(appointments):
    favorites = load_favorites()
    return [a for a in appointments if a["id"] in favorites]

def print_favorite_menu(appointments):
    favorites = get_favorites(appointments)
    print("\nИзбранные записи:")
    if not favorites:
        print("  (пока пусто, нажмите F на нужной записи)")
    for a in favorites:
        print(f"  [{a['id']}] {a['patient']} — {a['time']} ({a['status']})")
    print()
