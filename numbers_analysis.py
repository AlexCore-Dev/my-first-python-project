# Learning user input and for loops in Python - 2025.03.22.

num1 = []

for num in range(5):
    numbers = int(input(f'Add meg a(z) {num + 1} szamot: '))
    num1.append(numbers)
print('Az altalad megadott szamok:', num1)

# Calculate the sum, average, smallest and largest numbers

osszeg = sum(num1)
atlag = sum(num1) / len(num1)
legk = min(num1)
legn = max(num1)

print(f'A szamok osszege {osszeg}, az atlaga {atlag}. A legkissebb szam a(z) {legk}, a legnagyobb {legn}.')

# Count how many numbers are greater than 10

db = 0
for szam in num1:
    if szam > 10:
        db += 1

# Percentage of numbers greater than 10

ossz = len(num1)
szazalek = (db / ossz) * 100


print(f'A listaban {db} elem nagyobb 10-nel, ami a lista {szazalek:.2f}%-at teszi ki.')

# Separating even and odd numbers from the list

paros = []
for par in num1:
    if par % 2 == 0:
        paros.append(par)
print(f'Az lista kovetkezo elemei parosak: {paros}, a lista tobbi eleme paratlan!')