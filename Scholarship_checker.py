# for a schlarship, grade needs to be higher than 4.5 and atttendence more tha 80-%

names = ["Anna", "Tom", "Maja"]
grades = [4.8, 4.2, 5.0]
attendance = [90, 95, 70]

for i in range(len(names)):
    if grades[i] > 4.5 and attendance[i] > 80:
        print(f"{names[i]} got a scholarship")
