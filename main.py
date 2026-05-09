# Task 1 - Make a program that asks for names. If the name is on our VIP list, they get in. If not, they are rejected. We will use a loop so the program keeps running until we type “exit”

vip_names = ["Wojtek" , "Norbert" , "Kalina" , "Maja"]

while True:
    name = input("What is your name? ")

    if name.lower() == "exit":
        print("Goodbye!")
        break

    if name in vip_names:
        print(f"Welcome to VIP, {name}")
    else:
        print("Acces denied")
