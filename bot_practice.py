import telebot

from keyboards import *
from students import student
from texts import about_student_text
from conf import TOKEN, chat_id
from download import download

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    try:
        check = bot.get_chat_member(chat_id=chat_id, user_id=message.chat.id)
        msg = bot.send_message(message.chat.id,
                               'Привет, я бот b-201. Мы создаем телеграм бота для практики.\n Что вы хотите узнать от нас?',
                               reply_markup=about_our_students())
    except Exception as ex:
        msg = bot.send_message(message.chat.id,
                               text="Подпишись на <a href='https://t.me/kanal_servis'>канал</a> менеджеров",
                               parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    chat_id = call.message.chat.id
    if call.data == 'our_students':
        bot.send_message(chat_id=chat_id, text='<b>Наши студенты</b>',
                         reply_markup=our_students(), parse_mode='HTML')
    if call.data in [str(i[0]) for i in student.get_students()]:
        student_info = student.get_student_info(call.data)
        text = about_student_text.format(student_info[1], student_info[2], student_info[3], student_info[4],
                                         student_info[5])

        msg = bot.send_message(chat_id=chat_id, text=text, parse_mode='html', reply_markup=info_student_repl())


@bot.message_handler(content_types=['text'])
def main(message):
    chat_id = message.chat.id
    if message.text == 'Список студентов':
        bot.send_message(chat_id=chat_id, text='<b>Наши студенты</b>',
                         reply_markup=our_students(), parse_mode='HTML')
    if message.text == 'Скачать видео с ютуб':
        msg = bot.send_message(chat_id=chat_id, text='Скидывай ссылку на видео =)')
        bot.register_next_step_handler(msg, download_video)


def download_video(message):
    result = download(message.text)
    bot.send_message(message.chat.id, text=f"<a href=f'{result}'>Жми на меня</a>", parse_mode='HTML')


bot.polling(none_stop=True, interval=0)
