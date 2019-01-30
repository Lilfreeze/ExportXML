import os
import shutil
import pymysql.cursors
import sys
import configparser
from importAttMail import importMail
from lxml import etree
from datetime import datetime

#Lecture du fichier de config
config = configparser.ConfigParser()
config.read('config.ini')

#Création des dossiers
os.makedirs("./xml/", exist_ok=True)
os.makedirs("./temp/", exist_ok=True)
os.makedirs("./check/", exist_ok=True)
os.makedirs("./log/", exist_ok=True)

#Ouverture du fichier de log
now = datetime.now()
fichierLog = open("./log/log" + str(now.year) + str(now.month) + str(now.day) + ".txt", "a", encoding = 'utf8')

#Ouverture connexion MySQL : Ajouter le nom d' hôte ou IP, le user, le mot de passe et la base de donnees
try:
    connection = pymysql.connect(host=config['DATABASE_CONFIG']['host'],
                                 user=config['DATABASE_CONFIG']['user'],
                                 passwd=config['DATABASE_CONFIG']['passwd'],
                                 database=config['DATABASE_CONFIG']['database'])
except:
    print("La connexion a MySQL a échoué")
    fichierLog.write("La connexion a MySQL a échoue\n")
    fichierLog.close()
    sys.exit()
else:
    print("Connexion MySQL effectué")
    fichierLog.write("Connexion MySQL effectué\n")
    
importMail()

for fichiers in os.listdir('./xml/'):
    
    #Declaration des fichiers qui vont être ouvert
    fichier = open("./xml/" + fichiers,  "r")
    fichier2 = open("./temp/temp.xml", "a", encoding = 'utf8')

    #Lecture des ligne de "fichier"
    lignes = fichier.readlines()

    #Parcours de "fichier" ligne par ligne et remplacement de "kmloginfo:" par ""
    for ligne in lignes:
        ligneFinale = ligne.replace("kmloginfo:","")
        fichier2.write(ligneFinale)

    #Fermeture de fichier et fichier2
    fichier.close()
    #Fermeture de fichier2
    fichier2.close()
    #Deplacement des fichier dans "./xml/" vers "./check/" un par un
    shutil.move('./xml/' + fichiers, './check/' + str(now.year) + str(now.month) + str(now.day) + "_" + fichiers)


    #Parse du fichier temp.xml
    tree = etree.parse("./temp/temp.xml")
    racine = tree.getroot()

    for noeud in tree.xpath('//export_job_logResponse/export_job_log'):
        for info in noeud.iter('print_job_log'):
            cur = connection.cursor()
            donnees = (info.xpath("common/job_number")[0].text, info.xpath("common/user_name")[0].text, info.xpath("detail/print_color_mode")[0].text, info.xpath("common/start_time/year")[0].text, info.xpath("common/start_time/yday")[0].text, info.xpath("detail/complete_copies")[0].text, info.xpath("detail/complete_pages")[0].text)
            try:
                cur.execute("""INSERT INTO export VALUES (%s,%s,%s,%s,%s,%s,%s)""", donnees)
            except pymysql.err.IntegrityError :
                print("L'ID existe deja dans la table")
                fichierLog.write("L'ID" + info.xpath("common/job_number")[0].text + " existe deja dans la table MySQL. Cet ID de trouve dans le fichier : \"" + fichiers + "\"\n")
            
    #Suppression du fichier "./temp/temp.xml"
    os.remove("./temp/temp.xml")
    #Log le fichier finit
    fichierLog.write(fichier + " : OK")

connection.commit()
cur.close()

#Suppression des dossiers
try:
    os.rmdir("./xml/")
    os.rmdir("./temp/")
except PermissionError :
    print("Impossible de supprimé le dossier : Accès refusé")
    fichierLog.write("Impossible de supprimé le dossier : Accès refusé")

#Fermeture connexion MySQL
connection.close()

#Fermeture du fichier de log
fichierLog.close()
