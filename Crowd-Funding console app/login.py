"""
login function
"""
import json

def userlogin():
    email = input("Please enter your EMAIL ? ")
    password = input("Please enter your PASSWORD ? ")

    fileobj = open("info.txt", 'r')
    countr = 1
    for line in fileobj:
        l = list(line.split())
        if email == l[2] and password == str(l[3]):
            print("login success")
            countr = 0
            break
    if countr != 0:
        print("Fail")

    #list = []

    # try:
    #     fileobj = open("data_file.json", "r")
    #
    # except Exception as e:
    #     print(e)
    #
    # else:
    #     for line in fileobj:
    #         list.append(line)
    #
    #     #for record in list:
    #         #info = dict(record)
    #         #print(info)
    #     fileobj.close()

    #############################################


    # info = read_file()
    # for user in info:
    #     if user['email'] == email and user['password'] == password:
    #         print("successfully login")
    #         break
    # else:
    #     print("Wrong login")
    #     #userlogin()



#
# def read_file():
#     with open("data_file.json", "r") as read_file:
#         data_returned = json.load(read_file)
#         return data_returned
