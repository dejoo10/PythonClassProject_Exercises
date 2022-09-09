import sys


attempt = 0
trial = 0
username = "python"
password = "rules"


user_name = str(input("Enter your username"))
pass_word = str(input("Enter your password"))


while (username != user_name or password != pass_word) and trial < 1:
    while attempt < 4:
        user_name = str(input("Enter your username again"))
        pass_word = str(input("Enter your password again"))

        if user_name == username and pass_word == password:
            break


        attempt = attempt + 1

    trial = trial + 1
if user_name != username and pass_word != password:
    print("access block")
    exit()
print("Welcome")




sys.exit(4)