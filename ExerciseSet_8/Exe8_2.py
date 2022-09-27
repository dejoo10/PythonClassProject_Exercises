import mysql.connector

conn = mysql.connector.connect( host= "localhost",
                                user = "root",
                                passwd = "Ambidextrous",
                                database= "flight_game"
                                )


user = input("Enter the area code of any country:")
synt = "select name, type from airport where iso_country =" + "'"+ user + "'" + "order by type desc"
config = conn.cursor()
config.execute( synt)
for i in config:
    print(i)

