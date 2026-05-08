# Clinic Queue Management System

def assign_priority(age):
    if age >= 60:
        return "High Priority"
    elif age >= 18:
        return "Normal Priority"
    else:
        return "Child Priority"

def display_patient(name, age, priority):
    print("\n--- Patient Details ---")
    print("Name:", name)
    print("Age:", age)
    print("Priority Level:", priority)
    print("-----------------------")

# Main program
queue = []

while True:
    print("\n1. Add Patient")
    print("2. View All Patients")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))

        priority = assign_priority(age)
        queue.append((name, age, priority))

        print("Patient added successfully!")

    elif choice == "2":
        if len(queue) == 0:
            print("No patients in queue.")
        else:
            print("\n--- Clinic Queue ---")
            for patient in queue:
                display_patient(patient[0], patient[1], patient[2])

    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid option. Try again.")