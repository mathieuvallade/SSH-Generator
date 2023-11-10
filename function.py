from constant import *
import os

key_type = None
key_size = None
key_name = None
key_directory = None

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_key_type():
    print("Quelle type de clé souhaitez vous utiliser ? : ")
    key_type = input()
    return key_type
    
def get_key_size():
    print("En combien de bit voulez vous encoder votre clé ? : ")
    key_size = input()
    return key_size

def get_key_directory():
    user_name = os.getlogin()
    home_directory = os.path.expanduser(f"~{user_name}")
    key_directory = os.path.join(home_directory, '.ssh')
    return key_directory
    
def get_key_name():
    print("Comment souhaitez vous appeller votre clé ? : ")
    key_name = input()
    return key_name

def check_key_type():
    while True:
        key_type = get_key_type()
        
        if key_type not in RULES_KEY_TYPE:
            print("Type de clé non valide. Veuillez entrer 'rsa', 'dsa' ou 'ecdsa'.")
            
        else:
            clear_terminal()
            print(f"Vous avez choisi le type de clé '{key_type}'")
            return key_type

def check_key_size():
    while True:
        key_size = get_key_size()
        
        if key_size not in RULES_KEY_SIZE:
            print("Encodage non valide. Veuillez entrer '1024', '2048', '4096'.")
            
        else:
            clear_terminal()
            print(f"Vous avez encoder votre clé en {key_size} bit")
            return key_size

def check_key_name():
    key_name_valid = False
    
    while(key_name_valid is False):
        key_name_valid = True
        key_name = get_key_name()
        
        for character in RULES_KEY_NAME:
            
            for letter in key_name:
                
                if letter is character:
                    key_name_valid = False
                    break
                
        if key_name_valid is True:
            clear_terminal()
            print(f"Vous avez nommé votre clé : {key_name}")
            return key_name
        
        else:
            print("Nom invalide, eviter les caractères spéciaux tel que : '!', '@', '#', etc")
             
def generate_print_key():
    key_type = check_key_type()
    key_size = check_key_size()
    key_directory = get_key_directory()
    key_name = check_key_name()
    os.system(f"ssh-keygen -t {key_type} -b {key_size} -f {key_directory}/{key_name}")
    
    os.chdir(key_directory)
    clear_terminal()
    print(f"Voici votre clé publique : {key_name}.pub\n")
    public_key = open(f"{key_name}.pub", "r")
    print(public_key.read())
    public_key.close()
    print("Terminé")
    