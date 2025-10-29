def get_valid_number(prompt: str, cast_type):
    while True:
        raw = input(prompt).strip()
        try:
            value = cast_type(raw)
            return value
        except ValueError:
            print(f"Invalid input: '{raw}'. Please enter a valid {cast_type.__name__}.")


def main():
    print("=== Sales Data Entry ===")
    units = get_valid_number("Enter number of units sold (integer): ", int)
    price = get_valid_number("Enter price per unit (float): ", float)
    total_revenue = units * price
    print(f"Total revenue = {units} * {price:.2f} = ${total_revenue:,.2f}")

if __name__ == "__main__":
    main()
    