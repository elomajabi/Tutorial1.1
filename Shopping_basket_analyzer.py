from numpy.ma.extras import average

products = []
while True:
    x = input("Input price: ")

    if x.lower == "exit":
        break

    products.append(x)

print(products)
print(sum(products))
print(sum(products)/len(products))
print(max(products))
print(min(products))

counter = 0

for i in range(len(products)):
    if products[i] >  sum(products)/len(products):
        counter += 1

print(counter)
