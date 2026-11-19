 #validating user input
#rules:
# 1. username is no more than 12 charcters
#2 . username must not contain spaces
# 3. username must contain digits

username = input("Enter a username = ")



if len(username) > 12:
    print("Your username has to be 12 or under characters")
elif not username.find(" ") == -1:
   print("your username cant contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username} your username is valid44r")


