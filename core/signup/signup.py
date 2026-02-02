
def Signup(signup_que, call_func):

    if signup_que.lower() == "yes":
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        print(f"Welcome back, {input_username}")
    else:
        call_func()