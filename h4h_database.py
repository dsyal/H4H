# import the sqlite3 module
import sqlite3

# Define connection and cursor
connection = sqlite3.connect('h4h_database.db')
cursor = connection.cursor()


# create USER table
cursor.execute("DROP TABLE IF EXISTS USER")
createUserTable = '''CREATE TABLE USER(
Name VARCHAR(100), login VARCHAR(100),
password VARCHAR(100), startTime time,
endTime time
)'''
cursor.execute(createUserTable)
# Insert data into the table when you get it
cursor.execute("INSERT INTO USER VALUES ('Asad','abaloch', 'isthebest', 070000, 010000)")

cursor.execute("SELECT * FROM USER")

# printing the cursor data
print(cursor.fetchall())

# create Password table
cursor.execute("DROP TABLE IF EXISTS PW")
createPWTable = '''CREATE TABLE PW(
color VARCHAR(100), shape VARCHAR(100),
words VARCHAR(100)
)'''
cursor.execute(createPWTable)

cursor.execute("INSERT INTO PW VALUES ('orange','sad', 'soccer')")
cursor.execute("INSERT INTO PW VALUES ('brown','pentagon', 'badminton')")
cursor.execute("INSERT INTO PW VALUES ('teal','smiley', 'golf')")
cursor.execute("INSERT INTO PW VALUES ('purple','spades', 'republic')")
cursor.execute("INSERT INTO PW VALUES ('pink','clover', 'computer')")
cursor.execute("INSERT INTO PW VALUES ('yellow','diamond', 'stylus')")
cursor.execute("INSERT INTO PW VALUES ('red','heart', 'hack')")
cursor.execute("INSERT INTO PW VALUES ('blue','star', 'butter')")
cursor.execute("INSERT INTO PW VALUES ('green','slant', 'mask')")
cursor.execute("INSERT INTO PW VALUES ('black','square', 'horse')")
cursor.execute("INSERT INTO PW VALUES ('white','circle', 'horse')")
cursor.execute("INSERT INTO PW VALUES ('silver','triangle', 'computer')")


cursor.execute("SELECT * FROM PW")

# printing the cursor data
print(cursor.fetchall())

# create COLOR table
cursor.execute("DROP TABLE IF EXISTS COLOR")
createColorTable = '''CREATE TABLE COLOR(
color_entry VARCHAR(100)
)'''
cursor.execute(createColorTable)

cursor.execute("INSERT INTO COLOR VALUES ('orange')")
cursor.execute("INSERT INTO COLOR VALUES ('brown')")
cursor.execute("INSERT INTO COLOR VALUES ('teal')")
cursor.execute("INSERT INTO COLOR VALUES ('purple')")
cursor.execute("INSERT INTO COLOR VALUES ('pink')")
cursor.execute("INSERT INTO COLOR VALUES ('yellow')")
cursor.execute("INSERT INTO COLOR VALUES ('red')")
cursor.execute("INSERT INTO COLOR VALUES ('blue')")
cursor.execute("INSERT INTO COLOR VALUES ('green')")
cursor.execute("INSERT INTO COLOR VALUES ('black')")
cursor.execute("INSERT INTO COLOR VALUES ('white')")
cursor.execute("INSERT INTO COLOR VALUES ('silver')")


# create WORD table
cursor.execute("DROP TABLE IF EXISTS WORD")
createWordTable = '''CREATE TABLE WORD(
word_entry VARCHAR(100)
)'''
cursor.execute(createWordTable)

cursor.execute("INSERT INTO WORD VALUES ('soccer')")
cursor.execute("INSERT INTO WORD VALUES ('badminton')")
cursor.execute("INSERT INTO WORD VALUES ('golf')")
cursor.execute("INSERT INTO WORD VALUES ('republic')")
cursor.execute("INSERT INTO WORD VALUES ('computer')")
cursor.execute("INSERT INTO WORD VALUES ('stylus')")
cursor.execute("INSERT INTO WORD VALUES ('hack')")
cursor.execute("INSERT INTO WORD VALUES ('butter')")
cursor.execute("INSERT INTO WORD VALUES ('mask')")
cursor.execute("INSERT INTO WORD VALUES ('horse')")
cursor.execute("INSERT INTO WORD VALUES ('horse')")
cursor.execute("INSERT INTO WORD VALUES ('computer')")

# create SHAPE table
cursor.execute("DROP TABLE IF EXISTS SHAPE")
createShapeTable = '''CREATE TABLE SHAPE(
shape_entry VARCHAR(100)
)'''
cursor.execute(createShapeTable)

cursor.execute("INSERT INTO Shape VALUES ('sad')")
cursor.execute("INSERT INTO Shape VALUES ('pentagon')")
cursor.execute("INSERT INTO Shape VALUES ('smiley')")
cursor.execute("INSERT INTO Shape VALUES ('spades')")
cursor.execute("INSERT INTO Shape VALUES ('clover')")
cursor.execute("INSERT INTO Shape VALUES ('diamond')")
cursor.execute("INSERT INTO Shape VALUES ('heart')")
cursor.execute("INSERT INTO Shape VALUES ('star')")
cursor.execute("INSERT INTO Shape VALUES ('slant')")
cursor.execute("INSERT INTO Shape VALUES ('square')")
cursor.execute("INSERT INTO Shape VALUES ('circle')")
cursor.execute("INSERT INTO Shape VALUES ('triangle')")




#cursor.execute("Show tables");
# check the database creation data
if cursor:
	print("Database Created Successfully !")
else:
	print("Database Creation Failed !")

# Commit the changes in database and Close the connection
connection.commit()
connection.close()

