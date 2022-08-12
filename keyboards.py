from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from students import student
from teachers import teacher



def about_our_students():
    """
    Get keyboard with text 'about student'
    :return: keyboard
    """
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='наши студенты', callback_data='our_students'),InlineKeyboardButton(text='наши учителя', callback_data='our_teachers'))
    return keyboard


def our_students():
    """
    get keyboard with students fullname
    :return:
    """
    keyboard = InlineKeyboardMarkup()
    students = student.get_students()
    for i in students:
        keyboard.add(InlineKeyboardButton(text=i[1], callback_data=i[1]))
    return keyboard

def get_our_teachers():
    """
    get keyboard with teachers fullname
    :return:
    """
    keyboard = InlineKeyboardMarkup()
    teachers = teacher.get_teachers()
    for i in teachers:
        keyboard.add(InlineKeyboardButton(text=i[1], callback_data=i[1]))
    return keyboard



def info_student_repl():
    """
    reply menu in get student info
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
        'Список студентов').add('Список учителя').add('Скачать видео с ютуба')
    return keyboard
