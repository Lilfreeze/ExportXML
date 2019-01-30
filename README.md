# ExportXML

Script Python permettant d'extraire les pieces jointes de tous les mails d'un dossier Office Outlook 2010 (32bit),
d'extraire les données souhaitées et de les insérer dans une base de données MySQL.

# Schema table MySQL

Table MySQL :

ID | username | color | annee | jour | nbCopy | nbPage

# Config.ini

Dans le fichier de fichier de config il faut remplir avec les infos suivantes :

[DATABASE_CONFIG]
host : Nom d'hôte ou adresse IP du serveur MySQL
user : Nom d'utilisateur de la base de données
passwd : Mot de passe de l'utilisateur
database : Nom de la base de données

[OUTLOOK_CONFIG]
folder : fichier dans lequel se trouve les mails