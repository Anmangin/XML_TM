
import xml.etree.ElementTree as ET
import re
import sys     
import os
import json

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


logprint=False
unic_form=True

DICO={}

Pathin = sys.argv[1]
file_t = os.path.basename(Pathin)
file=file_t.replace('.xml', '')


directory = os.path.dirname(Pathin)
path= os.path.dirname(os.path.dirname(directory)) + r"\OUTFILE"


config_path=os.path.dirname(os.path.dirname(directory)) + "/config.json"
data = lire_et_trier_donnees(Pathin,config_path)

version=data["version"]
        #content+=f"# Version de TB pour ce fichier : {version}  \n")

with open(f"{os.path.dirname(directory)}/VersionTM.txt", "r", encoding="utf-8") as fichier:
    ACTversion = fichier.read()


checks,DICO = exporter_donnees_markdown_eCRF(data,False)

json_output = json.dumps(checks, indent=4)
with open( f"{path}/JSON/{file}_check.json" , 'w', encoding='utf-8') as f:
        f.write(json_output)
json_DICO = json.dumps(DICO, indent=4)
with open( f"{path}/JSON/{file}_dico.json" , 'w', encoding='utf-8') as f:
        f.write(json_DICO)
JSON_FUNC = json.dumps(data["ProScriptFunction"], indent=4)
with open( f"{path}/JSON/{file}_function.json" , 'w', encoding='utf-8') as f:
        f.write(JSON_FUNC)


             
