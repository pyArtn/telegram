from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from students import student


def about_our_students():
    """
    Get keyboard with text 'about student'
    :return: keyboard
    """
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='наши студенты', callback_data='our_students'))
    return keyboard


def our_students():
    """
    get keyboard with students fullname
    :return:
    """
    keyboard = InlineKeyboardMarkup()
    students = student.get_students()
    for i in students:
        keyboard.add(InlineKeyboardButton(text=i[1], callback_data=i[0]))
    return keyboard


def info_student_repl():
    """
    reply menu in get student info
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
        'Список студентов').add('Скачать видео с ютуб')
    return keyboard
