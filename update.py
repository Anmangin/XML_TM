
import xml.etree.ElementTree as ET
import re
import sys     

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


def exporter_donnees_markdown_eCRF(data,pathout):


 with open( pathout , 'w', encoding='utf-8') as f:

# Parcourir les données
    for  PVkey,PatientVisit in data["ProPatientVisit"].items():
        ProVisitGuid=PatientVisit["ProVisitGuid"]
        V_description = data["ProVisit"][ProVisitGuid]["Description"]
        V_OrderNo=PatientVisit["OrderNo"]
        f.write(f"# {V_description} \n")



        ProVisitForm=filtrer_par_cle( data["ProVisitForm"],"ProVisitGuid",ProVisitGuid)

        for  VFkey,VisitForm in ProVisitForm.items():
            ProFormGuid=VisitForm.get("ProFormGuid")     
            F_OrderNo=VisitForm["OrderNo"]
            F_description=data["ProForm"][ProFormGuid]["Description"]

            f.write(f"## {F_description} \n")
            ProFormGroup=filtrer_par_cle( data["ProFormGroup"],"ProFormGuid",ProFormGuid)
            for  key,FormGroup in ProFormGroup.items():
                ProGroupGuid=FormGroup["ProGroupGuid"]
                G_description=data["ProGroup"][ProGroupGuid]["Caption"]
                f.write(f"### {G_description} \n\n") 


                ProGroupItem=filtrer_par_cle( data["ProGroupItem"],"ProGroupGuid",ProGroupGuid)


                f.write("<table style='width:100%;'>\n")
                f.write("<tr>\n")
                f.write("<th style='width:50px; text-align:center;'><strong>Sas</strong></th>\n")
                f.write("<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;Question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>\n")
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
                    

                f.write("</table>\n\n")



Pathin = sys.argv[1]

Pathout_0=Pathin.replace('.xml', '.md')
Pathout_1=Pathout_0.replace('INFILE', 'OUTFILE')
Pathout=Pathout_1.replace('/XML/', '/MD/')


data = lire_et_trier_donnees(Pathin)
exporter_donnees_markdown_eCRF(data, Pathout )
# data = lire_et_trier_donnees(r"C:\Users\a_mangin\Documents\GitHub\XML_TM\Codebreak01.10.2024.xml")
# exporter_donnees_markdown_eCRF(data, r"C:\Users\a_mangin\Documents\GitHub\XML_TM\Codebreak01.10.2024.md" )
