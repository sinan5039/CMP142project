# Define a base class called 'school'
class school:
    def __init__(self, name, surname, age, salary):
        self.name = name              # Store the name of the person
        self.surname = surname        # Store the surname of the person
        self.age = age                # Store the age of the person
        self.salary = salary          # Store the salary of the person
        print("The school class worked.")  # Print message when object is created

    def info(self):
        # Display general information about the school worker
        print(f"{self.name} {self.surname} is {self.age} years old and a school worker with a salary of {self.salary} TL.")

    def increase(self):
        # Increase salary by 20% and return the new salary
        return self.salary * 1.2


# Define a subclass 'teacher' that inherits from 'school'
class teacher(school):
    def __init__(self, name, surname, age, salary, department):
        super().__init__(name, surname, age, salary)  # Call the constructor of the parent class
        self.department = department                  # Store the teacher's department
        print("Teacher class worked.")                # Print message when object is created

    def info(self):
        # Display specific information about the teacher
        print(f"{self.name} {self.surname} is a {self.department} teacher, {self.age} years old, with a salary of {self.salary} TL.")
    
    def increase(self):
        # Increase salary by 50% and return the new salary
        return self.salary * 1.5


# Define a subclass 'manager' that inherits from 'school'
class manager(school):
    def __init__(self, name, surname, age, salary, unit):
        super().__init__(name, surname, age, salary)  # Call the parent constructor first
        self.unit = unit                              # Store the manager's unit name
        print("Manager class worked.")                # Print message when object is created
    
    def info(self):
        # Display information about the manager
        print(f"{self.name} {self.surname} is {self.age} years old and works in the {self.unit} unit with a salary of {self.salary} TL.")

    def increase(self):
        # Increase salary by 40% and return the new salary
        return self.salary * 1.4


# Define a subclass 'attendant' that inherits from 'school'
class attendant(school):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age, salary)  # Use the constructor of 'school'
        print("Attendant class worked.")              # Print message when object is created

    def info(self):
        # Display information about the attendant
        print(f"{self.name} {self.surname} is an attendant, {self.age} years old, with a salary of {self.salary} TL.")
    
    def increase(self):
        # Double the salary and return it
        return self.salary * 2


# --- Object Creation and Method Calls ---

# Create an attendant object named 'sinan'
sinan = attendant("Sinan", "KARABACAK", 22, 8000)
sinan.info()                # Call the info() method for 'sinan'
print(sinan.increase())     # Print the increased salary

# Create a teacher object named 'ahmet'
ahmet = teacher("Ahmet", "YILMAZ", 54, 10000, "Physics")
ahmet.info()                # Call the info() method for 'ahmet'
print(ahmet.increase())     # Print the increased salary

# Create a manager object named 'mehmet'
mehmet = manager("Mehmet", "SABAN", 49, 12000, "Assistant Manager")
mehmet.info()               # Call the info() method for 'mehmet'
print(mehmet.increase())    # Print the increased salary
