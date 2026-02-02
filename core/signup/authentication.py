from .login import Login
from .signup import Signup

signup_que = input("Do you have an account? (yes/no): ")

def authentication():
    Signup(signup_que, Login)