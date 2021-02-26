string = input("Введите строку")
a = 0

for i in range(0, len(string)):
    if string[i] == "с":
        a = a + 1
    if i == 2:
        continue
    print(string[i])


if a > 0:
    print("В строке есть буква 'с'")

print("Длина строки:", len(string))

for i in range(0, len(string)):
    if i == len(string) - 1:
        continue
    print(string[i])