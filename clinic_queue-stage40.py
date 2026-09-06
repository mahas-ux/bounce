# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: ClinicQueue
def main():
    parser = argparse.ArgumentParser(description="ClinicQueue CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    add_p = sub.add_parser("add", help="add appointment")
    add_p.add_argument("patient", help="patient name")
    add_p.add_argument("time", help="appointment time")
    add_p.add_argument("--note", help="optional note", default="")
    show_p = sub.add_parser("show", help="show queue")
    sub.add_parser("done", help="mark next done")
    args = parser.parse_args()
    if args.command == "add":
        try:
            with open("clinic_queue.txt", "a") as f:
                f.write(f"{args.patient}|{args.time}|{args.note}\n")
            print(f"Added: {args.patient} at {args.time}")
        except OSError as e:
            print(f"Error: {e}")
    elif args.command == "show":
        try:
            with open("clinic_queue.txt") as f:
                lines = f.readlines()
            if not lines:
                print("Queue is empty.")
            else:
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.strip()}")
        except FileNotFoundError:
            print("Queue file not found.")
    elif args.command == "done":
        try:
            with open("clinic_queue.txt") as f:
                lines = f.readlines()
            if not lines:
                print("Queue is empty.")
            else:
                with open("clinic_queue.txt", "w") as f:
                    f.writelines(lines[1:])
                print(f"Marked patient {lines[0].split('|')[0]} as done.")
        except FileNotFoundError:
            print("Queue file not found.")

if __name__ == "__main__":
    main()
