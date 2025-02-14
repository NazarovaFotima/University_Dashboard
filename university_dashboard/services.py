from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from university_dashboard_faculty""")
        faculties = dictfetchall(cursor)
        return faculties


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from university_dashboard_kafedra""")
        kafedras = dictfetchall(cursor)
        return kafedras


def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from university_dashboard_subject""")
        subjects = dictfetchall(cursor)
        return subjects


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT university_dashboard_teacher.id, university_dashboard_teacher.first_name, university_dashboard_teacher.last_name, university_dashboard_teacher.age, 
        university_dashboard_kafedra.name as kafedra_name, university_dashboard_subject.name as subject_name from university_dashboard_teacher 
        left join university_dashboard_kafedra on university_dashboard_teacher.kafedra_id = university_dashboard_kafedra.id left join university_dashboard_subject on university_dashboard_teacher.subject_id =university_dashboard_subject.id""")
        teachers = dictfetchall(cursor)
        return teachers


def get_group():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT university_dashboard_group.id, university_dashboard_group.name, university_dashboard_faculty.name as faculty from university_dashboard_group left join university_dashboard_faculty on university_dashboard_group.faculty_id=university_dashboard_faculty.id""")
        groups = dictfetchall(cursor)
        return groups


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT university_dashboard_student.id, university_dashboard_student.first_name, university_dashboard_student.last_name, 
        university_dashboard_student.age, university_dashboard_group.name as group_name, university_dashboard_student.image as image from university_dashboard_student
        left join university_dashboard_group on university_dashboard_student.group_id = university_dashboard_group.id""")
        students = dictfetchall(cursor)
        return students

