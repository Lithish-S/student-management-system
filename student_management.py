FILE_NAME = "students.txt"

def add_student():
    with open(FILE_NAME, "a") as file:
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")
        file.write(f"{sid},{name},{marks}\n")
    print("Student added successfully!\n")

def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nID\tName\tMarks")
            print("-" * 25)
            for line in file:
                sid, name, marks = line.strip().split(",")
                print(f"{sid}\t{name}\t{marks}")
    except FileNotFoundError:
        print("No records found.\n")

def search_student():
    sid = input("Enter Student ID to search: ")
    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == sid:
                print("Student Found:")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Marks:", data[2])
                found = True
                break
    if not found:
        print("Student not found.\n")

def update_student():
    sid = input("Enter Student ID to update: ")
    lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == sid:
                name = input("Enter new name: ")
                marks = input("Enter new marks: ")
                file.write(f"{sid},{name},{marks}\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            data = line.strip().split(",")
            if data[0] != sid:
                file.write(line)
            else:
                found = True

    if found:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
