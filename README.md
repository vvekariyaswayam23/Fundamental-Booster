🚀 Personal Data Collector

A beginner-friendly Python project that collects user information, displays data types and memory addresses, and calculates an approximate birth year.






📖 About the Project

The Interactive Personal Data Collector is a simple Python console application designed to help beginners understand:

📝 User Input
🔄 Type Conversion (int, float, str)
🏷️ Data Types
🧠 Memory Addresses using id()
📅 Date & Time Operations
🎯 Formatted String Output (f-strings)

This project is perfect for Python beginners learning the fundamentals of programming.

✨ Features

✅ Collects user details interactively

✅ Displays the data type of each input

✅ Shows the memory address of stored variables

✅ Calculates approximate birth year

✅ Uses Python's datetime module

✅ Clean and beginner-friendly code

🛠️ Technologies Used
Technology	Purpose
🐍 Python	Main Programming Language
📅 datetime	Birth Year Calculation
💻 Console	User Interaction
📂 Project Structure
Personal-Data-Collector/
│
├── Fundamental Booster.py
├── README.md
└── Screenshot.png
📜 Source Code
from datetime import datetime

print("Welcome to the Interactive Personal Data Collector!\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {fav_number} (Type: {type(fav_number)}, Memory Address: {id(fav_number)})")

current_year = datetime.now().year
birth_year = current_year - age

print(f"\nYour birth year is approximately: {birth_year}")
🖥️ Program Demo
📸 Output Screenshot

Save your screenshot inside the project folder and rename it as:

Screenshot.png

Then add:

## 📸 Screenshot

<img width="568" height="200" alt="Screenshot 2026-06-19 175246" src="https://github.com/user-attachments/assets/bae67642-35f2-43d0-bf76-e9b6ed3d9b5b" />


Or if your screenshot is stored in GitHub:

## 📸 Screenshot

![Program Output](https://github.com/your-username/your-repository/blob/main/Screenshot.png)
🎯 Sample Output
Welcome to the Interactive Personal Data Collector!

Please enter your name: Swayam
Please enter your age: 20
Please enter your height in meters: 5.2
Please enter your favourite number: 4

Thank you! Here is the information we collected:

Name: Swayam
Age: 20
Height: 5.2
Favourite Number: 4

Your birth year is approximately: 2006
🚀 How to Run
1️⃣ Clone the Repository
git clone https://github.com/your-username/personal-data-collector.git
2️⃣ Navigate to Project Folder
cd personal-data-collector
3️⃣ Run the Program
python "Fundamental Booster.py"
🎓 Concepts Practiced
Variables
Input/Output
Data Types
Type Casting
Functions
Memory Management
Date & Time
String Formatting
🌟 Future Improvements
🔐 Add input validation
📊 Calculate BMI
💾 Save user data to a file
🎨 Create GUI using Tkinter
🌐 Build a Web Version using Flask
🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to fork the repository and submit a pull request.

👨‍💻 Author

Swayam

🌟 If you like this project, don't forget to Star ⭐ the repository!
