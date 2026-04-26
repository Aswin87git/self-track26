import json

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return None

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def create_tracker():
    task = input("Enter task name: ")
    days = int(input("Enter number of days: "))

    data = {
        "task": task,
        "days": [{"day": i+1, "done": False, "note": ""} for i in range(days)]
    }

    save_data(data)
    print("Tracker created!")

def show_tracker(data):
    print("\nTask:", data["task"])
    for d in data["days"]:
        status = "X" if d["done"] else " "
        note = f" - {d['note']}" if d["note"] else ""
        print(f"Day {d['day']} [{status}]{note}")

def mark_day(data):
    day = int(input("Enter day number: "))
    data["days"][day-1]["done"] = True
    save_data(data)
    print("Marked as done!")

def add_note(data):
    day = int(input("Enter day number: "))
    note = input("Enter note: ")
    data["days"][day-1]["note"] = note
    save_data(data)
    print("Note added!")

def main():
    while True:
        print("\n1. Create Tracker")
        print("2. Show Tracker")
        print("3. Mark Day")
        print("4. Add Note")
        print("5. Exit")

        choice = input("Choose: ")

        data = load_data()

        if choice == "1":
            create_tracker()
        elif choice == "2":
            if data:
                show_tracker(data)
            else:
                print("No tracker found")
        elif choice == "3":
            if data:
                mark_day(data)
            else:
                print("No tracker found")
        elif choice == "4":
            if data:
                add_note(data)
            else:
                print("No tracker found")
        elif choice == "5":
            break
        else:
            print("Invalid choice")

main()
