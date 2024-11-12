import xml.etree.ElementTree as ET
import re
import sys

def lire_et_trier_donnees(pathfileXML):
    # Analyse du fichier XML
    tree = ET.parse(pathfileXML)
    root = tree.getroot()

    # Liste des fiches
    FD = []
    for FWAW in root.iter('ProForm'):
        Description_F = FWAW.findtext("Description")
        SasName_F = FWAW.findtext("SasName")
        ProObjectGuid_F = FWAW.findtext("ProObjectGuid")
        FD.append((Description_F, SasName_F, ProObjectGuid_F))
    FD.sort()

    # Liste des groupes
    GL = []
    for GRAW in root.iter('ProFormGroup'):
        ProFormGuid_g = GRAW.findtext("ProFormGuid")
        ProGroupGuid_F = GRAW.findtext("ProGroupGuid")
        GL.append((ProFormGuid_g, ProGroupGuid_F))
    GL.sort()

    # Liste des groupes avec descriptions
    GD = []
    for GRAW in root.iter('ProGroup'):
        ProObjectGuid = GRAW.findtext("ProObjectGuid")
        Description = GRAW.findtext("Description")
        GD.append((ProObjectGuid, Description))
    GD.sort()

    # Liste des questions
    QL = []
    for GRAW in root.iter('ProGroupItem'):
        OrderNo = GRAW.findtext("OrderNo")
        ProGroupGuid = GRAW.findtext("ProGroupGuid")
        ProItemGuid = GRAW.findtext("ProItemGuid")
        QL.append((OrderNo, ProGroupGuid, ProItemGuid))
    QL.sort()

    # Liste des questions avec description
    QD = []
    for GRAW in root.iter('ProItem'):
        ProObjectGuid = GRAW.findtext("ProObjectGuid")
        Description = GRAW.findtext("Description")
        Description = re.sub("<[/]?\\w*>", "", Description)
        Description = re.sub("&nbsp;", "", Description)
        Description = re.sub("</font>", "", Description)
        Description = re.sub('<font color="#' + "\\w*" + '">', "", Description)
        SasName = GRAW.findtext("SasName")
        MinLength = GRAW.findtext("MinLength")
        MaxLength = GRAW.findtext("MaxLength")
        Scale = GRAW.findtext("Scale")
        ProControlTypeId = GRAW.findtext("ProControlTypeId")
        Hidden = GRAW.findtext("Hidden")
        ReadOnly = GRAW.findtext("ReadOnly")
        ProDataTypeId = GRAW.findtext("ProDataTypeId")
        ProCodeListGuid = GRAW.findtext("ProCodeListGuid")
        QD.append((ProObjectGuid, Description, SasName, MinLength, MaxLength, Scale, ProControlTypeId, Hidden, ReadOnly, ProDataTypeId, ProCodeListGuid))
    QD.sort()

    # Liste des catégories
    CL = []
    for GRAW in root.iter('ProCodeList'):
        ProObjectGuid = GRAW.findtext("ProObjectGuid")
        Caption = GRAW.findtext("Caption")
        CL.append((ProObjectGuid, Caption))
    CL.sort()

    # Liste des catégories avec description
    CD = []
    for GRAW in root.iter('ProCodeListItem'):
        OrderNo = GRAW.findtext("OrderNo")
        ProCodeListGuid = GRAW.findtext("ProCodeListGuid")
        Caption = GRAW.findtext("Caption")
        Value = GRAW.findtext("Value")
        CD.append((OrderNo, ProCodeListGuid, Caption, Value))
    CD.sort()

    # Retourner les données sous forme de dictionnaire trié
    return {
        "FD": FD,
        "GL": GL,
        "GD": GD,
        "QL": QL,
        "QD": QD,
        "CL": CL,
        "CD": CD
    }

def exporter_donnees_markdown_eCRF(donnees, pathfileXML):
    # Ouvrir le fichier markdown en écriture
    with open(pathfileXML + '.md', 'w', encoding='utf-8') as f:
        # Titre principal du fichier
        f.write("# Maquette CRF de l'étude *****\n\n")
        
        # Parcours des fiches et ajout des informations en Markdown
        for FDA in donnees["FD"]:
            Description = FDA[0]
            SasName = FDA[1]
            f.write(f"<div style='background-color: #add8e6; color: white; width: 100%; text-align: center; padding: 20px 0; font-size: 24px; font-weight: bold;'>{Description}</div>\n")
            f.write(f"<div style='color: red; text-align: center; font-style: italic;'>{SasName}</div>\n\n")

            
            # Recherche des groupes associés à chaque fiche
            GLT = filter(lambda x: x[0] == FDA[2], donnees["GL"])
            for GLA in GLT:
                GDT = filter(lambda x: x[0] == GLA[1], donnees["GD"])
                for GDA in GDT:
                    Description_Groupe = GDA[1]
                    # f.write(f"### {Description_Groupe}\n\n")
                    f.write(f"<div style='background-color: #6fa3d3; color: white; width: 100%; text-align: left; padding: 10px 0; font-size: 16px; font-weight: bold;'>{Description_Groupe}</div>\n")
                    # Démarrer un tableau Markdown pour chaque groupe



                    f.write("<table style='width:100%;'>\n")
                    f.write("<tr>\n")
                    f.write("<th style='width:50px; text-align:center;'><strong>Sas</strong></th>\n")
                    f.write("<th style='width:600px; text-align:center;'><strong>Label de la Question</strong></th>\n")
                    f.write("<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>\n")
                    f.write("</tr>\n")
                    f.write("<tr>\n")



                    # f.write("| <strong style='width:600px; text-align:center;'>**Label de la Question**</strong> | <strong style='width:300px; text-align:center;'>**Réponses possibles**</strong> |\n")
                    # # f.write("| **Label de la Question** | **Réponses possibles** |\n")
                    # f.write("|---------------------------|-------------------------|\n")
                    
                    # Recherche des questions du groupe
                    QLT = filter(lambda x: x[1] == GDA[0], donnees["QL"])
                    for QLA in QLT:
                        QDT = filter(lambda x: x[0] == QLA[2], donnees["QD"])
                        for QDA in QDT:
                            OrderNo = QLA[0]
                            Label = QDA[1]
                            SasName_Question = QDA[2]
                            MinLength = QDA[3]
                            MaxLength = QDA[4]
                            Scale = QDA[5]
                            ProControlTypeId = QDA[6]
                            ProDataTypeId = QDA[9]
                            ProCodeListGuid = QDA[10]
                            
                            # Déterminer le type de question et les réponses possibles
                            ProDataType = ""
                            rep = ""
                            if ProControlTypeId == "3":
                                ProDataType = "RADIO"
                                CDT = filter(lambda x: x[1] == ProCodeListGuid, donnees["CD"])
                                for CDA in CDT:
                                    Caption = CDA[2]
                                    Value = CDA[3]
                                    rep += f" 🔘 {Value} - <b>{Caption}</b> <br>"
                            elif ProDataTypeId == "5":
                                ProDataType = "DATE"
                                rep = " DD/MM/YYYY 📅"
                            else:
                                ProDataType = "AUTRE"
                                rep = "TXT"

                            # Ajouter une ligne dans le tableau pour cette question
                            


                            f.write(f" <tr> \n<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> {SasName_Question} </b></td> \n  <td style='width:600px; text-align:left;'> {Label}   </td>\n <td style='width:300px; text-align:center;'>  {rep} </td> \n </tr>\n")
                            # f.write("\n")
                    f.write("</table>\n")
    print(f"Le fichier Markdown a été créé avec succès : {pathfileXML + '.md'}")



pathfileXML = sys.argv[1]
print(pathfileXML)
donnees = lire_et_trier_donnees(pathfileXML)
print(donnees)

exporter_donnees_markdown_eCRF(donnees, pathfileXML)
