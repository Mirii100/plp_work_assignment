def calculate_discount(price, discount):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, the discount is applied.
    Otherwise, the original price is returned.
    """

  if num.isdigit():
       
    if discount >= 20:
        discount_amount = (discount / 100) * price
        return price - discount_amount

    else :
      print('the input is  not a  number ')
    return price

# Prompt user for input
price = float(input("Enter the original price:   "))
discount_percent = float(input("Enter the discount percentage:  do not indicate the % sign    " ))

final_price = calculate_discount(price, discount_percent)

print(f"Final price after discount: ${final_price:.2f}")
