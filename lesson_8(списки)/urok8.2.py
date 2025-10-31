# задание 2
n = int(input("Введите кол-во чисел (не меньше 4) - "))
arr = list(map(int, input(f"Введите {n} чисел через пробел - ").split()))

result = [arr[-1]] + arr[:-1]
print("Результат -", *result)
