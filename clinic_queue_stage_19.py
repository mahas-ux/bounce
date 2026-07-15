# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: ClinicQueue
def archive_records(archive_file, min_date=None):
    """Archive completed or old records to a separate file."""
    archived = []
    with open("clinic_queue.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["status"] == "completed" or (min_date and row["date"] < min_date):
                archived.append(row)
    if not archived:
        print("No records to archive.")
        return

    with open(archive_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(reader.fieldnames))
        writer.writeheader()
        for row in archived:
            writer.writerow(row)

    count = len(archived)
    print(f"Archived {count} record(s) to '{archive_file}'.")


if __name__ == "__main__":
    archive_records("clinic_queue_archive.csv", min_date="2024-12-31")
