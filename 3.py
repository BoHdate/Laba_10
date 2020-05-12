"""
3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.

Олійник Богдан Сергійович 122\Д
"""
from random import randint
from timeit import timeit

def it(a):                  #Ітерація 
    for i in range(len(a)):
        if a[i] == max(a):
            return i
def rc(a): 
    if len(a) == 2:
        return a[1] if a[1] > a[0] else a[0]
    else:
        return rc([a[0], rc(a[1:])])
a = [randint(1, 5) ** 2 for x in range(10)]
print(a)
res = input('Настисніть r щоб обрати рекурсію, i - ітерацію: ')
if res == 'r':
    print(a.index(rc(a)))
elif res == 'i':
    print(it(a))
j = timeit('"-".join(str(n) for n in range(100))', number = 10000)
print(j)
