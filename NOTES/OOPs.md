# Intro:

Python supports different programming approach.

You can create Objects, hence like C++, it is also a Object-Oriended Programming language. (OOP)

Every object has two characteristics:
- attributes
- behaviour

## Concepts of OOP follow some basic principles:
Concept | Explanation
-----|----
Inheritance    |A process of using details from a new class without modifying existing class.
Encapsulation|Hiding the private details of a class from other objects.
Polymorphism|A concept of using common operation in different ways for different data input.



### Class:

Class is like a definition/blue print of an object.
Class can be used for basic attribute definition.


```Python
class Employee(object):
    def __init__(self,f_name,l_name,dept):
        self.first_name = f_name
        self.last_name = l_name
        self.department = dept
        self.email = self.first_name + self.last_name + self.department + '@company_name.com'
        
```
### Object:

Object is an instance of the class.

```Python
new_employee = Employee('John','Gonzales','Accounts')
```
This will automatically create a new instance of Employee class which has attributes:
-   first_name
-   last_name
-   email
-   department
-   date_of_join

### Methods:

Methods are functions defined inside a class. They are used to define the behaviours of an object.

```Python
class Employee(object):
    def __init__(self,f_name,l_name,dept):
        self.first_name = f_name
        self.last_name = l_name
        self.department = dept
        self.email = self.first_name + self.last_name + self.department + '@company_name.com'
        

    def __add_increment(rating):
        if rating == 'A':
            self.salary = self.salary + (self.salary * 10)/100
        elif rating == 'B':
            self.salary = self.salary + (self.salary * 7)/100
        elif rating == 'C':
            self.salary = self.salary + (self.salary * 4)/100
```

Here in the above example you can see, we have create a method "add_increment", which will take ratings and accordingly, will update the salary.

### Inheritance:

Inheritance is a way of create a new class from existing class which will have all attributes of the existing class and will some extra of its own.


```Python
class Employee(object):
    def __init__(self,f_name,l_name,dept):
        self.first_name = f_name
        self.last_name = l_name
        self.department = dept
        self.email = self.first_name + self.last_name + self.department + '@company_name.com'
        self.date_of_join = datetime.datetime.date()
        self.employee_id = '1001'

class John(Employee):
    def __init__(self):
        self.employee_id = 1001
        self.salary = 25000    
```

Here you can see, we have created a new class John, which will inhereit basic attributes from class Employee.

Whatever extra attributes we wanted John to have are added in his own class definition, like his "Employee ID" and "Salary".

And due to inheritance of methods from the Parent class, Employee, we can simply use, "add_increment" on John as well.

### Encapsulation:

Encapsulation is a method to restrict access to certain attributes, values. This is to prevent direct modification of values, that is why the name "Encapsulation".

In the previous metioned examples, "add_increment", we dont want anyone to change the values of % like:
-   A = 10%
-   B = 7%
-   C = 4%

Usually, the private attributes are denoted by using double '_', or _dunders_ ( two times _ )


### Polymorphism:
Polymorphism is ability to use common interface for multiple from.

```Python
class Rectangle:
    def info(self):
        print('I am rectangle shaped!')
    
class Circle:    
    def info(self):
        print('I am circle shaped!')

r = Rectangle()
c = Circle()

def check_info(shape):
    shape.info()
    
print(check_info(r))
print(check_info(c))
```
Here we used common attribute from both classes, info(), to create a new method, check_info(), where we passed different objects (r,c) to get info, from each individual class.

This is Polymorphism.