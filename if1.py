"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
getAge = int(input('Введите ваш возраст? '))

def main(x):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if x <= 2:
        print("Ваш возраст не должен быть меньше 2")
    elif 2 < x < 7:
        occupation = 'Вы ходите в детский сад'
        print(occupation)
    elif 7 < x < 18:
        occupation = 'Вы учитесь в школе'
        print(occupation)
    elif 18 < x < 22:
        occupation = 'Вы учитесь в университете'
        print(occupation)
    else:
        occupation = 'Вы работаете'
        print(occupation)

if __name__ == "__main__":
    main(getAge)
