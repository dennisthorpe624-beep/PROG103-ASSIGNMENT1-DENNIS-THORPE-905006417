Clinic Queue Management System
📌 Project Description

The Clinic Queue Management System is a simple Python program designed to help a clinic manage patient queues efficiently.
It allows clinic staff to add patients, automatically assign priority levels based on age, and view all patients currently waiting for service.

This system helps organize patient flow and ensures elderly patients and children receive appropriate attention.

🎯 Purpose of the System

The program is used to:

Register patients arriving at a clinic
Automatically assign treatment priority
Maintain a waiting queue
Display patient information clearly
Improve clinic service organization
⚙️ Features

✅ Add new patients to the queue
✅ Automatic priority assignment based on age
✅ View all patients waiting in the clinic
✅ Simple menu-driven interface
✅ Continuous operation until user exits

🧠 Priority Rules

The system assigns priority levels using patient age:

Age Range	Priority Level
60 years and above	High Priority
18 – 59 years	Normal Priority
Below 18 years	Child Priority
🏗️ How the System Works
User selects an option from the menu:
Add Patient
View All Patients
Exit
When adding a patient:
User enters patient name
User enters patient age
System automatically determines priority level
Patient details are stored in a queue list.
Viewing patients displays all registered patients with their assigned priorities.
💻 Requirements
Python 3.x installed
Command line or terminal environment
▶️ How to Run the Program
Save the code as:
clinic_queue.py
Open terminal or command prompt.
Run the program:
python clinic_queue.py
Follow the on-screen menu instructions.
📂 System Structure
Functions Used

assign_priority(age)
Determines patient priority based on age.

display_patient(name, age, priority)
Displays formatted patient information.

📈 Benefits
Reduces patient waiting confusion
Helps staff manage queues easily
Gives priority to elderly patients
Simple and beginner-friendly system
🔮 Possible Future Improvements
Sort patients automatically by priority
Save patient data to a file or database
Add patient ID numbers
Add appointment scheduling
Create a graphical user interface (GUI)
👨‍💻 Author

Clinic Queue Management System Project
Python Programming Practice
