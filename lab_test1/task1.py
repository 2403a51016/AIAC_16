def currency_converter():
    # Example exchange rates (base: USD)
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.92,
        'INR': 83.0,
        'GBP': 0.78,
        'JPY': 157.0
    }

    print("Available currencies:", ', '.join(exchange_rates.keys()))
    from_currency = input("Enter the currency you have (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Currency not supported.")
        return None

    # Convert to USD first, then to target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]

    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    return converted_amount

# Example usage:
currency_converter()