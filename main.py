import os

key_type = None
key_size = None
key_name = None

correct_key_type = ['rsa', 'dsa', 'ecdsa']
correct_key_size = ['64', '128', '256', '512', '1024', '2048', '4096']

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
    
def get_key_name():
    print("Comment souhaitez vous appeller votre clé ? : ")
    key_name = input()
    return key_name

def check_key_type():
    while True:
        key_type = get_key_type()
        
        if key_type not in correct_key_type:
            print("Type de clé non valide. Veuillez entrer 'rsa', 'dsa' ou 'ecdsa'.")
            
        else:
            break
    clear_terminal()
    print(f"Vous avez choisi le type de clé '{key_type}'")

def check_key_size():
    while True:
        key_size = get_key_size()
        
        if key_size not in correct_key_size:
            print("Encodage non valide. Veuillez entrer '64', '128', '256', '512', '1024', '2048', '4096'.")
            
        else:
            break
    clear_terminal()
    print(f"Vous avez encoder votre clé en {key_size} bit")
    
def print_key():
    print("Voici la ligne de commande à utiliser :")
    print(f"ssh-keygen -t {key_type} -b {key_size} -f /home/freezorce/.ssh/{key_name}")

clear_terminal()
check_key_type()
check_key_size()
key_name = get_key_name()
print(key_name)
clear_terminal()
print_key()