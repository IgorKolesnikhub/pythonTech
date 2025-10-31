#Задание 1

n = int(input("Введите количество чисел "))
count = 0
for i in range(n):
    pup = int(input("Введите число "))
    if pup == 0:
        count = count + 1 
print("Количество нулей ", count)
