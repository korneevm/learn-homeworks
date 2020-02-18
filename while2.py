"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
question = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", 'Как погода?': 'Солнечно!'}


def ask_user_dict():
    # не учитываем регистр вопроса
    raw_user_say = input('Введите вопрос: ')
    user_say = raw_user_say.capitalize()
    if user_say in question:
        print(question[user_say])


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        ask_user_dict()


if __name__ == "__main__":
    ask_user()
