" Global Conversion Factors"

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_TO_FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_OFFSET

def main():
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Is this temperature in (C)elsius or (F)ahrenheit? ").strip().upper()

        match unit:
            case 'C':
                converted_temp = convert_to_fahrenheit(temp)
                print(f"{temp:.2f}°C is equal to {converted_temp:.2f}°F")
            case 'F':
                converted_temp = convert_to_celsius(temp)
                print(f"{temp:.2f}°F is equal to {converted_temp:.2f}°C")
            case _:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()