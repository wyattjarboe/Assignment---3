def main():
    print("=== Profit Margin Ratio Calculator ===")
    while True:
        try:
            profit_str = input("Enter profit (float): ").strip()
            revenue_str = input("Enter revenue (float): ").strip()

            profit = float(profit_str)
            revenue = float(revenue_str)

            ratio = profit / revenue  # may raise ZeroDivisionError
        except ValueError:
            # Silent reprompt on minor errors per instructions
            pass
        except ZeroDivisionError:
            # Silent reprompt if revenue is zero
            pass
        else:
            # Only runs if no exceptions occurred
            print(f"Profit margin = {ratio * 100:.2f}%")
            break  # Exit after a successful calculation

if __name__ == "__main__":
    main()