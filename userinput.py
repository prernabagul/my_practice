username = input("enter your name: ")

if len(username) > 12:
    print("username cannot be more then 12 characters")
elif not username.find(" ") == -1:
    print("username cannot contain spaces") 
elif not username.isalpha():
    print("username cannot contain digits")
else:
    print(f"welcome {username}")
