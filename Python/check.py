
import xml.etree.ElementTree as ET
import re
import sys     
import os
import json
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox



# Paramètres globaux
logprint = False
unic_form = True
DICO = {}


def Get_objt(root, racine, keyname, fields):
        ProForm = {}
        for FWAW in root.iter(racine):
            key = FWAW.findtext(keyname)
            if key:  # Vérifie que la clé existe
                ProForm[key] = {field: FWAW.findtext(field) for field in fields}
        return ProForm

def filtrer_par_cle(dictionnaire, champ, valeur):
    return {key: val for key, val in dictionnaire.items() if val.get(champ) == valeur}


def lire_et_trier_donnees(pathfileXML, config_path='config.json'):
    print(f"lecture des données de {pathfileXML}")
    # Charger la configuration
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Charger et analyser l'XML
    tree = ET.parse(pathfileXML)
    root = tree.getroot()
    version = root.attrib.get('ver')
    data = {"version": version}

    # Extraire et transformer les données à partir du fichier XML selon la config
    for key, params in config.items():
        racine = params["racine"]
        keyname = params["keyname"]
        fields = params["fields"]
        data[key] = Get_objt(root, racine, keyname, fields)

    # Trier les clés spécifiques
    trier_cles = ["ProPatientVisit", "ProVisitForm", "ProFormGroup", "ProGroupItem", "ProCodeListItem"]
    for key in trier_cles:
        if key in data:
            data[key] = dict(sorted(data[key].items(), key=lambda item: int(item[1].get("OrderNo", 0))))


    return data



def get_check(data,ProItemGuid,ProGroupGuid,ProFormGuid,i_SasName,F_SasName,checks):
    """genere le message pour les editcheck"""
    ProEdit=filtrer_par_cle( data,"ProItemGuid",ProItemGuid)
    for  key,Edit in ProEdit.items():
        if ((Edit["ProItemGuid"] == ProItemGuid) and (Edit["TargetProFormGuid"]==ProFormGuid or Edit["TargetProFormGuid"] is None) and (Edit["TargetProGroupGuid"]==ProGroupGuid or Edit["TargetProGroupGuid"] is None) and Edit["ProEditActionId"]=="1") :
                check={ 
                    "ActionExpression": Edit["ActionExpression"]  ,
                    "Message":Edit["Message"],
                    "path":Edit["TargetPath"] ,
                    'i_SasName':i_SasName,
                    'F_SasName':F_SasName                               
                    }
                checks.append(check)
    return checks



def exporter_donnees_markdown_eCRF(data,display_Edit=True):

        checks=[]
   

        if logprint:print(len(data["ProPatientVisit"]), "Patients visit")
        for  PVkey,PatientVisit in data["ProPatientVisit"].items():



            # Ecriture des variables nécéssaire pour l'affichage
            
            ProVisitGuid        =PatientVisit["ProVisitGuid"]
            V_description       =data["ProVisit"][ProVisitGuid]["Description"]
            V_Caption           =data["ProVisit"][ProVisitGuid]["Caption"]
            V_OrderNo           =PatientVisit["OrderNo"]

            if not unic_form: # si on fait un CRF complet, pas la peine de rajouter la liste des visites pour chaque fiche.
                # content+=f"<h1> {V_description} </h1> \n"
                if logprint:("écriture de #",V_description)



            ProVisitForm=filtrer_par_cle( data["ProVisitForm"],"ProVisitGuid",ProVisitGuid)
           
            for  VFkey,VisitForm in ProVisitForm.items():
                ProFormGuid=VisitForm.get("ProFormGuid")
                written=data["ProForm"][ProFormGuid].get("written", False)
                if written and unic_form: continue    

                # Ecriture des variables nécéssaire pour l'affichage
                F_OrderNo           =VisitForm["OrderNo"]
                F_description       =data["ProForm"][ProFormGuid]["Description"]
                F_SasName           =data["ProForm"][ProFormGuid]["SasName"]
                F_Caption           =data["ProForm"][ProFormGuid]["Caption"]


                data["ProForm"][ProFormGuid]["written"]=True
                # content+=f"<h2> {F_description}  </h2>\n"
                if logprint:print("écriture de ##",F_description)


                ProFormGroup=filtrer_par_cle( data["ProFormGroup"],"ProFormGuid",ProFormGuid)
                for  key,FormGroup in ProFormGroup.items():
                    # Ecriture des variables nécéssaire pour l'affichage
                    ProGroupGuid        =FormGroup["ProGroupGuid"]
                    G_description       =data["ProGroup"][ProGroupGuid]["Caption"]
                    G_Caption           =data["ProGroup"][ProGroupGuid]["Caption"]



                    ProGroupItem=filtrer_par_cle( data["ProGroupItem"],"ProGroupGuid",ProGroupGuid)
                    if logprint:print("écriture de ###",G_description, "(", len(ProGroupItem),")")
                    for  GI_key,GroupItem in ProGroupItem.items():
                        # Ecriture des variables nécéssaire pour l'affichage
                        ProItemGuid         =GroupItem.get("ProItemGuid")
                        i_SasName           =data["ProItem"][ProItemGuid]["SasName"]
                        I_Caption           =data["ProItem"][ProItemGuid]["Caption"]
                    
                      
                        DICO[f"[{V_Caption}][{F_Caption}][{G_Caption}][{I_Caption}] "] = {

                            'i_SasName':i_SasName,
                            'F_SasName':F_SasName     
                        }
                        checks=get_check(data["ProEdit"],ProItemGuid,ProGroupGuid,ProFormGuid,i_SasName,F_SasName,checks)

        return checks,DICO
        




        if logprint:print(f"fin d'écriture dans {pathout}")




def get_path_input():
    """Récupère le chemin du fichier à partir des arguments ou via un sélecteur de fichier."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return askopenfilename()

def ensure_directories(base_path, sub_dirs=None):
    """Crée un dossier de base et les sous-dossiers nécessaires s'ils n'existent pas."""
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    if sub_dirs:
        for sub_dir in sub_dirs:
            full_path = os.path.join(base_path, sub_dir)
            if not os.path.exists(full_path):
                os.makedirs(full_path)

def confirm_execution(path):
    """Demande confirmation à l'utilisateur pour continuer l'exécution."""
    return messagebox.askyesno("Confirmation", f"Path : {path}\nVoulez-vous continuer ?")

def save_json(data, path, filename):
    """Enregistre les données en JSON dans le chemin spécifié."""
    with open(os.path.join(path, filename), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def main():
    # Initialisation
    execution_path = os.getcwd()
    Pathin = get_path_input()
    file_name = os.path.basename(Pathin).replace('.xml', '')
    directory = os.path.dirname(Pathin)
    output_path = os.path.join(execution_path, "OUTFILE")

    # Gestion des chemins locaux
    if len(sys.argv) <= 1:
        output_path += "_LOCAL"
        ensure_directories(output_path, sub_dirs=["JSON"])
        if not confirm_execution(output_path):
            return

    # Lecture des données et configuration
    config_path = os.path.join(execution_path,"Python", "config.json")
    data = lire_et_trier_donnees(Pathin, config_path)
   
    # Export des données
    checks, DICO = exporter_donnees_markdown_eCRF(data, False)
    
    if len(checks)>0:save_json(checks, os.path.join(output_path, "JSON"), f"{file_name}_check.json")
    else: print("Liste des checks vide!")
    if len(DICO)>0:save_json(DICO, os.path.join(output_path, "JSON"), f"{file_name}_dico.json")
    else: print("DICO vide!")
    if len(data.get("ProScriptFunction", {}))>0:save_json(data.get("ProScriptFunction", {}), os.path.join(output_path, "JSON"), f"{file_name}_function.json")
    else: print("pas de fonction trouvé!")

if __name__ == "__main__":
    main()