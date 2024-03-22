#!/usr/bin/env python3
import os
from simple_term_menu import TerminalMenu

RULES_GEN_MOD = ['rapide', 'avancé']
RULES_KEY_TYPE = ['rsa', 'dsa', 'ecdsa', 'eddsa']
RULES_RSA_KEY_SIZE = ['1024', '2048', '4096', '8192']
RULES_ECDSA_KEY_SIZE = ['256', '384', '521']
RULES_KEY_NAME = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '[', ']', '{', '}', ';', ':', '"', ',', '<', '.', '>', '/', '?', '\'', ']', ' ']

gen_mod = None
key_type = None
key_size = None
key_directory = None
key_name = None

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_gen_mod():
    mode_menu = TerminalMenu(["Rapide", "Avancé"])
    mode_index = mode_menu.show()
    return RULES_GEN_MOD[mode_index]

def get_user_input(message):
    return input(message).strip()

def get_key_type():
    key_type_menu = TerminalMenu(RULES_KEY_TYPE)
    key_type_index = key_type_menu.show()
    return RULES_KEY_TYPE[key_type_index]

def get_key_size():
    global key_size
    key_size_menu = None
    if key_type == 'rsa':
        key_size_menu = TerminalMenu(RULES_RSA_KEY_SIZE)
    elif key_type == 'ecdsa':
        key_size_menu = TerminalMenu(RULES_ECDSA_KEY_SIZE)
    
    if key_size_menu:
        key_size_index = key_size_menu.show()
        key_size = key_size_menu[key_size_index]
    else:
        key_size = None

def get_key_directory():
    global key_directory
    user_name = os.getlogin()
    home_directory = os.path.expanduser(f"~{user_name}")
    key_directory = os.path.join(home_directory, '.ssh')
    return key_directory

def get_key_name():
    global key_name
    key_name = get_user_input("Comment souhaitez-vous appeler votre clé ? : ")
    while any(char in key_name for char in RULES_KEY_NAME):
        print("Nom invalide, évitez les caractères spéciaux tels que : '!', '@', '#', etc.")
        key_name = get_user_input("Comment souhaitez-vous appeler votre clé ? : ")

def get_key_parameter():
    global key_type, key_size, key_name, key_directory
    key_type = get_key_type()
    get_key_size()
    get_key_name()
    key_directory = get_key_directory()

def generate_key():
    clear_terminal()
    if key_size is None:
        os.system(f"ssh-keygen -t ed25519 -f {key_directory}/{key_name}")  
    elif gen_mod == 'rapide':
        os.system(f"ssh-keygen -t ed25519 -f {key_directory}/{key_name}")  
    elif gen_mod == 'avancé':
        os.system(f"ssh-keygen -t {key_type} -b {key_size} -f {key_directory}/{key_name}")
    os.chdir(key_directory)

def print_key():
    generate_key()
    clear_terminal()
    print(f"Voici votre clé SSH publique :\n")
    with open(f"{key_name}.pub", "r") as public_key:
        print(public_key.read())

if __name__ == "__main__":
    clear_terminal()
    gen_mod = get_gen_mod()
    get_key_parameter()
    print_key()
    