cities = [" Warsaw", "gdansk ", " WroCLAW", "kraków", " POZNAN "]

cleaned = []

for city in cities:
    cleaned.append(city.strip().lower())

print(cleaned)