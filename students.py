from database import db


class Student:
    def __init__(self):
        self.offset = 0

    @staticmethod
    def get_students():
        sql = 'SELECT id,fullname FROM students'
        try:
            db.cursor.execute(sql)
            result = db.cursor.fetchall()
            return result
        except Exception as ex:
            print(ex)

    @staticmethod
    def get_student_info(fullname):
        sql = f" SELECT * FROM students WHERE fullname = '{fullname}'"
        try:
            db.cursor.execute(sql)
            result = db.cursor.fetchone()
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
