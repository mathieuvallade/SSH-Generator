print("Quelle type de clé souhaitez vous utiliser ? : ")
key_type = input()
print(f"Vous avez choisi le type de clé {key_type}")

print("En combien de bit voulez vous encoder votre clé ? : ")
key_size = input()
print(f"Vous avez encoder votre clé en {key_size} bit")

print("Quel est votre nom de machine ? :")
key_files = input()
print(f"Votre nom de machine est {key_size}")

print("Comment souhaitez vous appeller votre clé ? : ")
key_name = input()
print(f"Votre nom de machine est {key_name}")

print("Voici la ligne de commande à utiliser :")
print(f"ssh-keygen -t {key_type} -b {key_size} -f /home/{key_files}/.ssh/{key_name}")