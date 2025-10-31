# задание 2 

n = int(input("Введите кол-во чисел для первой строчки - ").strip())
list1 = set()
for i in range(n):
    num = int(input("Введите число - ").strip())
    list1.add(num)

m = int(input("Введите кол-во чисел для второй строчки - ").strip())  
list2 = set()
for i in range(m):
    num = int(input("Введите число - ").strip())
    list2.add(num)
numbers = list1 & list2

print("Кол-во общих чисел в двух строках -", len(numbers))
