import mysql.connector


conn = mysql.connector.connect( host= "localhost",
                                user = "root",
                                passwd = "Ambidextrous",
                                database= "flight_game"
                                )


user = input("Enter the ICAO code of any airport:")
config = conn.cursor()
config.execute("select name, location from airport, game where ident = " + "'" + user + "'")

for i in config:
    print(i)





