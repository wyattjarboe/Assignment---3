def get_float(prompt: str):
    """Prompt until a valid float is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"Invalid number: '{raw}'. Try again.")

def validate_percentage(pct: float):
    """
    Validate that percentage is between 0 and 100 (inclusive).
    You can allow negatives if you want to simulate pay cuts;
    here we enforce 0–100 as requested.
    """
    if pct < 0:
        # Example of a manual (built-in) exception raise for bad input
        raise ValueError("Percentage cannot be negative.")
    if pct > 100:
        raise ValueError("Percentage cannot exceed 100.")

def main():
    print("=== Salary Adjustment Simulator ===")
    while True:
        try:
            current_salary = get_float("Enter current salary (float): ")
            pct = get_float("Enter adjustment percentage (0–100): ")
            validate_percentage(pct)

            new_salary = current_salary * (1 + pct / 100.0)
            print(f"New salary after {pct:.2f}% adjustment: ${new_salary:,.2f}")
            break
        except ValueError as e:
            print(f"Input error: {e}. Please try again.\n")

if __name__ == "__main__":
    main()