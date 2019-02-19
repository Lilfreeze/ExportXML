# ExportXML

Script Python permettant d'extraire les pieces jointes de tous les mails d'un dossier Office Outlook 2010 (32bit),
d'extraire les données souhaitées et de les insérer dans une base de données MySQL.

# Fonction importAttMail

Cette partie du code ouvre outlook en local sur le poste.
Se connecte au dossier souhaité ("folder" dans config.ini).
Puis exporte toutes les pièces-jointes des mails, et les transfert vers un autre dossier.

# Execution

C'est le fichier exportXML.py qui est à éxecuter, il créera quelques dossiers (xml,temp,check et log).
Il ne restera que check et log a la fin de l'execution.

# Config.ini

Dans le fichier de fichier de config il faut remplir avec les infos suivantes :

[DATABASE_CONFIG]

host : Nom d'hôte ou adresse IP du serveur MySQL

user : Nom d'utilisateur de la base de données

passwd : Mot de passe de l'utilisateur

database : Nom de la base de données

[OUTLOOK_CONFIG]

folder : fichier dans lequel se trouve les mails

# Schema table MySQL

Table MySQL :

ID | username | color | annee | jour | nbCopy | nbPage
