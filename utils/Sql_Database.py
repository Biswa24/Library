import sqlite3


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS novels(name text, author text, read integer )')
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO novels VALUES(?,?,?)', (name, author, 0))
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM novels ')
    books = cursor.fetchall()
    return books
    connection.close()


def mark_book_as_read(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE novels SET read = 1 WHERE name == ? AND author ==?', (name, author ))
    connection.commit()
    connection.close()


def delete_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM novels WHERE name ==? AND author==?', (name, author))
    connection.commit()
    connection.close()