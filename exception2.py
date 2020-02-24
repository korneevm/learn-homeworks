"""

Домашнее задание №1

Исключения: приведение типов

* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало
    
"""



def get_summ(num_one, num_two):
    try:
        result = int(num_one) + int(num_two)
        print(result)
    except(ValueError):
        print("Не получилось привести к целому числу")

if __name__ == "__main__":

        print(get_summ(2, 2))
        print(get_summ(3, "3"))
        print(get_summ("4", "4"))
        print(get_summ("five", 5))
        print(get_summ("six", "шесть"))
