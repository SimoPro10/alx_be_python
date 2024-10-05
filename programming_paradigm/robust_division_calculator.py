
def safe_divide(numerator, denominator):
    numerator = float(input("enter the first number : "))
    denominator = float(input("enter the second number : "))
    try:

        result = numerator/denominator
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("wrong input,enter a number !")

    else:
        return result