from constant import *
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(message):
    return input(message).strip()

def get_key_type():
    while True:
        global key_type
        key_type = get_user_input("Quel type de clé souhaitez-vous utiliser ? : ")
        if key_type in RULES_KEY_TYPE:
            clear_terminal()
            print(f"Vous avez choisi le type de clé '{key_type}'")
            return key_type
        else:
            print("Type de clé non valide. Veuillez entrer 'rsa', 'dsa', 'ecdsa' ou 'eddsa'.")

def get_key_size():
    global key_size
    match key_type:
        case 'rsa':   
            while True:
                key_size = get_user_input("En combien de bits voulez-vous encoder votre clé ? : ")
                if key_size in RULES_RSA_KEY_SIZE:
                    clear_terminal()
                    print(f"Vous avez encodé votre clé en {key_size} bits")
                    return key_size
                else:
                    print("Encodage non valide. Veuillez entrer '1024', '2048', '4096' ou '8192'.")

        case 'dsa':
            key_size = '1024'
            return key_size
        
        case 'ecdsa':
            while True:
                key_size = get_user_input("En combien de bits voulez-vous encoder votre clé ? : ")
                if key_size in RULES_ECDSA_KEY_SIZE:
                    clear_terminal()
                    print(f"Vous avez encodé votre clé en {key_size} bits")
                    return key_size
                else:
                    print("Encodage non valide. Veuillez entrer '256', '384' ou '521'.")
                    
        case 'eddsa': 
            key_size = None
            return key_size

def get_key_directory():
    global key_directory
    user_name = os.getlogin()
    home_directory = os.path.expanduser(f"~{user_name}")
    key_directory = os.path.join(home_directory, '.ssh')
    return key_directory

def get_key_name():
    global key_name
    while True:
        key_name = get_user_input("Comment souhaitez-vous appeler votre clé ? : ")
        if all(char not in key_name for char in RULES_KEY_NAME):
            clear_terminal()
            print(f"Vous avez nommé votre clé : {key_name}")
            return key_name
        else:
            print("Nom invalide, évitez les caractères spéciaux tels que : '!', '@', '#', etc.")

def get_key_parameter():
    get_key_type()
    get_key_size()
    get_key_directory()
    get_key_name()

def generate_key():
    clear_terminal()
    if key_size == None:
        os.system(f"ssh-keygen -t ed25519 -f {key_directory}/{key_name}")  
        os.chdir(key_directory)
        
    else:
        os.system(f"ssh-keygen -t {key_type} -b {key_size} -f {key_directory}/{key_name}")
        os.chdir(key_directory)

def print_key():
    clear_terminal()
    generate_key()
    print(f"Voici votre clé SSH publique :\n")
    with open(f"{key_name}.pub", "r") as public_key:
        print(public_key.read())
