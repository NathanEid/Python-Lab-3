
"""
main page for the project
        Crowd-Funding console app
"""
import registration
import login

print("Welcome to the Crowd-Funding console app")

choice = input("Please choose registration or login : \n 1) Registration \n 2) Login \n 3) Exit \n")

check = True
while check:
    if choice == "1":
        registration.getData()
        break
    elif choice == "2":
        login.userlogin()
        break
    elif choice == "3":
        check = False
    else:
        choice = input("You should choose registration or login : \n 1) Registration \n 2) Login \n 3) Exit")

