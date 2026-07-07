# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: ClinicQueue
def generate_summary(queue):
    """Генерирует краткую сводку по текущим данным очереди."""
    if not queue:
        return "Очередь пуста."
    
    total = len(queue)
    active = sum(1 for p in queue if p.status == 'в ожидании')
    completed = sum(1 for p in queue if p.status == 'завершен')
    upcoming = sum(1 for p in queue if p.status in ('прием', 'на прием'))
    
    # Получаем первого пациента для примера
    first_patient = queue[0] if queue else None
    
    summary_lines = [
        f"=== СВОДКА ПО ОЧЕРЕДИ ===",
        f"Всего записей: {total}",
        f"В ожидании: {active}",
        f"На приеме/на прием: {upcoming}",
        f"Завершенных: {completed}",
    ]
    
    if first_patient:
        summary_lines.append(f"Первый пациент: {first_patient.name} ({first_patient.time})")
        
        if hasattr(first_patient, 'notes') and first_patient.notes:
            summary_lines.append(f"Заметка: {first_patient.notes}")
            
        if hasattr(first_patient, 'doctor') and first_patient.doctor:
            summary_lines.append(f"Врач: {first_patient.doctor}")
    
    return "\n".join(summary_lines)

print(generate_summary(visit_queue))
