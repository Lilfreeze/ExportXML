import os
import shutil
from importAttMail import importMail
from lxml import etree

#Création des dossiers
os.mkdir("./xml/")
os.mkdir("./temp/")
os.mkdir("./export/")
os.mkdir("./check/")

importMail()

for fichiers in os.listdir('./xml/'):
    print(fichiers)
    
    #Declaration des fichiers qui vont être ouvert
    fichier = open("./xml/" + fichiers,  "r")
    fichier2 = open("./temp/temp.xml", "w", encoding = 'utf8')

    #Lecture des ligne de "fichier"
    lignes = fichier.readlines()

    #Parcours de "fichier" ligne par ligne et remplacement de "kmloginfo:" par ""
    for ligne in lignes:
        ligneFinale = ligne.replace("kmloginfo:","")
        fichier2.write(ligneFinale)

    #Fermeture de fichier et fichier2
    fichier.close()
    fichier2.close()

    #Parse du fichier temp.xml
    tree = etree.parse("./temp/temp.xml")
    racine = tree.getroot()

    #Déclaration d'un nouveau fichier
    fichier3 = open("./export/export.txt", "a")

    #Ecriture dans fichier 3 des balises : job_number, user_name, print_color_mode
    for noeud in tree.xpath('//export_job_logResponse/export_job_log'):
        for info in noeud.iter('print_job_log'):
            infoFinale = info.xpath("common/job_number")[0].text
            fichier3.write(str(infoFinale) + "\n")
            infoFinale = info.xpath("common/user_name")[0].text
            fichier3.write(str(infoFinale) + "\n")
            infoFinale = info.xpath("detail/print_color_mode")[0].text
            fichier3.write(str(infoFinale) + "\n")
            infoFinale = info.xpath("common/start_time/year")[0].text
            fichier3.write(str(infoFinale) + "-")
            infoFinale = info.xpath("common/start_time/yday")[0].text
            fichier3.write(str(infoFinale) + "\n")
    
    #Fermeture de fichier3
    fichier3.close()
    #Deplacement des fichier dans "./xml/" vers "./check/" un par un
    shutil.move('./xml/' + fichiers, './check/')
    #Suppression du fichier "./temp/temp.xml"
    os.remove("./temp/temp.xml")


#Suppression des dossiers
os.remove("./xml/")
os.remove("./temp/")
