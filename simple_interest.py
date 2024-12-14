def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest.
    
    Formula:
        Simple Interest = (Principal * Rate * Time) / 100

    Args:
        principal (float): The principal amount (must be greater than 0).
        rate (float): The annual interest rate in percentage (must be greater than 0).
        time (float): The time in years (must be greater than 0).

    Returns:
        float: The calculated simple interest.
    """
    if principal <= 0 or rate <= 0 or time <= 0:
        raise ValueError("Principal, rate, and time must all be greater than zero.")
    
    return (principal * rate * time) / 100


def main():
    print("Welcome to the Simple Interest Calculator!")
    
    try:
        # Take input from the user
        principal = float(input("Enter the principal amount (in your currency): "))
        rate = float(input("Enter the annual interest rate (in %): "))
        time = float(input("Enter the time (in years): "))

        # Calculate simple interest
        simple_interest = calculate_simple_interest(principal, rate, time)

        # Display the result
        print(f"\nSimple Interest Details:")
        print(f"Principal Amount: {principal}")
        print(f"Annual Interest Rate: {rate}%")
        print(f"Time Duration: {time} years")
        print(f"Calculated Simple Interest: {simple_interest}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
