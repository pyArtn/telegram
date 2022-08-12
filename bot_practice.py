import telebot

from redis_file import r
from keyboards import *
from students import student
from texts import about_student_text
from conf import TOKEN, chat_id
from download import download

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    id_user = message.chat.id

    message_ids = r.get_messages_from_list(user_id=id_user)
    for message_id in message_ids:  # delete messages
        bot.delete_message(id_user, int(message_id))
    r.delete_key(f"messages:{id_user}")

    try:
        check = bot.get_chat_member(chat_id=chat_id, user_id=id_user)
        msg = bot.send_message(id_user,
                               'Привет, я бот b-201. Мы создаем телеграм бота для практики.\n Что вы хотите узнать от нас?',
                               reply_markup=about_our_students())
        r.add_message_to_list_redis(user_id=message.chat.id, id_messages=[msg.id])
    except Exception as ex:
        print(ex)
        msg = bot.send_message(id_user,
                               text="Подпишись на <a href='https://t.me/kanal_servis'>канал</a> менеджеров",
                               parse_mode='HTML')
        r.add_message_to_list_redis(user_id=id_user, id_messages=[msg.id])


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    chat_id = call.message.chat.id

    message_ids = r.get_messages_from_list(user_id=chat_id)
    for message_id in message_ids:  # delete messages
        bot.delete_message(chat_id, int(message_id))
    r.delete_key(f"messages:{chat_id}")

    if call.data == 'our_students':
        msg = bot.send_message(chat_id=chat_id, text='<b>Наши студенты</b>',
                               reply_markup=our_students(), parse_mode='HTML')
        r.add_message_to_list_redis(chat_id, [msg.id])
    if call.data in [str(i[0]) for i in student.get_students()]:
        student_info = student.get_student_info(call.data)
        text = about_student_text.format(student_info[1], student_info[2], student_info[3], student_info[4],
                                         student_info[5])
        print(student_info[6])
        message_photo = bot.send_photo(chat_id=chat_id, photo=open(student_info[6], 'rb'), caption=text, parse_mode='HTML',
                                       reply_markup=info_student_repl())

        # msg = bot.send_message(chat_id=chat_id, text=text, parse_mode='html', reply_markup=info_student_repl())
        r.add_message_to_list_redis(chat_id, [message_photo.id])


@bot.message_handler(content_types=['text'])
def main(message):
    chat_id = message.chat.id

    message_ids = r.get_messages_from_list(user_id=chat_id)
    for message_id in message_ids:  # delete messages
        bot.delete_message(chat_id, int(message_id))
    r.delete_key(f"messages:{chat_id}")

    if message.text == 'Список студентов':
        msg = bot.send_message(chat_id=chat_id, text='<b>Наши студенты</b>',
                               reply_markup=our_students(), parse_mode='HTML')
        r.add_message_to_list_redis(chat_id, [msg.id])
    if message.text == 'Скачать видео с ютуб':
        msg = bot.send_message(chat_id=chat_id, text='Скидывай ссылку на видео =)')
        r.add_message_to_list_redis(chat_id, [msg.id])
        bot.register_next_step_handler(msg, download_video)


def download_video(message):
    chat_id = message.chat.id
    result = download(message.text)
    print(result)
    msg = bot.send_message(chat_id, text=f"<a href='{result}'>Жми на меня</a>", parse_mode='HTML')
    r.add_message_to_list_redis(chat_id, [msg.id])


bot.polling(none_stop=True, interval=0)
