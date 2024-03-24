price = int(input('Enter the price: '))
discount_percent = int(input('Enter the discount percent: '))
def calculate_discount(price, discount_percent):
    final_price = price*(100-discount_percent)*0.01
    return final_price


print('Your discounted price is: ')
print(calculate_discount(price, discount_percent))