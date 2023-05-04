from datetime import timedelta
from datetime import datetime

speaker = 'Alex'
duration = 110.0
duration_timedelta = timedelta(minutes=duration)
delta = timedelta(minutes=10)
# print(duration_timedelta + delta)

# list
visitors = ['Dmitrii', 'Yarik', 'Kir']  # create list
# print(visitors[0])

# cycles
# for i in visitors:
#     print(i)
#
# print(len(visitors))

# dictionaries

visitor_dict = {}
visitor_dict['Dmitrii'] = 'Hello All'
visitor_dict['Yarik'] = 'Hello Dim'
visitor_dict['Kir'] = 'Wazaaap?'

# print(visitor_dict)
# print(visitor_dict['Kir'])
# print(len(visitor_dict))

# for in dict

# for key, value in visitor_dict.items():
#     print(F'Key: {key}, Value: {value}')

# functions
all_messages = []  # создаем пустой список сообщений


def add_message(author='Test', text='Test'):  # объявляем ффункуию добавления сообщений с параметрами
    message = {
        'author': author,
        'text': text,
        'time': datetime.now().strftime('%H:%M:%S'),
    }
    all_messages.append(message)  # добавляем параметризированное сообщшение в список всех сообщений


add_message('Dim', 'Qqq')  # вызываем функция для добавления сообщений
add_message(author='Yar', text='Hi')
add_message(text='Hi', author='Yar')


def print_message(msg):  # форматирование одного сообщения
    print(f"[{msg['author']}]: {{ {msg['text']} {msg['time']} }}")


def print_all_messages():  # форматированный вывод всех сообщений из списка
    for message in all_messages:
        print_message(message)


print_all_messages()
