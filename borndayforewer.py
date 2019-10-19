"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
# Дата рождения А.С Пушкина = 26 мая 1799 г.

pushkin_year = 1799
pushkin_day = 27

def question_answer(question, correct_answer):
    user_answer = None
    while user_answer != correct_answer:
        if user_answer is not None:
            print("Не верно")
        user_answer = input(question)
        while not user_answer.isdigit():
            print("Не верно")
            user_answer = input(question)
        user_answer = int(user_answer)


question_answer('Введите год рождения А.С Пушкина: ', pushkin_year)
question_answer('Введите день рождения А.С Пушкина: ', pushkin_day)
print("Верно")
