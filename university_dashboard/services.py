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
        cursor.execute("""SELECT * from university_dashboard_teacher""")
        teachers = dictfetchall(cursor)
        return teachers


def get_group():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from university_dashboard_group""")
        groups = dictfetchall(cursor)
        return groups


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from university_dashboard_student""")
        students = dictfetchall(cursor)
        return students

