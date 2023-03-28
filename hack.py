import mysql.connector as database

connection = database.connect(
    user = "Pi",
    password = "1234",
    host = "localhost",
    database = "hack"
)

cursor = connection.cursor()

f1 = open("hostel_out.txt", "r")
lines = f1.readlines()
for i in lines:
    statement = "UPDATE students set Inside_Hostel = 'No' WHERE tag_id = " + i[:10]
    cursor.execute(statement)
f1.close()

f2 = open("hostel_in.txt", "r")
lines = f2.readlines()
for i in lines:
    statement = "UPDATE students set Inside_Hostel = 'Yes' WHERE tag_id = " + i[:10]
    cursor.execute(statement)
f2.close()

f3 = open("campus_out.txt", "r")
lines = f3.readlines()
for i in lines:
    statement = "UPDATE students set Inside_Campus = 'No' WHERE tag_id = " + i[:10]
    cursor.execute(statement)
f3.close()

f4 = open("campus_in.txt", "r")
lines = f4.readlines()
for i in lines:
    statement = "UPDATE students set Inside_Campus = 'Yes' WHERE tag_id = " + i[:10]
    cursor.execute(statement)
f4.close()

connection.commit()

    
