import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

print("Veuillez entrer le type de clef que vous souhaitez utiliser : ")
key_type = input()

while True:
    print("Veuillez entrer le type de clé que vous souhaitez utiliser : ")
    key_type = input()

    if key_type not in ['rsa', 'dsa', 'ecdsa']:
        print("Type de clé non valide. Veuillez entrer 'rsa', 'dsa' ou 'ecdsa'.")
    else:
        break

print(f"Vous avez choisi le type de clé : {key_type}")

print("Veuillez entrer en chiffre en combien de bit vous souhaitez encoder votre clef : ")
key_size = input()
print("Veuillez entrer le nom que vous souhaitez donner à votre clef : ")
key_name = input()

print("Voici la ligne de commande à utiliser :")
print(f"ssh-keygen -t {key_type} -b {key_size} -f /home/freezorce/.ssh/{key_name}")
