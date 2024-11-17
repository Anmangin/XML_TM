
import xml.etree.ElementTree as ET
import re
import sys     
import os

def Get_objt(root, racine, keyname, fields):
        ProForm = {}
        for FWAW in root.iter(racine):
            key = FWAW.findtext(keyname)
            if key:  # Vérifie que la clé existe
                ProForm[key] = {field: FWAW.findtext(field) for field in fields}
        return ProForm

def filtrer_par_cle(dictionnaire, champ, valeur):
    return {key: val for key, val in dictionnaire.items() if val.get(champ) == valeur}

def lire_et_trier_donnees(pathfileXML):
    
    tree = ET.parse(pathfileXML)
    root = tree.getroot()
    version = root.attrib.get('ver')
    data = {
        "ProPatientVisit": Get_objt(root, "ProPatientVisit", "ProObjectGuid", fields=("ProPatientGuid", "ProVisitGuid", "MinOccurance", "MaxOccurance", "OrderNo")),
        "ProVisit": Get_objt(root, "ProVisit", "ProObjectGuid", fields=("Description",)),
        "ProVisitForm": Get_objt(root, "ProVisitForm", "ProObjectGuid", fields=("ProVisitGuid", "ProFormGuid", "MinOccurance", "MaxOccurance", "OrderNo")),
        "ProForm": Get_objt(root, "ProForm", "ProObjectGuid", fields=("Description", "SasName")),
        "ProFormGroup": Get_objt(root, "ProFormGroup", "ProObjectGuid", fields=("OrderNo", "ProFormGuid", "ProGroupGuid")),
        "ProGroupItem": Get_objt(root, "ProGroupItem", "ProObjectGuid", fields=("ProGroupGuid", "ProItemGuid", "OrderNo")),
        "ProGroup": Get_objt(root, "ProGroup", "ProObjectGuid", fields=("Caption",)),
        "ProItem": Get_objt(root, "ProItem", "ProObjectGuid", fields=("Description", "Scale", "SasName", "MinLength", "MaxLength", "ProControlTypeId", "SasType","ProCodeListGuid","ProDataTypeId","Hidden","ReadOnly","Disabled")),
        "ProCodeList": Get_objt(root, "ProCodeList", "ProObjectGuid", fields=("OrderNo", "Caption")),
        "ProCodeListItem": Get_objt(root, "ProCodeListItem", "ProObjectGuid", fields=("ProCodeListGuid","OrderNo", "Caption", "Value")),
        "ProEdit": Get_objt(root, "ProEdit", "ProObjectGuid", fields=("ProEditActionId","TargetLevelId", "ProVisitFormGuid","TargetProGroupGuid","TargetProFormGuid","ProGroupGuid","ProGroupItemGuid", "ProItemGuid","ActionExpression","DataExpression","Message","TargetPath")),
        "TBNode": Get_objt(root, "TBNode", "ProObjectGuid", fields=("TBNodeId","ParentTBNodeId", "Caption","TBNodeTypeId")),
        "version":version,
    
    
    }

    for key in ["ProPatientVisit", "ProVisitForm", "ProFormGroup", "ProGroupItem","ProCodeListItem"]:
        data[key] = dict(sorted(data[key].items(), key=lambda item: int(item[1].get("OrderNo", 0))))


    #  affichage des catégories
    for key, value in data["ProCodeList"].items():
            rep = ""
            # Filtrer les items associés à la ProCodeList actuelle
            filtered_items = {k: v for k, v in data["ProCodeListItem"].items() if v["ProCodeListGuid"] == key}

            # Construire la chaîne de caractères pour le champ Display
            if len(filtered_items) < 15:
                for item in filtered_items.values():
                    rep += f"🔘 {item['Value']} - <b>{item['Caption']}</b> <br>"
            else:
                rep = "🔘 Radio boutton trop long"

            # Ajouter le champ Display
            data["ProCodeList"][key]["Display"] = rep

    for key, value in data["ProItem"].items():
            SasType=value["SasType"]
            MaxLength=value["MaxLength"]
            rep=""
            if value["ProDataTypeId"] =="5": rep = "📅 DD/MM/YYYY "
            else :rep=  f"{SasType} - {MaxLength}"

            # Ajouter le champ Display
            data["ProItem"][key]["Display"] = rep

    return data

# Appel de la fonction

def find_arbo(TBNode):
            if TBNode["ParentTBNodeId"]=="6":source="Fiche"
            elif TBNode["ParentTBNodeId"]=="7":source="groupe"
            elif TBNode["ParentTBNodeId"]=="8":source="item"
            elif TBNode["ParentTBNodeId"]=="9":source="codelist"
            elif TBNode["ParentTBNodeId"]< 10 : source="unknown"
            return source
    

def exporter_donnees_markdown_eCRF(data,pathin,pathout):
    with open( pathout , 'w', encoding='utf-8') as f:

        version=data["version"]
        f.write(f"# Version de TB pour ce fichier : {version}  \n")
        dossier = os.path.dirname(pathin)

        with open(f"{dossier}/VersionTM.txt", "r", encoding="utf-8") as fichier:
            OngoingVer = fichier.read()

        
        if OngoingVer != version :
             f.write(f"# Fichier non compatible avec la version en cours de TM : actuel:{OngoingVer}, version du fichier : {version}  \n")
             
        


        errortitle=0      
        for  PVkey,TBNode in data["TBNode"].items():    
            if TBNode["TBNodeId"] is not None  :
                TBNodeId=TBNode["TBNodeId"]
                Caption=TBNode["Caption"]
                listItm=filtrer_par_cle( data["TBNode"],"ParentTBNodeId",TBNodeId)
                if len(listItm)==0 :
                    if errortitle==0:
                        errortitle+=1
                        f.write(f"# ERREUR DANS LES DOSSIERS DU FICHIER  \n")
                        f.write(f"{find_arbo(TBNode)}/{Caption} est vide\n")

        # Parcourir les données
        print(len(data["ProPatientVisit"]), "Patients visit")
        if len(data["ProPatientVisit"])==0 : 
            if errortitle==0:
                        errortitle+=1
                        f.write(f"# ERREUR DANS LES DOSSIERS DU FICHIER  \n")
            f.write(f"Pas d'arborescence patient ! \n")
        for  PVkey,PatientVisit in data["ProPatientVisit"].items():
            ProVisitGuid=PatientVisit["ProVisitGuid"]
            V_description = data["ProVisit"][ProVisitGuid]["Description"]
            V_OrderNo=PatientVisit["OrderNo"]
            f.write(f"# {V_description} \n")
            print("écriture de #",V_description)



            ProVisitForm=filtrer_par_cle( data["ProVisitForm"],"ProVisitGuid",ProVisitGuid)
            for  VFkey,VisitForm in ProVisitForm.items():
                ProFormGuid=VisitForm.get("ProFormGuid")     
                F_OrderNo=VisitForm["OrderNo"]
                F_description=data["ProForm"][ProFormGuid]["Description"]

                f.write(f"## {F_description} \n")
                print("écriture de ##",F_description)
                ProFormGroup=filtrer_par_cle( data["ProFormGroup"],"ProFormGuid",ProFormGuid)
                for  key,FormGroup in ProFormGroup.items():
                    ProGroupGuid=FormGroup["ProGroupGuid"]
                    G_description=data["ProGroup"][ProGroupGuid]["Caption"]
                    f.write(f"### {G_description} \n\n")
                    


                    ProGroupItem=filtrer_par_cle( data["ProGroupItem"],"ProGroupGuid",ProGroupGuid)
                    print("écriture de ###",G_description, "(", len(ProGroupItem),")")



                    f.write("<table style='width:100%;'>\n")
                    f.write("<tr>\n")
                    f.write("<th style='width:50px; text-align:center;'><strong>Sas</strong></th>\n")
                    f.write("<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>\n")
                    f.write("<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>\n")
                    f.write("<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>\n")
                    f.write("</tr>\n")
                    f.write("<tr>\n")


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
                                elif EditACtion=="9":EditACtion="Read Only"
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
                            

                        f.write(
                                    " <tr> \n" +
                                    f"<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> {Hidden}{ReadOnly}{i_SasName} </b></td> \n" +
                                    f" <td style='width:600px; text-align:left;'> {I_description}</td>\n" +
                                    f" <td style='width:600px; text-align:left;'>  {Message} </td>\n" +
                                    f" <td style='width:300px; text-align:center;'> {rep} </td> \n </tr>\n"
                                    )
                        print("écriture de ",I_description)
                        

                    f.write("</table>\n\n")
    print(f"fin d'écriture dans {pathout}")



Pathin = sys.argv[1]

Pathout_0=Pathin.replace('.xml', '.md')
Pathout_1=Pathout_0.replace('INFILE', 'OUTFILE')
Pathout=Pathout_1.replace('/XML/', '/MD/')

data = lire_et_trier_donnees(Pathin)
exporter_donnees_markdown_eCRF(data,Pathin, Pathout )
# data = lire_et_trier_donnees(r"E:\Users\tony\Documents\GitHub\XML_TM\INFILE\XML\FA12.xml")
# exporter_donnees_markdown_eCRF(data,r"E:\Users\tony\Documents\GitHub\XML_TM\INFILE\XML\TRT.xml",  r"E:\Users\tony\Documents\GitHub\XML_TM\TRT.md" )
