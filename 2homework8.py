import sqlite3


personal_base = sqlite3.connect("Personal.ID")
sql = personal_base.cursor()

sql.execute(
    """CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    id TEXT
    )
    """
)
personal_base.commit()

def filling_user():
    global user_name, user_id
    user_name = input('Name: ')
    user_id = input('ID: ')


    sql.execute(f"SELECT name FROM users WHERE name ='{user_name}' ")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?)", (user_name, user_id ))
        personal_base.commit()
        print('USER REGISTERED')
    for value in sql.execute('SELECT * FROM users'):
        print(value)
    else:

        print('такие данные уже существуют')
        personal_base.commit()

if __name__ == '__main__':
    filling_user()

def delete():
    for value in sql.execute("SELECT * FROM users"):
        print(value)
    a = input('Выберите данные: ')
    sql.execute(f"SELECT affairs FROM users WHERE affairs = '{a}'")
    if sql.fetchone():
        b = input("Удалить или нет?(да или нет)")
        if b == 'да':
            sql.execute(f"DELETE FROM users WHERE affairs = '{a}'")
            print('Данные удалена')
        elif b == 'нет':
            print('Данные остались')
            personal_base.commit()

if __name__ == '__main__':
    delete()