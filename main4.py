a = input()
b = input()
c = input()
print(a.lower())
print(b.lower())
print(c.lower())

print(a.upper())
print(b.upper())
print(c.upper())

print(a.capitalize())
print(b.capitalize())
print(c.capitalize())

x = input()
y = input()
z = input()

text1 = 'Овощ: {}. Количество: {}'
print(text1.format(a.capitalize(),x))
text1 = 'Овощ: {}. Количество: {}'
print(text1.format(b.capitalize(),y))
text1 = 'Овощ: {}. Количество: {}'
print(text1.format(c.capitalize(),z))