# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount)

# Print result
if final_price < original_price:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Original price remains: {original_price}")
