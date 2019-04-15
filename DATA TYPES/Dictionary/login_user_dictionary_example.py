def accept_login(users,username,password):
    if username in users and users[username] == password:
        return True
    else:
        return False

if __name__ == "__main__":
    
    users = {
                "admin@nkpydev.net" : "password1",
                "nkuser@nkpydev.net" : "password2"        
            }
    
    if accept_login(users,"nkuser@nkpydev.net","password2"):
        print('Login Successful!')
    else:
        print('Login Failed!')