from random import randint

"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела?": ["Хорошо!", "Нормально!", "Отлично!", "Пойдет!"],
                         "Что делаешь?": ["Программирую", "Отдыхаю", "Гуляю", "Пью кофе"],
                         "Что такое while?": ["Это один из самых универсальных циклов в Python, "
                                              "поэтому он довольно медленный. \n"
                                              "Выполняет тело цикла до тех пор, "
                                              "пока условие цикла истинно.",
                                              "Сначала оценивается условие."
                                              "Если оно истинное, начинается цикл, и тело while исполняется.\n"
                                              "Тело будет исполняться до тех пор,"
                                              " пока условие остается истинным.\n"
                                              "Если оно становится ложным,"
                                              "программа выходит из цикла и прекращает исполнение тела."]
                         }


def ask_user(answers_dict):
    print('Здравствуйте!\n'
          'Задайте вопрос, а я постараюсь ответить на него, как надоест скажите "Пока"!\n')
    while True:
        user_says = input('Скажи что-нибудь: ')
        if user_says == 'Пока':
            print('Всего доброго! До свидания!')
            break
        elif user_says in answers_dict:
            print(answers_dict[user_says][randint(0, len(answers_dict[user_says]) - 1)])
        else:
            print('Я не понял!')


if __name__ == "__main__":
    ask_user(questions_and_answers)
