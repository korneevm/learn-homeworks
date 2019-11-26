"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

dialog = {
         "Как дела?"                    : "Хорошо",
         "Что дедаешь?"                 : "Прогаю",
         "Откуда ты?"                   : "Из Никеля",
         "Как погода?"                  : "Идёт кислотный дождь",
         "Как прожить и не работать?"   : "Никак",
         "Сколько километров до столицы": "Как до луны",
         "Сколько можно вопросов!?"     : "Наверное хватит",
     }
def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            request = str(input("Задай вопрос "))
            for key, value in dialog.items():
                if key == request:
                    print("Вот тебе ответ: ", value)
                    break
    
        except KeyboardInterrupt:
            print("Пока!")
            break


if __name__ == "__main__":
    ask_user()
