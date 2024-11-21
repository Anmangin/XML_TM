
import xml.etree.ElementTree as ET
import re
import sys     
import os
import json
def remove_details_tags(text):
    # Utilisation de l'expression régulière pour supprimer les balises <details>...</details>
    cleaned_text = re.sub(r'<(th|td)\s+class=["\']check["\'][^>]*>.*?<!--\$htmlbalise-->.', '', text, flags=re.DOTALL)
    # cleaned_text = re.sub(r'<(th|td)\s+class=["\']check["\'][^>]*>.*?<!--\$htmlbalise-->.*?</\1>', '', text, flags=re.DOTALL)


    return cleaned_text

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

    # Ajouter le champ "Display" pour ProCodeList
    data["ProCodeList"] = ajouter_display_pro_codelist(data)

    # Ajouter le champ "Display" pour ProItem
    data["ProItem"] = ajouter_display_pro_item(data)

    return data


def ajouter_display_pro_codelist(data):
    """Ajoute un champ 'Display' pour les ProCodeList."""
    for key, value in data["ProCodeList"].items():
        # Filtrer les items associés à la ProCodeList actuelle
        filtered_items = {k: v for k, v in data["ProCodeListItem"].items() if v["ProCodeListGuid"] == key}

        # Construire la chaîne de caractères pour le champ Display
        if len(filtered_items) < 15:
            rep = "<br>".join(f"🔘 {item['Value']} - <b>{item['Caption']}</b>" for item in filtered_items.values())
        else:
            rep = "🔘 Radio bouton trop long"

        # Ajouter le champ Display
        data["ProCodeList"][key]["Display"] = rep

    return data["ProCodeList"]


def ajouter_display_pro_item(data):
    """Ajoute un champ 'Display' pour les ProItem."""
    for key, value in data["ProItem"].items():
            if value["ProDataTypeId"] == "5":
                rep = "📅 DD/MM/YYYY"
            else:
                rep = f"{value['SasType']} - {value['MaxLength']}"

            # Ajouter le champ Display
            if rep :data["ProItem"][key]["Display"] = rep


    return data["ProItem"]

# Appel de la fonction

def find_arbo(TBNode):
            if TBNode["ParentTBNodeId"]=="6":source="Fiche"
            elif TBNode["ParentTBNodeId"]=="7":source="groupe"
            elif TBNode["ParentTBNodeId"]=="8":source="item"
            elif TBNode["ParentTBNodeId"]=="9":source="codelist"
            elif int(TBNode["ParentTBNodeId"]) < 10 : source="unknown"
            else : source="unknown"
            return source
    




def exporter_donnees_markdown_eCRF(data,pathout,file,ACTversion):

        
 
        content=f"<body>\n\n\n"

        
        if ACTversion != version :
             content+=f"# Fichier non compatible avec la version en cours de TM : actuel:{OngoingVer}, version du fichier : {version}  \n"
             
        


        errortitle=0      
        for  PVkey,TBNode in data["TBNode"].items():    
            if TBNode["TBNodeId"] is not None  :
                TBNodeId=TBNode["TBNodeId"]
                Caption=TBNode["Caption"]
                listItm=filtrer_par_cle( data["TBNode"],"ParentTBNodeId",TBNodeId)
                if len(listItm)==0 :
                    if errortitle==0:
                        errortitle+=1
                        content+=f"# ERREUR DANS LES DOSSIERS DU FICHIER  \n"
                        content+=f"{find_arbo(TBNode)}/{Caption} est vide TBNodeId:{TBNodeId}\n"

        # Parcourir les données
        print(len(data["ProPatientVisit"]), "Patients visit")
        if len(data["ProPatientVisit"])==0 : 
            if errortitle==0:
                        errortitle+=1
                        content+=f"# ERREUR DANS LES DOSSIERS DU FICHIER  \n"
            content+=f"Pas d'arborescence patient ! \n"
        for  PVkey,PatientVisit in data["ProPatientVisit"].items():
            ProVisitGuid=PatientVisit["ProVisitGuid"]
            V_description = data["ProVisit"][ProVisitGuid]["Description"]
            V_OrderNo=PatientVisit["OrderNo"]
            if not unic_form: 
                content+=f"<h1> {V_description} </h1> \n"
                print("écriture de #",V_description)



            ProVisitForm=filtrer_par_cle( data["ProVisitForm"],"ProVisitGuid",ProVisitGuid)
           
            for  VFkey,VisitForm in ProVisitForm.items():
                ProFormGuid=VisitForm.get("ProFormGuid")
                written=data["ProForm"][ProFormGuid].get("written", False)
                if written and unic_form: continue    
                F_OrderNo=VisitForm["OrderNo"]
                F_description=data["ProForm"][ProFormGuid]["Description"]
                data["ProForm"][ProFormGuid]["written"]=True
                content+=f"<h2> {F_description}  </h2>\n"
                print("écriture de ##",F_description)
                ListVisit=filtrer_par_cle( data["ProVisitForm"],"ProFormGuid",ProFormGuid)

                if unic_form: # cas ou on imprime qu'une version de la fiche, alors on liste les visites ou elle apparait.
                    Li="Liste des visites avec cette fiches :"
                    for  VFkey,LV in ListVisit.items():
                        Vgui_temp=LV["ProVisitGuid"]
                        V_description_temp = data["ProVisit"][Vgui_temp]["Description"]
                        Li+= f"{V_description_temp}"
                    content+=f"{Li} \n\n"

                    









                ProFormGroup=filtrer_par_cle( data["ProFormGroup"],"ProFormGuid",ProFormGuid)
                for  key,FormGroup in ProFormGroup.items():
                    ProGroupGuid=FormGroup["ProGroupGuid"]
                    G_description=data["ProGroup"][ProGroupGuid]["Caption"]
                    content+=f"<h3> {G_description} </h3> \n\n"
                    


                    ProGroupItem=filtrer_par_cle( data["ProGroupItem"],"ProGroupGuid",ProGroupGuid)
                    print("écriture de ###",G_description, "(", len(ProGroupItem),")")



                    content+="<table style='width:100%;'>\n"
                    content+="<tr>\n"
                    content+="<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>\n"
                    content+="<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->\n"
                    content+="<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>\n"
                    content+="<th style='width:50px; text-align:center;'><strong>Sas</strong></th>\n"
                    content+="</tr>\n"
                    content+="<tr>\n"


                    for  GI_key,GroupItem in ProGroupItem.items():
                        I_OrderNo=GroupItem["OrderNo"]
                        ProItemGuid=GroupItem.get("ProItemGuid")
                        I_description=data["ProItem"][ProItemGuid]["Description"]
                        i_SasName=data["ProItem"][ProItemGuid]["SasName"]
                        ProCodeListGuid=data["ProItem"][ProItemGuid]["ProCodeListGuid"]
                        Hidden=data["ProItem"][ProItemGuid]["Hidden"]
                        Disabled=data["ProItem"][ProItemGuid]["Disabled"]
                        ReadOnly=data["ProItem"][ProItemGuid]["ReadOnly"]
                        rep=""
                        rep=data["ProItem"][ProItemGuid]["Display"]
                        if ProCodeListGuid :rep=data["ProCodeList"][ProCodeListGuid]["Display"]

                        if Hidden=="True": Hidden="👻"
                        else: Hidden=""
                        if ReadOnly=="True": ReadOnly="🔒"
                        else: ReadOnly=""
                        print( I_description)
                        
                        ProEdit=filtrer_par_cle( data["ProEdit"],"ProItemGuid",ProItemGuid)

                        i=0
                        Message= ""               
                        for  key,Edit in ProEdit.items():
                            if (Edit["ProItemGuid"] == ProItemGuid) and (Edit["TargetProFormGuid"]==ProFormGuid or Edit["TargetProFormGuid"] is None) and (Edit["TargetProGroupGuid"]==ProGroupGuid or Edit["TargetProGroupGuid"] is None)  :
                                i+=1
                                EditACtion= Edit["ProEditActionId"]
                                if EditACtion=="1":EditACtion="Valid"
                                elif EditACtion=="3":EditACtion="Enabled"
                                elif EditACtion=="6":EditACtion="Hidden"
                                elif EditACtion=="10":EditACtion="DVA"
                                elif EditACtion=="11":EditACtion="Email"
                                elif EditACtion=="9":EditACtion="DVC"
                                elif EditACtion=="23":EditACtion="Dynamic codelist filter"
                                msg=Edit["Message"]
                                chk=Edit["ActionExpression"]
                                DTE = Edit['DataExpression']
                                path=Edit["TargetPath"]

                                Message+=f"<tr><td> {EditACtion}:{path}</td> </tr>"
                                Message+=f"<tr> <td> <pre><code class='javascript'>#Action Expression \n{chk} \n#data Expression \n{DTE} \n</code></pre> </td>"
                                Message+=f"<td> {msg}</td> </tr>"

                        Message+="</table></details>"
                        if i==0:Message=""
                        else: Message= f"<details> <summary>{i} EditCheck </summary><table>" + Message
                            
                        content+=" <tr> \n"                       
                        content+=            f" <td style='width:600px; text-align:left;'> {I_description}</td>\n" 
                        content+=             f" <td class='check' style='width:600px; text-align:left;'>  {Message} </td> <!--$htmlbalise--> \n\n" 
                        content+=             f" <td style='width:300px; text-align:center;'> {rep} </td> \n"
                        content+=            f"<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> {Hidden}{ReadOnly}{i_SasName} </b></td> \n" 
                        content+=" </tr> \n"            
                        print("écriture de ",I_description)
                        

                    content+="</table>\n\n"
                content+=f"<pre><br clear=all style='mso-special-character:line-break;page-break-before:always'></pre>"
        content+=f"</body>\n\n\n"
        with open( f"{pathout}/HTML/{file}.html" , 'w', encoding='utf-8') as f:
            htmlcontent= f"    <head>   \n    <meta charset='UTF-8'>    \n   <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n <title>test fiche</title> \n   <link rel='stylesheet' href='style.css'> \n </head> \n\n" + remove_details_tags(content)
            f.write(htmlcontent)
        with open( f"{pathout}/MD/{file}.md" , 'w', encoding='utf-8') as f:
            f.write(content)


        print(f"fin d'écriture dans {pathout}")



unic_form=True


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


exporter_donnees_markdown_eCRF(data,path,file,ACTversion)
