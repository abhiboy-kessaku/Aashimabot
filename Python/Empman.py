class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: ₹{self.salary}")


class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, department, salary):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("Employee with this ID already exists.")
                return
        employee = Employee(emp_id, name, department, salary)
        self.employees.append(employee)
        print(f"Employee '{name}' added successfully.")

    def view_employees(self):
        if not self.employees:
            print("No employees in the system.")
        else:
            print("\nAll Employees:")
            for emp in self.employees:
                emp.display()

    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("Employee Found:")
                emp.display()
                return
        print("Employee not found.")

    def remove_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f"Employee with ID '{emp_id}' removed.")
                return
        print("Employee not found to remove.")


# Main Program
def main():
    system = EmployeeManagement()

    while True:
        print("\n=== Employee Management Menu ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Remove Employee by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            department = input("Enter department: ")
            salary = float(input("Enter salary: ₹"))
            system.add_employee(emp_id, name, department, salary)

        elif choice == '2':
            system.view_employees()

        elif choice == '3':
            emp_id = input("Enter employee ID to search: ")
            system.search_employee(emp_id)

        elif choice == '4':
            emp_id = input("Enter employee ID to remove: ")
            system.remove_employee(emp_id)

        elif choice == '5':
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
