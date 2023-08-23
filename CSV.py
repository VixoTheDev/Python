import csv

# Writing to a CSV file
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
    writer.writerow(["Bob", 30])

# Reading from a CSV file
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print("Row:", row)
