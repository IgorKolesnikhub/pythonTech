#задание 2

word = input("Введите слово: ").lower()

a = word.count('a')
e = word.count('e')
i = word.count('i')
u = word.count('u')
o = word.count('o')

if a == 0:
        print( "a отсутствует в слове: ", False)
if e == 0:
        print( "e отсутствует в слове: ", False)
if i == 0:
        print( "i отсутствует в слове: ", False)
if u == 0:
        print( "u отсутствует в слове: ", False)
else:
        print( "o отсутствует в слове: ", False)
        
print(f"буква a {a}",
      f"буква e {e}", 
      f"буква i {i}",
      f"буква u {u}",
      f"буква o {o}", sep="\n")         
print(f"Гласных: {a + e + i + o + u}") 
print(f"Согласных: {len(word) - (a + e + i + o + u)}") 
