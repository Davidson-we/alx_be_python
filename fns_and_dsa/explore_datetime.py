from datetime import datetime, timedelta

# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # save current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days)  # calculate future date
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")


def main():
    # Show the current date and time
    current_date = display_current_datetime()

    # Calculate future date based on user input
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
