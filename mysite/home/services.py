from django.db import connection
from contextlib import closing



def post(code):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT title_{code} as title, description_{code} as description, image FROM home_post ")
        header = dict_fetchall(cursor)
        return header

def followers(code):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT comment_{code} as comment, full_name,image FROM home_followers ")
        header = dict_fetchall(cursor)
        return header
def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
