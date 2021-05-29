"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

a = str(input())
b = str(input())

def main(a, b):
    if type(a) == str and type(b) == str:
        if a == b and b != 'learn':
            return '1'
        if len(a) > len(b) and b != 'learn':
            return '2'
        if a != b and b == 'learn':
            return '3'
        else:
            return 'Такого условия я не знаю'
    else:
        return '0'
    
if __name__ == "__main__":
    main(a, b)

print(main(a, b))
