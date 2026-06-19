from datetime import datetime

print("Welcome to the Interactive Personal Data Collector!\n")

# Collect user input
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

# Display collected data with type and memory address
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {fav_number} (Type: {type(fav_number)}, Memory Address: {id(fav_number)})")

# Calculate approximate birth year
current_year = datetime.now().year
birth_year = current_year - age

print(f"\nYour birth year is approximately: {birth_year} "
      f"(based on your age of {age})")

print("\nThank you for using the Personal Data Collector. Goodbye!")
