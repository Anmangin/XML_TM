import xml.etree.ElementTree as ET
import re
import sys     
import os
import json
# from bs4 import BeautifulSoup
# from docx import Document
# from docx.shared import Pt
# from docx.enum.text import WD_ALIGN_PARAGRAPH  # Assurez-vous d'ajouter cette importation
# from docx.enum.text import WD_BREAK  # Importation pour les sauts de page

# from docx.oxml import OxmlElement
# from docx.oxml.ns import qn

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from pathlib import Path

# Chemin vers le fichier HTML
chemin_html = f"{os.getcwd()}/Python/Template_CRF.html"

# Lire le contenu du fichier HTML

contenu_html = Path(chemin_html).read_text(encoding='utf-8')


# Paramètres globaux
logprint = False
unic_form = True
DICO = {}


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





def lire_et_trier_donnees(pathfileXML, config_path='Python/config.json'):
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





            # Partie du la nature de la var
            if value["Hidden"]=="True": Hidden="👻"
            else: Hidden=""
            if value["ReadOnly"]=="True": ReadOnly="🔒"
            else: ReadOnly=""
            value["Status"]= Hidden + ReadOnly


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
    




def get_message(data,ProItemGuid,ProGroupGuid,ProFormGuid):
    """genere le message pour les editcheck"""
    Message=""
    i=0
    ProEdit=filtrer_par_cle( data,"ProItemGuid",ProItemGuid)
    for  key,Edit in ProEdit.items():
        if (Edit["ProItemGuid"] == ProItemGuid) and (Edit["TargetProFormGuid"]==ProFormGuid or Edit["TargetProFormGuid"] is None) and (Edit["TargetProGroupGuid"]==ProGroupGuid or Edit["TargetProGroupGuid"] is None)  :
            i+=1


            EditACtion= Edit["ProEditActionId"]
            if   EditACtion =="1"           :EditACtion="Valid"
            elif EditACtion =="3"           :EditACtion="Enabled"
            elif EditACtion =="6"           :EditACtion="Hidden"
            elif EditACtion =="10"          :EditACtion="DVA"
            elif EditACtion =="11"          :EditACtion="Email"
            elif EditACtion =="9"           :EditACtion="DVC"
            elif EditACtion =="23"          :EditACtion="Dynamic codelist filter"
            msg=Edit["Message"]
            chk=Edit["ActionExpression"]
            DTE=Edit['DataExpression']
            path=Edit["TargetPath"]

            Message+=f"<tr><td> {EditACtion}:{path}</td> </tr>"
            Message+=f"<tr> <td> <pre><code class='javascript'>#Action Expression \n{chk} \n#data Expression \n{DTE} \n</code></pre> </td>"
            Message+=f"<td> {msg}</td> </tr>"


    Message+="</table></details>"
    if i==0:Message=""
    else: Message= f"<details> <summary>{i} EditCheck </summary><table>" + Message


    return Message




def exporter_donnees_markdown_eCRF(data,ACTversion,display_Edit=True):
        JSON_EXPORT = {}
        doc =""
        # doc = Document()
        content=f"<body>\n\n\n"




        content+="<!-- Sidebar -->\n"
        content+="<div class=""sidebar"" id=""sidebar"">\n"
        content+="<h3>Table des matières</h3>\n"
        content+="<div id=""sidebar-links""></div>\n"
        content+="</div> \n<div class=""content""> \n"

        
        # if ACTversion != version :
        #      content+=f"# Fichier non compatible avec la version en cours de TM : actuel:{OngoingVer}, version du fichier : {version}  \n"
        #      doc.add_heading(f"Fichier non compatible avec la version en cours de TM : actuel:{OngoingVer}, version du fichier : {version}", level=1)
             
        
        if logprint:print(len(data["ProPatientVisit"]), "Patients visit")
        if len(data["ProPatientVisit"])==0 : 
            content+=f"# ERREUR DANS LES DOSSIERS DU FICHIER  \n"
            content+=f"Pas d'arborescence patient ! \n"
            # doc.add_heading("ERREUR DANS LES DOSSIERS DU FICHIER", level=1)
            # doc.add_paragraph("Pas d'arborescence patient !")

        for  PVkey,PatientVisit in data["ProPatientVisit"].items():



            # Ecriture des variables nécéssaire pour l'affichage
            ProVisitGuid        =PatientVisit["ProVisitGuid"]
            V_description       =data["ProVisit"][ProVisitGuid]["Description"]
            V_Caption           =data["ProVisit"][ProVisitGuid]["Caption"]
            V_OrderNo           =PatientVisit["OrderNo"]



            if not unic_form: # si on fait un CRF complet, pas la peine de rajouter la liste des visites pour chaque fiche.
                content+=f"<section id='{PVkey}' data-type='visit'  data-parent='{PVkey}' data-label='{V_description}'>\n"
                content+=f"<h1> {V_description} </h1> \n"
                # doc.add_heading(f"{V_description}", level=2)
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
                

                content+=f"<section id='{VFkey}' data-parent='{PVkey}' data-type='form' data-label='{F_description}'>\n"
                content+=f"<h2> {F_description} </h2>\n"
                # doc.add_heading(f"{F_description}", level=3)
                if logprint:print("écriture de ##",F_description)

                if unic_form:# cas ou on imprime qu'une version de la fiche, alors on liste les visites ou elle apparait.
                    ListVisit=filtrer_par_cle( data["ProVisitForm"],"ProFormGuid",ProFormGuid)
                    ListVisit= dict(sorted(ListVisit.items(), key=lambda item: int(item[1].get("OrderNo", 0))))
                    Li="Liste des visites avec cette fiches :"
                    for  VFkey,LV in ListVisit.items():
                        # Ecriture des variables nécéssaire pour l'affichage
                        Vgui_temp=LV["ProVisitGuid"]
                        V_description_temp = data["ProVisit"][Vgui_temp]["Description"]
                        Li+= f"{V_description_temp}"
                    content+=f"<p>{Li}</p> \n"
                    # doc.add_paragraph(Li)

                    



                ProFormGroup=filtrer_par_cle( data["ProFormGroup"],"ProFormGuid",ProFormGuid)
                for  key,FormGroup in ProFormGroup.items():
                    # Ecriture des variables nécéssaire pour l'affichage
                    ProGroupGuid        =FormGroup["ProGroupGuid"]
                    G_description       =data["ProGroup"][ProGroupGuid]["Caption"]
                    G_Caption           =data["ProGroup"][ProGroupGuid]["Caption"]


                    # Titre du groupe, ainsi que l'entete pour les  variables
                    content+=f"<h3> {G_description} </h3>\n"
                    # doc.add_heading(f"{G_description}", level=4)
                                    
                    content+="<table style='width:100%;'>\n"
                    content+="<tr>\n"
                    content+="<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>\n"
                    if display_Edit:content+="<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->\n"
                    content+="<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>\n"
                    content+="<th style='width:50px; text-align:center;'><strong>Sas</strong></th>\n"
                    content+="</tr>\n"


                    # # table = doc.add_table(rows=1, cols=4)
                    # table.autofit = True
                    # table.style = 'Table Grid'

                    # # Table header
                    # hdr_cells = table.rows[0].cells
                    # hdr_cells[0].text = 'Label de la question'
                    # if display_Edit:
                    #     hdr_cells[1].text = 'Check'
                    # hdr_cells[2].text = 'Réponses possibles'
                    # hdr_cells[3].text = 'Sas'



                    ProGroupItem=filtrer_par_cle( data["ProGroupItem"],"ProGroupGuid",ProGroupGuid)
                    if logprint:print("écriture de ###",G_description, "(", len(ProGroupItem),")")
                    for  GI_key,GroupItem in ProGroupItem.items():
                        # Ecriture des variables nécéssaire pour l'affichage
                        I_OrderNo           =GroupItem["OrderNo"]
                        ProItemGuid         =GroupItem.get("ProItemGuid")
                        I_description       =data["ProItem"][ProItemGuid]["Description"]
                        i_SasName           =data["ProItem"][ProItemGuid]["SasName"]
                        I_Caption           =data["ProItem"][ProItemGuid]["Caption"]
                        ProCodeListGuid     =data["ProItem"][ProItemGuid]["ProCodeListGuid"]
                        Hidden              =data["ProItem"][ProItemGuid]["Hidden"]
                        Disabled            =data["ProItem"][ProItemGuid]["Disabled"]
                        ReadOnly            =data["ProItem"][ProItemGuid]["ReadOnly"]
                        i_Display           =data["ProItem"][ProItemGuid]["Display"]
                        I_Status            =data["ProItem"][ProItemGuid]["Status"]
                        rep=""
                        if ProCodeListGuid :rep=data["ProCodeList"][ProCodeListGuid]["Display"]
                      
                      
                        # DICO[f"[{V_Caption}][{F_Caption}][{G_Caption}][{I_Caption}] "] = {

                        #     'i_SasName':i_SasName,
                        #     'F_SasName':F_SasName     
                        # }

                        
                        Message = get_message(data["ProEdit"],ProItemGuid,ProGroupGuid,ProFormGuid)    
                        
                        content+=" <tr> \n"                       
                        content+=            f" <td style='width:600px; text-align:left;'> {I_description}</td>\n" 
                        if display_Edit:content+=             f" <td class='check' style='width:600px; text-align:left;'>  {Message} </td>\n" 
                        content+=             f" <td style='width:300px; text-align:center;'> {rep} </td> \n"
                        content+=            f"<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> {I_Status}{i_SasName} </b></td> \n" 
                        content+=" </tr>\n"
                        JSON_EXPORT = get_JSONLIGNE(JSON_EXPORT,V_description,F_description,G_description,GI_key,I_description,Message,rep,i_Display,I_Status,i_SasName)            
                        # print("écriture de ",I_description)
                        # para = doc.add_paragraph()
                        # run = para.add_run("")

                        # # Add row for each group item
                        # row_cells = table.add_row().cells
                        # row_cells[0].text = I_description
                        # row_cells[2].text = rep
                        # p = row_cells[2].paragraphs[0]  # Premier paragraphe de la cellule
                        # run = p.add_run(rep)

                        # # Appliquer la police compatible avec les émojis
                        # run.font.name = 'Segoe UI Emoji'

                        # # Modifier également au niveau XML pour garantir la compatibilité dans Word
                        # r = run._element
                        # rPr = r.get_or_add_rPr()
                        # rFonts = OxmlElement('w:rFonts')
                        # rFonts.set(qn('w:ascii'), 'Segoe UI Emoji')
                        # rFonts.set(qn('w:hAnsi'), 'Segoe UI Emoji')
                        # rPr.append(rFonts)
                        # row_cells[3].text = f"{I_Status} {i_SasName}"
                        

                    content+="</table>\n\n"
                content+=f"</section>"
                # doc.add_page_break()
            content+=f"</section> \n"



        with open(rf"{os.getcwd()}/Python/sidebar.js", 'r', encoding='utf-8') as file:
            js = file.read()    
        content+=f"  </div><script>{js}</script> </body>\n\n\n"
        
        return content,doc,JSON_EXPORT
        
def get_JSONLIGNE(JSON_EXPORT, V_description, F_description, G_description, GI_key,
                  I_description, Message, rep,display, I_Status, i_SasName):
    # Assure-toi que la clé 'Patient' existe dans JSON_EXPORT
    if 'visites' not in JSON_EXPORT:
        JSON_EXPORT['visites'] = []

    # Cherche si le patient existe déjà dans la liste des patients, sinon crée-le
    visites = next((p for p in JSON_EXPORT['visites'] if p['V_description'] == V_description), None)
    
    if not visites:
        # Crée un nouveau patient avec V_description comme nom
        visites = {"V_description": V_description, "fiches": []}
        JSON_EXPORT['visites'].append(visites)

    # Cherche la fiche dans le patient, sinon crée-la
    fiche = next((f for f in visites['fiches'] if f['F_description'] == F_description), None)
    
    if not fiche:
        fiche = {"F_description": F_description, "groupes": []}
        visites['fiches'].append(fiche)

    # Cherche le groupe dans la fiche, sinon crée-le
    groupe = next((g for g in fiche['groupes'] if g['G_description'] == G_description), None)
    
    if not groupe:
        groupe = {"G_description": G_description, "questions": []}
        fiche['groupes'].append(groupe)


    # Ajout de la question dans le groupe
    question = {
         "GI_key": GI_key,
        "I_description": I_description,
        "Message": Message if Message else None,
        "rep": rep if rep else display,
        "I_Status": I_Status,
        "i_SasName": i_SasName
    }
    groupe['questions'].append(question)
    
    return JSON_EXPORT


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
    # output_path = os.path.join(execution_path, "OUTFILE")
    output_path =execution_path

    # Gestion des chemins locaux
    if len(sys.argv) <= 1:
        # output_path += "_LOCAL"
        ensure_directories(output_path, sub_dirs=["JSON"])
        if not confirm_execution(output_path):
            return
    ensure_directories(output_path)
    # Lecture des données et configuration
    config_path = os.path.join(execution_path, "Python/config.json")
    data = lire_et_trier_donnees(Pathin, config_path)
   
    # Export des données
   
    # doc = Document()
    JSON_EXPORT = {}
    content ,doc,JSON_EXPORT= exporter_donnees_markdown_eCRF(data,"5.0.3.27.Update 3b",True)
    

    ensure_directories(f"{output_path}/DOCX")
    ensure_directories(f"{output_path}/HTML")
    ensure_directories(f"{output_path}/MD")
    # doc.save(f"{output_path}/DOCX/{file_name}.docx")


    with open(f"{os.getcwd()}/Python/style.css", 'r', encoding='utf-8') as file:
            css = file.read()    



    htmlcontent = (f"<head>\n"
    f"    <meta charset='UTF-8'>\n"
    f"    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
    f"    <title>test fiche</title>\n"
    f"    <style>\n{css}\n</style>\n"  # Inclure le CSS directement
    f"</head>\n\n"
    + content
) #remove_details_tags(content)
    # if len(JSON_EXPORT)>0:save_json(JSON_EXPORT,f"{output_path}/JSON", f"{file_name}_CRFS.json")
    # else: print("Liste des checks vide!")
    if not os.path.exists(f"{output_path}/docs/MD/{file_name}.md"):
        with open( f"{output_path}/docs/MD/{file_name}.md" , 'w', encoding='utf-8') as f:
                f.write(f"# DOCUMENTATION POUR LE FICHIER {file_name}")
                
    customjs = f"const jsonData = {json.dumps(JSON_EXPORT)};"
    final_export_0=contenu_html.replace("// <JSONDATA>",customjs)
    final_export=final_export_0.replace("/* <css></css> */",css)
    with open( f"{output_path}/docs/Templates/{file_name}.html" , 'w', encoding='utf-8') as f:
        f.write(final_export)


if __name__ == "__main__":
    main()





             
