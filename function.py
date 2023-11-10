from constant import rules_key_type, rules_key_size, rules_key_name
import os
key_type = None
key_size = None
key_file = None
key_name = None

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

def get_key_file():
    print("Veuillez entrer votre nom d'utilisateur : ")
    key_file = input()
    return key_file
    
def get_key_name():
    print("Comment souhaitez vous appeller votre clé ? : ")
    key_name = input()
    return key_name

def check_key_type():
    while True:
        key_type = get_key_type()
        
        if key_type not in rules_key_type:
            print("Type de clé non valide. Veuillez entrer 'rsa', 'dsa' ou 'ecdsa'.")
            
        else:
            break
    clear_terminal()
    print(f"Vous avez choisi le type de clé '{key_type}'")
    return key_type

def check_key_size():
    while True:
        key_size = get_key_size()
        
        if key_size not in rules_key_size:
            print("Encodage non valide. Veuillez entrer '1024', '2048', '4096'.")
            
        else:
            break
    clear_terminal()
    print(f"Vous avez encoder votre clé en {key_size} bit")
    return key_size

def check_key_file():
    while True:
        key_file = get_key_file()
        print("Veuillez confirmer votre nom d'utilisateur : ")
        key_file_valid = input()
        
        if key_file != key_file_valid:
            print("Les noms d'utilisateur ne correspondent pas. Veuillez réessayer.")
            
        else:
            print(f"Votre nom d'utilisateur est {key_file}")
            return key_file
            break

def check_key_name():
    key_name_valid = False
    
    while(key_name_valid is False):
        key_name_valid = True
        key_name = get_key_name()
        
        for character in rules_key_name:
            
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
             
def print_key():
    key_type = check_key_type()
    key_size = check_key_size()
    key_file = check_key_file()
    key_name = check_key_name()
    print("Voici la ligne de commande à utiliser :")
    print(f"ssh-keygen -t {key_type} -b {key_size} -f /home/{key_file}/.ssh/{key_name}")