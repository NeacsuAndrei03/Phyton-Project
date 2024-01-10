class Employee:
    """Common base class for all employees"""
    empCount = 0
#X=NEACSU
#Y=ANDREI
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        """Displays the number of employees"""
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        """Displays employee details"""
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Tasks with status {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    """Manager class inheriting from Employee"""

    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = "D5 " + department  # Prefix department name with "D5"
        Manager.mgr_count += 1

    def display_employee(self):
        """Displays only the name of the employee"""
        print("Name : ", self.name)

# Creating instances of Employee and Manager classes
emp1 = Employee("Radu Popa", 50000)
emp2 = Employee("Popescu Traian", 60000)

mgr1 = Manager("Neacsu Andrei", 80000, "Finance")
mgr2 = Manager("Vladislav Noris", 75000, "Marketing")

# Displaying employees and managers
print("Displaying all employees:")
emp1.display_employee()
emp2.display_employee()

print("\nDisplaying all managers:")
mgr1.display_employee()
mgr2.display_employee()

# Displaying counts of employees and managers
print(f"\nEmployee count: {emp1.empCount}")
print(f"Manager count: {mgr1.mgr_count}")
