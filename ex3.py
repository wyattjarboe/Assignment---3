def get_customer_age():
    """
    Loop until the user enters a valid positive integer age.
    Also demonstrates handling a NameError (simulated) once.
    """
    # Simulate a NameError (e.g., referencing a variable that isn't defined yet)
    try:
        _ = not_defined_yet  # noqa: F821  (deliberate to trigger NameError)
    except NameError:
        print("(Note) Caught a NameError for an undefined variable. Continuing...\n")

    while True:
        raw = input("Enter customer age (integer): ").strip()
        try:
            age = int(raw)
            if age <= 0:
                print("Age must be a positive integer. Try again.")
                continue
            return age
        except ValueError:
            print(f"Invalid age: '{raw}'. Please enter a whole number.")

def main():
    print("=== Age Verification ===")
    age = get_customer_age()
    if age >= 18:
        print("Eligible: Customer meets the age requirement (18+).")
    else:
        print("Not eligible: Customer must be at least 18.")

if __name__ == "__main__":
    main()