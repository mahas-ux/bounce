# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: ClinicQueue
def dry_run(operation, *, original, modified, reason=""):
    """Return a human-readable description of a hypothetical change without persisting."""
    parts = [
        f"[DRY-RUN] {operation}:",
        f"  original: {original}",
        f"  modified: {modified}",
    ]
    if reason:
        parts.append(f"  reason:   {reason}")
    return "\n".join(parts)
