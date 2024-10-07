import sqlite3

##connection
connection = sqlite3.connect("student.db")

##cursor object 

cursor = connection.cursor()

# table_info = '''
# CREATE TABLE STUDENT(NAME VARCHAR(25),CLASS VARCHAR(10),SECTION VARCHAR(5));
# '''
#cursor.execute(table_info)

##insert

cursor.execute('''INSERT INTO STUDENT VALUES('Saravana','ML','A') ''')
cursor.execute('''INSERT INTO STUDENT VALUES('Saravanakumar','ML','A') ''')
cursor.execute('''INSERT INTO STUDENT VALUES('Kumar','ML','B') ''')
cursor.execute('''INSERT INTO STUDENT VALUES('KumarSaravana','ML','C') ''')


print("Insert records are")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)
connection.commit()
connection.close()