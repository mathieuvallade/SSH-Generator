# SSH-Generator

Le SSH Generator est un programme conçu pour simplifier la génération de clés SSH de manière sécurisée.
Ce programme invite l'utilisateur à fournir des informations sur le type de clé, la taille de la clé en bits et le nom de la clé souhaitée, puis génère la paire de clés correspondante. Il affiche ensuite la clé publique générée pour permettre à l'utilisateur de l'utiliser dans ses dépôts Git ou d'autres applications nécessitant des clés SSH.

## Fonctionnalités :

Choix du Type de Clé : L'utilisateur est invité à sélectionner le type de clé SSH parmi les options disponibles, telles que RSA, DSA, ECDSA ou ED25519.
Taille de la Clé : L'utilisateur peut spécifier la taille de la clé en bits, offrant une flexibilité pour des niveaux de sécurité variés.
Nom de la Clé : L'utilisateur peut attribuer un nom significatif à sa clé pour une meilleure gestion.
Génération de Clés : Le programme utilise les informations fournies par l'utilisateur pour générer une paire de clés privée/publique.
Affichage de la Clé Publique : Une fois la génération de la paire de clés terminée, le programme affiche la clé publique correspondante, prête à être utilisée dans les dépôts Git ou autres services compatibles avec SSH.
Utilisation :
L'utilisateur exécute le programme depuis un terminal. Le script guide l'utilisateur tout au long du processus, demandant le type de clé, la taille en bits et le nom de la clé. Après la génération des clés, le programme affiche la clé publique, prête à être copiée et utilisée.

## Objectif :

L'objectif principal de ce programme est de simplifier et de rendre plus conviviale la création de clés SSH pour les utilisateurs, en automatisant le processus de génération tout en offrant des options personnalisées pour répondre aux besoins de sécurité spécifiques.

## Technologies :

Ce programme peut être développé en utilisant des langages tels que Python, Bash, ou tout autre langage de script adapté à l'interaction en ligne de commande.

## Note : 

Il est essentiel de souligner l'importance de la sécurisation et de la gestion appropriée des clés générées pour éviter tout accès non autorisé à des systèmes ou des données sensibles.