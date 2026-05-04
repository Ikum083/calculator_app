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
        pass

if __name__ == "__main__":
    # call child clas
    calc_app = MainMenu()
# boolean to control while loop
    calculating = True
while calculating:
# user input to ask for 2 numbers
    try: 
        first_num = int(input("Enter first number: "))
        second_num = int(input("Enter second number: "))
    # user input to ask for operation to be used
        operation = input("Enter operation to be used(add, subtract, multiply, divide): ").lower()
    # conditional to return answer depending on operation
        if operation == "add":
            answer = calc_app.add_num(first_num, second_num)
        elif operation == "subtract":
            answer = calc_app.sub_num(first_num, second_num)
        elif operation == "multiply":
            answer = calc_app.multi_num(first_num, second_num)
        elif operation == "divide":
            answer = calc_app.div_num(first_num, second_num)
        else:
            print("Operation not available")
        # returns answer
        print(answer)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("Invalid Value")

    # ask user if they want to continue
    ask_user = input("Continue or exit program?(y/n): ").lower()
    if ask_user == 'n':
        calculating = False