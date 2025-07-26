from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    format = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted: ", format)


def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.date.today() + datetime.timedelta(days=days_to_add)
        print("Future date: ", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer value for days.")

    

display_current_datetime()
calculate_future_date()