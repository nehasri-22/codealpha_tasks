# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3400,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("📈 Simple Stock Tracker")
print("Available stocks:", list(stock_prices.keys()))

# Input loop
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\n📊 Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock} -> {quantity} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value = ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock} -> {quantity} × ${price} = ${value}\n")
        file.write(f"\nTotal Investment = ${total_investment}")
    
    print("✅ Portfolio saved to 'portfolio.txt'")