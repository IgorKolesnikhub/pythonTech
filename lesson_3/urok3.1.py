pet = input("Введите вид питомца: ") 
name = input("Введите кличку животного: ")
age = int(input("Введите возраст питомца: "))

k = age % 10

if (age > 9) and (age < 20) or (age > 110)or(k > 4) or (k == 0):
    print(f'Это {pet} по кличке {name}. Возраст: {age} лет')
else:
    if k==1: 
        print(f'Это {pet} по кличке {name}. Возраст: {age} год')
    else: 
        print(f'Это {pet} по кличке {name}. Возраст: {age} года ')


