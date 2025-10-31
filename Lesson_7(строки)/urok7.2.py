def compress_spaces(input_string):  
    # Разбиваем строку по пробелам и соединяем через один пробел  
    return ' '.join(input_string.split())  
  
# Пример использования  
input_str = "Это   пример    строки   с    множеством   пробелов"  
result = compress_spaces(input_str)  
print(f"Исходная строка: '{input_str}'")  
print(f"Результат: '{result}'")  
