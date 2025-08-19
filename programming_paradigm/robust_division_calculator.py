class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


def safe_divide(numerator, denominator):
    calc = Calculator()
    try:
        num = float(numerator)
        den = float(denominator)
        result = calc.divide(num, den)   # Delegate actual math
        return f"Result: {result:.2f}"
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except ValueError:
        return "Error: Both numerator and denominator must be numeric values"
