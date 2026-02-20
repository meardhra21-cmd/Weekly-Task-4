class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def increase_salary(self, amount):
        if amount > 0:
            self.salary += amount
            print("Salary increased successfully!")
        else:
            print("Increase amount must be positive.")

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


emp1 = Employee("Ardhra", 101, 30000)

emp1.display_details()
emp1.increase_salary(5000)
emp1.display_details()
