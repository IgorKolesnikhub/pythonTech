#Задание 1
pets = {}

#Вводим данные о питомце
name = input("Введите имя питомца: ")
species = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

#Поправляем грамматику
if age % 10 == 1 and age % 100 != 11:
    vozrast = "год"
elif age % 10 in [2, 3, 4] and not (age % 100 in [12, 13, 14]):
    vozrast = "года"
else:
    vozrast = "лет"
    
#Создаем внутренний словарь с информацией о питомце
pet_info = {
    'Вид питомца': species,
    'Возраст питомца': f"{age}, {vozrast}",
    'Имя владельца': owner
}

#Добавляем в основной словарь pets
pets[name] = pet_info

#Результат для проверки
print("Созданный словарь pets:")
print(pets)
