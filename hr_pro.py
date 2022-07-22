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

    def get_bonus(self):
        return int(self.bonus_percentage * self.salary)

    def __str__(self):
        prefix = super().__str__()
        return f"{prefix}, Bonus Percentage: {self.get_bonus()}"


# Displays to the user the available options (does not return anything)
def options(options):
    print("---------\n")
    print("Options: ")
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

    options_list = [
        "Show Employees",
        "Show Managers",
        "Add An Employee",
        "Add A Manager",
        "Exit"
    ]

    # start of program
    print("Welcome to HR Pro 2022")
    # to loop through the options until the user exits
    user_choice = 0
    while user_choice != 5:
        user_choice = options(options_list)
        if user_choice == 1:
            print(">>> Employees <<<\n")
            for i, employee in enumerate(employees, 1):
                print(f"{i}. {employee}")

        elif user_choice == 2:
            print(">>> Managers <<<\n")
            for i, manager in enumerate(managers, 1):
                print(f"{i}. {manager}")

        elif user_choice == 3:
            employees.append(add_employee())

        elif user_choice == 4:
            managers.append(add_manager())

        elif user_choice > 5:
            print("Enter a number from the list!")

    print("You have exited the program!")


if __name__ == '__main__':
    main()
