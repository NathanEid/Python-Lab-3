"""
registration function to get the data from the user and stor it in a file
"""
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
mobileregex= '^01[0-2,5]{1}[0-9]{8}$'


def getData():
    firstname = input("What is your FIRST NAME ? ")
    while True:
        if firstname.isalpha():
            break
        else:
            firstname = input("Invalid NAME, What is your FIRST NAME ? ")

    lastname = input("What is your LAST NAME ? ")
    while True:
        if lastname.isalpha():
            break
        else:
            lastname = input("Invalid NAME What is your LAST NAME ? ")

    email = input("What is your EMAIL ? ")
    while True:
        if re.fullmatch(regex, email):
            break
        else:
            email = input("Invalid EMAIL, What is your EMAIL ? ")

    password = input("What is your PASSWORD ? ")

    confpassword = input("Please CONFIRM your PASSWORD ? ")
    while True:
        if confpassword == password:
            break
        else:
            confpassword = input("It doesn't MATCH, Please CONFIRM your PASSWORD ? ")

    mobile = input("What is your MOBILE PHONE ? ")
    while True:
        if re.match(mobileregex, mobile):
            break
        else:
            mobile = input("Invalid MOBILE PHONE, What is your MOBILE PHONE ? ")

    info = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "password": password,
        "mobile": mobile
    }

    try:
        fileobj = open("info.txt", "a")
        fileobj.write(f"{firstname} {lastname} {email} {password} {mobile}\n")
        fileobj.close()
    except Exception as e:
        print(e)

    # try:
    #     fileobj = open("data.jason", "a")
    #     fileobj.write(f"{info} \n")
    #     fileobj.close()
    # except Exception as e:
    #     print(e)

    # try:
    #     with open("data_file.json", "a") as write_file:
    #         json.dump(info, write_file)
    # except Exception as e:
    #     print(e)





