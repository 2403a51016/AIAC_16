# Power Bill Calculator

def calculate_bill(units):
    # Example slab rates (customize as needed)
    if units <= 100:
        rate = 5
    elif units <= 200:
        rate = 7
    else:
        rate = 10
    return units * rate

def main():
    try:
        prev_bill = float(input("Enter previous month's bill amount (₹): "))
        units_used = int(input("Enter units used this month: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    current_bill = calculate_bill(units_used)
    total_bill = prev_bill + current_bill

    print("\nPower Bill Summary")
    print("-" * 40)
    print(f"{'Description':<25}{'Amount (₹)':>15}")
    print("-" * 40)
    print(f"{'Previous Month Bill':<25}{prev_bill:>15.2f}")
    print(f"{'Current Month Bill':<25}{current_bill:>15.2f}")
    print("-" * 40)
    print(f"{'Total Bill':<25}{total_bill:>15.2f}")
    print("-" * 40)

if __name__ == "__main__":
    main()