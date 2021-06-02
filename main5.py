line1 = input("Введите первый список слов через запятую: ")
first_list = line1.split(',')
print("Количество слов в первом списке:",
      line1.count(" ") + 1)

line2 = input(f"Введите второй список из "
              f"{line1.count(' ') + 1} "
              f"слов через запятую: ")
second_list = line2.split(',')
d = dict(zip(first_list, second_list))
print(d)
