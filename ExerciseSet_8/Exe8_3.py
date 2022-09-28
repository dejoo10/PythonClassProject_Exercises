import mysql.connector
import geopy
from geopy import distance



conn = mysql.connector.connect( host= "localhost",
                                user = "root",
                                passwd = "Ambidextrous",
                                database = "flight_game"
                                )

icao_code1 = input("Enter the first ICAO code")
icao_code2 = input("Enter the second ICAO code")
sql = "select latitude_deg, longitude_deg from airport where ident = " + "'" + icao_code1 + "'"
stm = "select latitude_deg, longitude_deg from airport where ident = " + "'" + icao_code2 + "'"
con_fig = conn.cursor()
con_fig.execute(sql)


for i in con_fig:
    print(i)

con_fig.execute(stm)
for j in con_fig:
    print(j)

print(distance.distance(i, j).km)