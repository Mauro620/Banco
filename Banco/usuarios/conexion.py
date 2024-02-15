import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "banco",
    port = 3306
)

#print(database)

cursor = database.cursor(buffered=True)
