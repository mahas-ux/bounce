# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: ClinicQueue
class UserProfile:
    def __init__(self, name, role="patient"):
        self.name = name
        self.role = role  # "patient", "doctor", "admin"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, role={self.role!r})"

_profiles_cache = None

def get_user_profile(name, default_role="patient"):
    global _profiles_cache
    if _profiles_cache is None:
        _profiles_cache = {}
    
    profile_name = name.lower().strip()
    if profile_name in _profiles_cache:
        return _profiles_cache[profile_name]
    
    role_map = {
        "doctor": "doctor",
        "admin": "admin",
        "patient": default_role,
    }
    role = role_map.get(profile_name) or default_role
    
    profile = UserProfile(name, role)
    _profiles_cache[profile_name] = profile
    return profile

def get_current_user():
    name = input("Введите ваше имя: ").strip()
    if not name:
        print("Имя не может быть пустым.")
        return None
    return get_user_profile(name)
