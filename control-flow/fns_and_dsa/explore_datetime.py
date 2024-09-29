from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted date and time
    print(f"Current date and time: {formatted_date}")
    
# Part 2: Calculate a Future Date
def calculate_future_date(days):
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date by adding the timedelta (days) to the current date
    future_date = current_date + timedelta(days=days)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print(f"Future date: {formatted_future_date}")

def main():
    # Call the function to display current date and time
    display_current_datetime()
    
    # Prompt the user to enter the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Call the function to calculate and display the future date
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
