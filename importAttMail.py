import win32com.client
import os
import configparser

#Lecture du fichier de config
config = configparser.ConfigParser()
config.read('config.ini')

def importMail() :
    i = 1
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    root_folder = outlook.Folders.Item(i)
    
    while str(root_folder)!= config['OUTLOOK_CONFIG']['folder'] :
        i = i + 1
        root_folder = outlook.Folders.Item(i)

    historique = root_folder.Folders['Historique XML']
    fait = root_folder.Folders['Fait']
    messages = historique.Items
    
    j = 0
    for message in messages:
        j = j + 1
    

    while j != 0 :

        try :
            title = messages(j).Subject
            attachments = messages(j).Attachments
            attachment = attachments.Item(1)
            attachment.SaveASFile(os.getcwd() + '\\xml\\' + str(j) + str(attachment))
            messages(j).move(fait)
            j = j - 1
            print("Mail restant " + str(j))
        
        except:
            quit
