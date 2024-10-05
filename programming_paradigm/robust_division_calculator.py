
def safe_divide(numerator, denominator):
   
    try:
         numerator = float(input("enter the first number : "))
         denominator = float(input("enter the second number : "))

         result = numerator/denominator
         return f"The result of the division is {result}"
    except ZeroDivisionError:
         return "Error: Cannot divide by zero."
    except ValueError:
         return "Error: Please enter numeric values only."

    

