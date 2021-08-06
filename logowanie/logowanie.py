
accounts = {}


while True:
    option = input("Type 'Sign in' or 'Log in' ")
    login = input("Login :")
    password = input("Password: ")
    if option == "Sign in":
        accounts[login]=password

        pass
    elif option =="Log in":
        if accounts[login]==password:
            print("succes")
            break        
    else:
        pass