def is_palindrome(s):  
    # Сравниваем строку с её обратной версией  
    if s == s[::-1]:  
        return "yes"  
    else:  
        return "no"  
  
# Пример использования:  
polindrom = input("введите строчку: шалаш") 
print(is_palindrome(polindrom))  
  
