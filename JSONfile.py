import json

with open("data.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("Age:", data["age"])
