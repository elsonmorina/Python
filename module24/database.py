import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL
    )
''')

#COMMIT THE CHANGES

connection.commit()

cursor.execute('''
    INSERT INTO employees(name,position,department,salary)
    VALUES (?,?,?,?)
    

''',('John Doe','Software Engineer','IT',7000.00))

connection.commit()

cursor.execute('SELECT * FROM employees')

rows = cursor.fetchall()

for row in rows:
    print(row)
cursor.execute('''
    UPDATE employees
    SET SALARY = ?
    WHERE name = ?
''',(7500.00,'John Doe'))
connection.commit()
cursor.execute('SELECT * FROM employees')

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('''
    DELETE FROM employees
    WHERE name = ?
''',('John Doe',))

connection.commit()

cursor.close()
connection.close()