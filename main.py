import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

print("Veuillez entrer le type de clef que vous souhaitez utiliser : ")
key_type = input()
print("Veuillez entrer en chiffre en combien de bit vous souhaitez encoder votre clef : ")
key_size = input()
print("Veuillez entrer le nom que vous souhaitez donner à votre clef : ")
key_name = input()

print("Voici la ligne de commande à utiliser :\n")
print(f"ssh-keygen -t {key_type} -b {key_size} -f /home/freezorce/.ssh/{key_name}")

