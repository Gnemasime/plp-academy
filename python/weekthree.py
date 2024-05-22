def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price == original_price:
        print(f"No discount applied. Original price: ${original_price:.2f}")
    else:
        print(f"Final price after applying {discount_percent}% discount: ${final_price:.2f}")

except ValueError:
    print("Error: Please enter valid numerical values for price and discount percentage.")
