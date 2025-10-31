#задание 3

numbers = list(map(int, input("Введите числа через пробел - ").split()))
seen = set()
result = []

for num in numbers:
    if num in seen:
        result.append(f"{num} - YES")
    else:
        result.append(f"{num} - NO")
        seen.add(num)

print("Результат:")
for res in result:
    print(res)
