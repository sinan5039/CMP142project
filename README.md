# WHY WOULD YOU USE GenAI SYSTEMS GENERATE EVERYTHING FROM START TO FINISH??? HIGHLY UNACCEPTEBLE.  
# WHAT IS YOUR NAME AND STUDENT ID? 
# Python OOP - School Management System

This project was prepared for the [Course Name] course to demonstrate the principles of Object-Oriented Programming (OOP).

## Project Structure

The project consists of `teacher`, `manager`, and `attendant` subclasses that inherit from a main `school` (Staff) base class.

* **`school` (Base Class):** Holds the common attributes for all staff (name, surname, age, salary).
* **`teacher` (Subclass):** Inherits from the `school` class and additionally holds `department` information.
* **`manager` (Subclass):** Inherits from the `school` class and additionally holds `unit` information.
* **`attendant` (Subclass):** Inherits from the `school` class.

## OOP Concepts Demonstrated

* **Inheritance:** All subclasses call the base class's `__init__` method using `super()`.

* **Polymorphism:** The `info()` and `increase()` methods are redefined in each subclass (Method Overriding) to meet the specific needs of that class.
