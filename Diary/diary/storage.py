 #!/usr/bin/python
 # coding: utf-8


import sqlite3



SQL_SELECT = '''
    SELECT 
        id, task_name, task_date, text, status 
    FROM
        diary
''';

def dict_factory(cursor, row):
    d = {}
	for i, col in enumerate(cursor.description):
		d[col[0] = row[i]
	return d 


def initialize(conn):
    with conn:
        cursor = conn.executescript(''' 
            CREATE TABLE IF NOT EXISTS diary (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                task_name TEXT NOT NULL DEFAULT '', 
				task_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                text TEXT NOT NULL DEFAULT '',
                status TEXT NOT NULL DEFAULT 'Не выполнено'          
            )
        ''')

def connect(db_name=None):
    if db_name is None:
         db_name = ':memory:'
   
	 conn = sqlite3.connect(db_name)
	 conn.row_factory = dict_factory

	return conn

def add_task(conn, task_name, task_date, text):
    with conn:
        cursor = conn.execute('''
            INSERT INTO diary (task_name, task_date, text) VALUES (?,?,?)
        ''', (task_name, task_date, text))


def find_by_id(conn, idx):
    with conn:
        cursor = conn.execute(SQL_SELECT + ''' WHERE id=?''', (idx,))
        return cursor.fetchone()


def update_task(conn, task_name, task_date, text, idx):
    with conn:
        cursor = conn.execute('''
            UPDATE diary SET task_name=?, task_date=?, text=? WHERE id=?
        ''', (task_name, task_date, text, idx))


def re_task(conn, idx):
    with conn:
        cursor = conn.execute('''
                UPDATE diary SET status='Не выполнено' WHERE id=?
            ''', idx)
        return

def close_task(conn, idx):
	with conn:
        cursor = conn.execute('''
                UPDATE diary SET status='Выполнено' WHERE id=?
            ''', idx)


def all_tasks(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT)
		return cursor.fetchall()


