lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

stylish_setee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

sales_tax = 0.88

customer_one_total = 0
customer_one_itemization = ""

#The transaction begins
customer_one_total += lovely_loveseat_price
print("Customer One Total: " + str(customer_one_total))

customer_one_itemization += lovely_loveseat_description
print("Customer One Itemization: " + str (customer_one_itemization))

customer_one_total += luxurious_lamp_price
print("Customer One Total: " + str(customer_one_total))

customer_one_itemization += luxurious_lamp_description
print("Customer One Itemization: " + str (customer_one_itemization))

customer_one_tax = customer_one_total * sales_tax
print("Sales Tax: " + str(sales_tax))
print()

customer_one_total += customer_one_tax

print("Customer One Items: ")
print(customer_one_itemization)
print()
print("Customer One Total: ")
print(customer_one_total)