#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
username=input("Enter the username")
username=str(username)

if usernmae=="admin":
    password=input("Enter the password")
    if password=="12345":
        print("Access granted")
    else:
        counter=counter+1
