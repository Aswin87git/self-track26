import json

def create_tracker():
    task = input("Enter task name: ")
    days = int(input("Enter number of days: "))

    data = {
        "task": task,
        "days": [{"day": i+1, "done": False, "note": ""} for i in range(days)]
    }

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Tracker created!")

create_tracker()


