import json

with open("events.json", "r") as file:
    data = json.load(file)

print(json.dumps(data[:2], indent=4))  # Print first 2 items neatly formatted