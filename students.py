import json

from redis_file import r
from database import db


class Student:
    def __init__(self):
        self.offset = 0

    @staticmethod
    def get_students():
        sql = 'SELECT id,fullname FROM students'
        redis_result = r.get_value(['get_students'])
        try:
            if redis_result is not None:
                return redis_result
            else:
                db.cursor.execute(sql)
                result = db.cursor.fetchall()
                r.add_key('get_students', result)
                return result
        except Exception as ex:
            print(ex)

    @staticmethod
    def get_student_info(id):
        sql = f'SELECT * FROM students WHERE id = {id}'
        redis_result = r.get_value([f"get_student_info:{id}"])
        try:
            if redis_result is not None:
                return redis_result
            else:
                db.cursor.execute(sql)
                result = db.cursor.fetchone()
                r.add_key(f"get_student_info:{id}", result)
                return result
        except Exception as ex:
            print(ex)

    def get_students_offset_2(self, call_data='default'):
        sql = "SELECT * FROM students ORDER BY age LIMIT 2 OFFSET {}"
        try:
            if call_data == 'prev_2_students':
                self.offset -= 2
                db.cursor.execute(sql.format(self.offset))
                return db.cursor.fetchall()
            elif call_data == 'next_2_students':
                self.offset += 2
                db.cursor.execute(sql.format(self.offset))
                return db.cursor.fetchall()
            else:
                db.cursor.execute(sql.format(self.offset))
                return db.cursor.fetchall()
        except Exception as ex:
            print(ex)

    @staticmethod
    def get_first_2_students(self):
        sql = "SELECT * FROM students ORDER BY age LIMIT 2"
        try:
            db.cursor.execute(sql)
            return db.cursor.fetchall()
        except Exception as ex:
            print(ex)


student = Student()
