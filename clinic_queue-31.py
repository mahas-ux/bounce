# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: ClinicQueue
import json


class ProfileManager:
    """Управление переключением активного профиля."""

    def __init__(self, profiles_path="profiles.json"):
        self.profiles_path = profiles_path
        self.active_profile = "default"
        self._load_profiles()

    def _load_profiles(self):
        if not os.path.exists(self.profiles_path):
            return
        with open(self.profiles_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.profiles = {k: v for k, v in data.get('profiles', {}).items()}

    def list_profiles(self):
        print("\n=== Доступные профили ===")
        if not self.profiles:
            print("Нет сохранённых профилей.")
            return []
        for name, profile in self.profiles.items():
            active_mark = " (активен)" if name == self.active_profile else ""
            print(f"  [{name}]{active_mark}: {profile.get('display_name', 'Без имени')}")
        return list(self.profiles.keys())

    def switch_profile(self, new_profile):
        if not self.profiles:
            print("Сначала создайте профиль через create_profile()")
            return False
        if new_profile not in self.profiles:
            print(f"Профиль '{new_profile}' не найден.")
            return False
        old_profile = self.active_profile
        self.active_profile = new_profile
        with open(self.profiles_path, 'w', encoding='utf-8') as f:
            json.dump({'profiles': self.profiles}, f, ensure_ascii=False, indent=2)
        print(f"\nПереключён на профиль: {new_profile} (с предыдущего: {old_profile})")
        return True

    def create_profile(self, name, display_name="Новый пользователь"):
        if name in self.profiles:
            print(f"Профиль '{name}' уже существует.")
            return False
        self.profiles[name] = {"display_name": display_name}
        with open(self.profiles_path, 'w', encoding='utf-8') as f:
            json.dump({'profiles': self.profiles}, f, ensure_ascii=False, indent=2)
        print(f"Создан профиль: {name}")
        return True


# Инициализация менеджера профилей в ClinicQueue
profile_manager = ProfileManager()
