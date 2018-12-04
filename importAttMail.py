import win32com.client
import os

def importMail() :
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    root_folder = outlook.Folders.Item(4)
    print(root_folder)
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
        
        except:
            quit
