#Задание 3

a = int(input("Введите А - "))
b = int(input("Введите В - "))

for i in range(a + (a + 1) % 2, b + b % 2, 2):
    print(i, end=' ')
