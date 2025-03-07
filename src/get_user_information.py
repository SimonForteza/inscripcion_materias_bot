from dotenv import load_dotenv
import os

def get_user_info():
    load_dotenv()
    user = os.getenv("MY_USERNAME")
    password = os.getenv("PASSWORD")
    return user, password