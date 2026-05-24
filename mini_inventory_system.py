# Create a program that:
# asks the user to enter product names
# stops when user types "done"
# stores counts of products using a dictionary
#
# At the end print:
# all products
# how many times each was entered
# the most entered product

products = {}

while True:
    product = input("Your product: ")

    if product.lower() == "done":
        break

    product = product.lower().strip()

    if product not in products:
        products[product] = 1
    else:
        products[product] += 1

for product in products:
    print(product, "->", products[product])

most_entered_key = max(products, key=products.get)
print("Count: ", products[most_entered_key])
print(f"The most entered product: ", most_entered_key)