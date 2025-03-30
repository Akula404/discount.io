# Question 1
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    return price

# Question 2
try:
    price = float(input("Enter the original price of the item:"))
    discount_percent = float(input("Enter the discount percentage:"))

    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after discount: Ksh{final_price:2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
    
