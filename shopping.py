#   Ask user for input on three products names
product1 = input("Please enter the first product: ")
product2 = input("Please enter the second product: ")
product3 = input("Please enter the third product: ")

#   Ask user for input on the prices (float with two decimals) for each product
product1Price = float(input("Please give a price for product 1: "))
product2Price = float(input("Please give a price for product 2: "))
product3Price = float(input("Please give a price for product 3: "))

#   Round the product prices input to two decimal values
product1Price = round(product1Price,2)
product2Price = round(product2Price,2)
product3Price = round(product3Price,2)

#   Calculate the total of all products
productsTotal = product1Price + product2Price + product3Price

#   Calculate the average of all products and round to two decimal places
productsAverage = round(((productsTotal)/3),2)

#   print out the sentence
print(f"The Total of {product1}, {product2}, {product3} is R{productsTotal} and the average price of the items are R{productsAverage}")