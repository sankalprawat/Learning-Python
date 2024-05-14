try:
    num_str = input("Enter a number: ")
    num = int(num_str)  # Potential ValueError
    result = num / 0  # Potential ZeroDivisionError

except (ValueError, ZeroDivisionError) as error:  # Catching multiple exceptions
    error_message = {
        ValueError: "Error: Invalid input. Please enter a number.",
        ZeroDivisionError: "Error: Cannot divide by zero."
    }

    print(error_message.get(type(error), "An unexpected error occurred."))
