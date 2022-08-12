from database import db


class Teacher:

    @staticmethod
    def get_teachers():
        sql = 'SELECT id,fullname FROM teachers'
        try:
            db.cursor.execute(sql)
            result = db.cursor.fetchall()
            return result
        except Exception as ex:
            print(ex)

    @staticmethod
    def get_teacher_info(fullname):
        sql = f" SELECT * FROM teachers WHERE fullname = '{fullname}'"
        try:
            db.cursor.execute(sql)
            result = db.cursor.fetchone()
            return result
        except Exception as ex:
            print(ex)


teacher = Teacher()