import sys


empty = ""
airport = {"AYAA" : "AMA AIRPORT",
           "AYBK" : "BULOLO AIRPORT",
           "AYDU" : "DARU AIRPORT",
           "AYGA" : "GURNEY AIRPORT",
           "AYHK" : "HOSKINS AIRPORT"}

user = "x"
while user != "":
    user = input("Will you like to enter a new airport? answer yes or no, or press enter to quit").upper()
    if user == "YES":
        code = input("Enter the ICAO code and name of the airport").upper()
        name = input("Enter the name of the airport").upper()
        airport[code] = name
        print(airport)
    elif user == "NO":
        re_user = input(" Will you like to fetch information of an existing airport").upper()
        if re_user == "YES":
            code = input( "ICAO code of the airport").upper()
            print(f"Airport with  {code} ICAO code is {airport[code]}")
        else:
            print("You can start again")
    elif user == "":
            print("You have exited the system")




sys.exit(0)


empty = ""
airport = {"AYAA" : "AMA AIRPORT",
           "AYBK" : "BULOLO AIRPORT",
           "AYDU" : "DARU AIRPORT",
           "AYGA" : "GURNEY AIRPORT",
           "AYHK" : "HOSKINS AIRPORT"}

count = 0
user = input("Will you like to enter a new airport? answer yes or no, you press enter to quit").upper()
while True:
    if user == "YES":
        code = input("Enter the ICAO code and name of the airport").upper()
        name = input("Enter the name of the airport").upper()
        airport[code] = name
        print(airport)
    else:
        re_user = input(" Will you like to fetch information of an exisiting airport").upper()
        if re_user == "YES":
            code = input( "ICAO code of the airport").upper()
            if code in airport:
                print(f"Airport with {code} is {airport[code]}")
        else:
            print("end")



sys.exit(0)