import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "12227067"))
    API_HASH = os.getenv("API_HASH", "b463bedd791aa733ae2297e6520302fe")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5850629523:AAEJBWduZfIGyERyiXA9ctu-E0RrcnDnoi0")
    sudo = os.getenv("SUDO","6246163989 1817166549 6255094965")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
