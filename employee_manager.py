import pandas as pd

# Load employee data
def load_data():
    return pd.read_csv("employees.csv")

# Display all employee records
def display_employees(data):
    print("\n--- Employee List ---")
    print(data)

# Add a new employee
def add_employee(data):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    new_employee = pd.DataFrame({
        'Name': [name],
        'Age': [age],
        'Department': [department],
        'Salary': [salary]
    })

    updated_data = pd.concat([data, new_employee], ignore_index=True)
    print("✅ Employee added successfully!")
    return updated_data

# Delete an employee by name
def delete_employee(data):
    name = input("Enter name to delete: ")
    updated_data = data[data['Name'] != name]
    print("✅ Employee deleted successfully!")
    return updated_data

# Update employee salary
def update_salary(data):
    name = input("Enter employee name to update salary: ")
    new_salary = float(input("Enter new salary: "))
    data.loc[data['Name'] == name, 'Salary'] = new_salary
    print("✅ Salary updated successfully!")
    return data

# Filter employees by department
def filter_by_department(data):
    dept = input("Enter department to filter: ")
    filtered = data[data['Department'] == dept]
    print(f"\n--- Employees in {dept} Department ---")
    print(filtered)

# Save data to file
def save_data(data):
    data.to_csv("employees.csv", index=False)
    print("✅ Data saved successfully!")

# Main menu loop
def main():
    data = load_data()

    while True:
        print("\n=== Employee Data Manager ===")
        print("1. Display Employees")
        print("2. Add Employee")
        print("3. Delete Employee")
        print("4. Update Salary")
        print("5. Filter by Department")
        print("6. Save and Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            display_employees(data)
        elif choice == '2':
            data = add_employee(data)
        elif choice == '3':
            data = delete_employee(data)
        elif choice == '4':
            data = update_salary(data)
        elif choice == '5':
            filter_by_department(data)
        elif choice == '6':
            save_data(data)
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
