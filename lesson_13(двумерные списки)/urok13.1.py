import random

# Запросим размер матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Генерация первой матрицы
matrix1 = []
for i in range(rows):            
    row = []
    for j in range(cols):         
        row.append(random.randint(1, 9))
    matrix1.append(row)

# Генерация второй матрицы
matrix2 = []
for i in range(rows):             
    row = []
    for j in range(cols):         
        row.append(random.randint(1, 9))
    matrix2.append(row)

# Сложение матриц
result = []                  
for i in range(rows):          
    row = []                  
    for j in range(cols):         
        row.append(matrix1[i][j] + matrix2[i][j])  
    result.append(row)            

# Для красоты :)
def print_matrix(matrix, title):
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{x:3}" for x in row))

print_matrix(matrix1, "Матрица 1")
print_matrix(matrix2, "Матрица 2")
print_matrix(result, "Результат сложения")
