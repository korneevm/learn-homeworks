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

def check_string(str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            return 0
        elif str1 == str2:
            return 1
        elif str1 != str2:
            if len(str1) > len(str2):
                return 2
            elif str2 == 'learn':
                return 3

if __name__ == '__main__':
        str1 = 'lol'
        str2 =  1
        print(check_string(str1, str2))
        str1 = 'lol'
        str2 = 'lol'
        print(check_string(str1, str2))
        str1 = 'lolll'
        str2 = 'lol'
        print(check_string(str1, str2))
        str1 = 'lol'
        str2 = 'learn'
        print(check_string(str1, str2))
        str1 = 'lol'
        str2 = 'lldldl'
        print(check_string(str1, str2))
        #как обрабатывать исключения?

