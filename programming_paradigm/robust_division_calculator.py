def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        dem = float(denominator)
        result = num / dem
        return f"Result: {result: 2f}"
    except ZeroDivisionError:
        return "Error Cannot divide by zero"
    except ValueError:
        return "Error: Both numerator and denomirator must be numeric value"
