"""
2. Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.

ОлійникБогдан Сергійович 122\Д
"""
from timeit import timeit
def Resumma(x):                                 #Складаємо так всі цифри заданого числа
    if x < 10:                                   #поки воно не стане однозначним
        return x
    else:
        return x % 10 + Resumma(x // 10)

def Reroot(x):
    if x < 10:
        return x
    else:
        return Recroot((RecSumma(x)))

def Itsumma(x):
    a = 0
    for i in range(x):
        a += x % 10
        x //= 10
    return a

def Itroot(x):
    while x > 9:
        i = int(x % 10)
        x = x // 10
        x = x + i
    return x

x = int(input('Введіть число: '))
choice = input('Настисніть r щоб обрати рекурсію, i - ітерацію: ')
if choice == 'r':
    print(x, Resumma(x), Reroot(x))
elif choice == 'i':
    print(x, Itsumma(x), Itroot(x))
j = timeit('"-".join(str(n) for n in range(100))', number=10000)
print(j)
