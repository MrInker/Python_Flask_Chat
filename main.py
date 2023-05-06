# TODO Upload to GIT

from flask import Flask, render_template, request  # импорируем фласк, предваительно установив
from datetime import datetime
import json
import os.path

app = Flask(__name__)  # Создаем экземпляр приложения
MAIN_HOST = '0.0.0.0'
all_messages = []


def load_messages():
    with open('db.json', 'r') as file:
        data = json.load(file)  # чтение из файла
    return data['messages']


if os.path.isfile('db.json') == False:
    with open('db.json', 'w') as file:
        print('Created db.json')
if os.path.getsize('db.json') > 0:
    all_messages = load_messages()


def add_message(author='Test', text='Test'):  # объявляем ффункуию добавления сообщений с параметрами
    message = {
        'author': author,
        'text': text,
        'time': datetime.now().strftime('%H:%M:%S'),
    }
    all_messages.append(message)  # добавляем параметризированное сообщшение в список всех сообщений
    save_message()


def save_message():  # сохраняем все сообщения в файл
    all_messages_data = {'messages': all_messages}
    with open('db.json', 'w') as file:
        json.dump(all_messages_data, file)  # загрузка в файл


@app.route('/')  # Реализуем ЕНД поинт начальной страницы через декоратор!
def main_page():
    return 'Hellooo. </br> There is <a href="/chat"> CHARTA </a> </br> There is <a href="/status"> STATUS </a>'


@app.route('/chat')  # Реализуем ЕНД поинт начальной страницы через декоратор!
def chat_page():
    return render_template('form.html')


@app.route('/get_messages')
def get_messages():
    # print('Отдаем все сообщения')
    return {'messages': all_messages}


@app.route('/send_message')
def send_message():
    name = request.args.get('name')  # получаем данные из query запроса к серверу
    text = request.args.get('text')


    print(f'User: "{name}", say: "{text}"')
    add_message(name, text)
    return 'ok'


@app.route('/status')
def status_chat():

    if os.path.getsize('db.json') == 0:
        return 'Записей нет'
    with open('db.json', 'r') as file:
        data = json.load(file)
    n_messages = int(len(data['messages']))

    doct2 = []
    for k in range(n_messages):
        doct2.append(data['messages'][k]['author'])

    n_users = int(len(set(doct2)))

    return f'Количество пользователей(считаем что имена уникальные): {n_users} </br></br>Сообщений в чате всего: {n_messages}'


if __name__ == '__main__':
    app.run(host=MAIN_HOST, port=8080)  # конфигурируем параметны запускаемого приложения
