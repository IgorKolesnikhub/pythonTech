# задание 1

n = int(input("Введите кол-во чисел - "))                          
nums = set(map(int, input("Введите числа через пробел - ").split()))    
print("Кол-во уничкальных чисел -", len(set(nums)))                    
