def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    else:
        raise ValueError("invalid operation")
try:
    num1= float(input("enter the first number:"))
    num2 = float(input("enter the second number:"))
    operator = input("enter an operator (+,-,*,/):")
    result = calculate(num1,num2,operator)
    print(f"the result of {num1}{operator}{num2} is: {result}")
except ValueError as e:
    print(f"invalid input {e}")
except ZeroDivisionError:
    print("cannot divide by zero")
except Exception as e:
    print(f"unexpected error ocurred: {e}")
finally:
    print("end of the program")