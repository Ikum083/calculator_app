# calculator app using inheritance
## create parent classes
### parent class for addition
class Addition:
#### main method ask for 2 arguments and adds them
    def add_num(self, num1, num2):
        return num1 + num2

### parent class for subtraction
class Subtraction:
#### main method ask for 2 arguments and subtracts them
    def sub_num(self, num1, num2):
        return num1 - num2

### parent class  for multiplication
class Multiplication:
#### main method ask for 2 arguments and multiplies them
    def multi_num(self, num1, num2):
        return num1 * num2

### parent class for division
class Division:
#### main method ask for 2 arguments and divides them
    def  div_num(self, num1, num2):
        return num1 / num2

### child class to handle user input
class MainMenu(Addition, Subtraction, Multiplication, Division):
    def calculator_menu(self):
        try:
            first_num = input(int("Enter first number: "))
            second_num = input(int("Enter second number: "))
            operation = input("Enter operation to be used(add, subtract, multiply, divide): ").lower()
#### user input to ask for 2 numbers

#### user input to ask for operation to be used
#### returns answer

### call child class