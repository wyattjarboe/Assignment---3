def get_valid_int(prompt):
    """Prompt until a valid integer is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print(f"Invalid integer: '{raw}'. Please try again.")

def main():
    print("=== Inventory Quantity Checker ===")
    while True:
        # define variables inside the loop
        inventory = get_valid_int("Enter current inventory level (int): ")
        threshold = get_valid_int("Enter minimum reorder threshold (int): ")

        # compare inventory and threshold
        if inventory < threshold:
            print("Reorder alert: Inventory is below threshold!")

        # compute percentage safely
        try:
            percent = (inventory / threshold) * 100
        except ZeroDivisionError:
            print("Cannot compute percentage because threshold is zero. Please re-enter values.\n")
            continue  # restart the loop if zero

        print(f"Inventory is {percent:.2f}% of the threshold.")
        break  # exit successfully

if __name__ == "__main__":
    main()
    



         