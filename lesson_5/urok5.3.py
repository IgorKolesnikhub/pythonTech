#задани 3 

summa_startap = int(input("Сумма инвестиций: "))
Mike = int(input("Сумма у Майкла: "))
Ivan = int(input("Сумма у Ивана: "))


if (Mike >= summa_startap) and (Ivan >= summa_startap):
    print("2")
elif (Mike >= summa_startap) and (Ivan <= summa_startap):
    print("Mike")
elif (Mike <= summa_startap) and (Ivan >= summa_startap):
    print("Ivan")
elif (Mike <= summa_startap and Ivan <= summa_startap and Mike + Ivan >= summa_startap):
    print("1")
else:
    print("0")
