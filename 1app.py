# Word Problem: The School Portal Login System
# Your school is creating a new online portal for students to sign up for accounts. The login system needs a function that accepts two pieces of information from the user:
# Their email address
# Their password
# Before creating the new account, the function must verify that the email and password follow school rules:
# The email must be a string and must contain an "@" symbol.
# The password must also be a string.
# The password must be at least 8 characters long.
# The password must include at least one number.
# The password must include at least one uppercase letter.
# If ANY of these rules are broken, the function should return an error message explaining what went wrong.
# If EVERYTHING is good, the function should return a dictionary that represents the newly created user.

def school_login(email,password):
    if "@" not in email:
        return "not in email format"
    if len(password) < 8:
        return "invalid password format"
    for i in password:
        if i == i.isdigit:
            i+=1
            if i>=1:
                print("valid password")
            else:
                print("invalid password")
    for x in password:
        if x == x.upper:
            x+=1
            if x>=1:
                print("valid password")
            else:
                print("invalid password")
school_login("nueina@gmail.com","123Abiopq")

    