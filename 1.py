"""
1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.

Олійник Богдан Сергійович 122\Д
"""
from timeit import timeit       #Імпортуєм timeit
def rec(x):                     #Pекурсія
    if x == 0:
        return 1
    else:
        return x * rec(x - 1)

def it(x):                      #Iтерація
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a
choice = input('Настисніть r щоб обрати рекурсію, i - ітерацію: ')
x = int(input('Введіть число: '))
if choice == 'r':
    print(x, rec(x))
elif choice == 'i':
    print(x, it(x))
j = timeit('"-".join(str(n) for n in range(100))', number = 10000)
print(j)
