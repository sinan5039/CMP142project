name = input("Enter your name: ")
age = input("Enter your age: ")

with open("users.txt", "a") as file:       # Open the file in append mode.Save to users.txt
    file.write(f"Name: {name}, Age: {age}\n")  # Write the name and age to the file.

print("\nAll saved users:")
with open("users.txt", "r") as file:       # Open the file in read mode.
    for line in file:                      # Read each line in the file.
        print(line.strip())                # Print the line without extra newlines.
    