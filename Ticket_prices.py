# Create a program that:
#
# stores movie visitor ages in a list
# checks ticket price based on age:
#
# Rules:
#
# under 12 → ticket costs 10 zł
# from 12 to 17 → ticket costs 15 zł
# 18 and above → ticket costs 25 zł
#
# The program should:
#
# print each person's ticket price
# calculate total money earned
#
# example:
# ages = [8, 15, 22, 10, 35]
# expected output:
# Person age 8 pays 10 zł
# Person age 15 pays 15 zł
# Person age 22 pays 25 zł
# ...
#
# Total earned: 85 zł

ages = [8, 15, 22, 10, 35]
total = 0
children = 0
teenagers = 0
adults = 0

for age in ages:
    if age < 12:
        price = 10
        children += 1
        total += 10

    elif age >= 12 and age < 18:
        price = 15
        teenagers += 1
        total += 15

    else:
        price = 25
        adults += 1
        total += 25

    print(f"Person age {age} pays {price}")

print(total)
print(children)
print(teenagers)
print(adults)