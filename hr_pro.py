from datetime import datetime


class Employee:
   # Employee class here
    today = datetime.today().year

    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        return int(self.today - self.employment_year)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}"


class Manager(Employee):
    # Manager class here
    today = datetime.today().year

    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def get_working_years(self):
        return super().get_working_years()

    def get_bonus(self):
        return int(self.bonus_percentage * self.salary)

    def __str__(self):
        prefix = super().__str__()
        return f"{prefix}, Bonus Percentage: {self.get_bonus()}"


# Displays to the user the available options (does not return anything)
def options():
    print("---------\n")
    print("Options: ")
    options = [
        "Show Employees",
        "Show Managers",
        "Add An Employee",
        "Add A Manager",
        "Exit"
    ]

    for i, option in enumerate(options, 1):
        print(f"    {i}. {option}")
    # takes user input to get the option chosen
    user_choice = int(input("\nWhat would you like to do? "))
    print("\n---------")
    return user_choice


# adds an employee and returns that employee
def add_employee():
    name = input("Name: ")
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    employment_year = int(input("Employment Year: "))
    employee = Employee(
        name=name,
        age=age,
        salary=salary,
        employment_year=employment_year
    )
    print("\n**** Employee Added Successfully ****")
    return employee


# Adds a manger and returns that manager
def add_manager():
    name = input("Name: ")
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    employment_year = int(input("Employment Year: "))
    bonus_percentage = float(input("Bonus Percentage: "))
    manager = Manager(
        name=name,
        age=age,
        salary=salary,
        employment_year=employment_year,
        bonus_percentage=bonus_percentage
    )

    print("\n**** Manager Added Successfully ****")
    return manager


def main():
    # main code here
    employees = []
    managers = []
    to_exit = True
    # start of program
    print("Welcome to HR Pro 2022")
    # to loop through the options until the user exits
    while to_exit:
        user_choice = options()
        if user_choice == 1:
            print(">>> Employees <<<\n")
            for i, employee in enumerate(employees, 1):
                print(f"{i}. {employee.__str__()}")

        elif user_choice == 2:
            print(">>> Managers <<<\n")
            for i, manager in enumerate(managers, 1):
                print(f"{i}. {manager.__str__()}")

        elif user_choice == 3:
            employee = add_employee()
            employees.append(employee)

        elif user_choice == 4:
            manager = add_manager()
            managers.append(manager)

        elif user_choice == 5:
            print("You have exited the program!")
            to_exit = False
        else:
            print("Enter a number from the list!")


if __name__ == '__main__':
    main()
