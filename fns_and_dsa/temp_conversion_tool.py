# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Global counter for tracking conversions
conversion_count = 0

def convert_to_celsius(fahrenheit):
    # No need to use 'global' here since we are only reading the variable
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # No need to use 'global' here since we are only reading the variable
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def increment_conversion_count():
    global conversion_count  # Modifying the global counter
    conversion_count += 1

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return  # Exit if invalid input

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
        increment_conversion_count()
    elif unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
        increment_conversion_count()
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return

    print(f"Conversions performed: {conversion_count}")

if __name__ == "__main__":
    main()
