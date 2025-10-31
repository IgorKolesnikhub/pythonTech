# задание 3

m = int(input("Введите массу лодки - ")) 
n = int(input("Введите кол-во рыбаков - "))  
weights = [int(input("Введите массу рыбаков - ")) for _ in range(n)]

weights.sort()

i, j = 0, n - 1
boats = 0

while i <= j:
    if weights[i] + weights[j] <= m:
        i += 1   # лёгкий сел с тяжёлым
    j -= 1       # тяжёлый уплывает
    boats += 1
print(f'Кол-во лодок которые понадобятся: {boats}')
