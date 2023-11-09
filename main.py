import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

while True:
    print("Quelle type de clé souhaitez vous utiliser ? : ")
    key_type = input()

    if key_type not in ['rsa', 'dsa', 'ecdsa']:
        print("Type de clé non valide. Veuillez entrer 'rsa', 'dsa' ou 'ecdsa'.")
    else:
        break
    
print(f"Vous avez choisi le type de clé {key_type}")

while True:
    print("En combien de bit voulez vous encoder votre clé ? : ")
    key_size = input()

    if key_size not in ['64', '128', '256', '512', '1024', '2048', '4096']:
        print("Encodage non valide. Veuillez entrer '64', '128', '256', '512', '1024', '2048', '4096'.")
    else:
        break

print(f"Vous avez encoder votre clé en {key_size} bit")

print("Comment souhaitez vous appeller votre clé ? : ")
key_name = input()

print("Voici la ligne de commande à utiliser :")
print(f"ssh-keygen -t {key_type} -b {key_size} -f /home/freezorce/.ssh/{key_name}")
