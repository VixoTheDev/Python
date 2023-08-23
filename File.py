# Write data to a file
with open("data.txt", "w") as file:
    file.write("Hello, this is some data!")

# Read data from the file
with open("data.txt", "r") as file:
    data = file.read()
    print("Data from file:", data)
