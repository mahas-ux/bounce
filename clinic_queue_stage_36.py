# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: ClinicQueue
def _integrity_check(queue, issues=None):
    if issues is None:
        issues = []
    if not isinstance(queue, list):
        issues.append("queue is not a list")
        return issues
    for i, patient in enumerate(queue):
        if not isinstance(patient, dict):
            issues.append(f"patient at index {i} is not a dict")
            continue
        if not isinstance(patient.get("name"), str) or not patient["name"]:
            issues.append(f"patient at index {i} has invalid name")
        if not isinstance(patient.get("time"), (int, float)) or patient["time"] < 0:
            issues.append(f"patient at index {i} has invalid time")
        if not isinstance(patient.get("status"), str):
            issues.append(f"patient at index {i} has invalid status")
        if not isinstance(patient.get("notes"), (str, type(None))):
            issues.append(f"patient at index {i} has invalid notes")
    return issues


def repair_queue(queue):
    if isinstance(queue, list):
        fixed = []
        for patient in queue:
            if isinstance(patient, dict):
                fixed.append({
                    "name": patient["name"] if isinstance(patient["name"], str) else "",
                    "time": patient["time"] if isinstance(patient["time"], (int, float)) and patient["time"] >= 0 else 0,
                    "status": patient["status"] if isinstance(patient["status"], str) else "pending",
                    "notes": patient["notes"] if isinstance(patient["notes"], str) else "",
                })
            else:
                fixed.append({"name": "", "time": 0, "status": "pending", "notes": ""})
        return fixed
    return []
