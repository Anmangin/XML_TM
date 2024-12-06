import xml.etree.ElementTree as ET
import re
import sys     
import os
import json
import traceback

import tkinter as tk
from tkinter.filedialog import askopenfilename,askdirectory
from tkinter import messagebox
from pathlib import Path
from XML_Function import lire_et_trier_donnees,exporter_donnees_markdown_eCRF


# Paramètres globaux
unic_form = False



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
def print_MD(output_path,file_name):
        if not os.path.exists(f"{output_path}/docs/MD/{file_name}.md"):
            with open( f"{output_path}/docs/MD/{file_name}.md" , 'w', encoding='utf-8') as f:
                f.write(f"# DOCUMENTATION POUR LE FICHIER {file_name}")

def main():
 try:
    if getattr(sys, 'frozen', False):
        execution_path = sys._MEIPASS
    else :execution_path = os.getcwd()


    

   

    Pathin = get_path_input()
    file_name = os.path.basename(Pathin).replace('.xml', '')
    # directory = os.path.dirname(Pathin)
    output_path =execution_path

    # Gestion des chemins locaux
    if len(sys.argv) <= 1 and getattr(sys, 'frozen', False):
        output_path += "/LOCAL"
        ensure_directories(output_path, sub_dirs=["docs"])
        ensure_directories(output_path+"/docs", sub_dirs=["Templates"])
    ensure_directories(output_path)
    

    
    # Lecture des données et configuration
    config_path = os.path.join(execution_path, "Python\config.json")

    data = lire_et_trier_donnees(Pathin, config_path)
   

    JSON_EXPORT= exporter_donnees_markdown_eCRF(data,unic_form)
    

    css = Path(f"{execution_path}/Python/style.css").read_text(encoding='utf-8')

# SORTIE MD QUAND C'est pour le stancard.

    if len(sys.argv) >1: print_MD(output_path,file_name)
                
    JSON_Data = f"const jsonData = {json.dumps(JSON_EXPORT)};"
    chemin_html = f"{execution_path}/Python/Template_CRF.html"
    contenu_html = Path(chemin_html).read_text(encoding='utf-8')
    final_export_0=contenu_html.replace("// <JSONDATA>",JSON_Data)
    final_export_1=final_export_0.replace("/* <css></css> */",css)
    final_export_2=final_export_1.replace(r"\r\n","<br>")
    final_export_3=final_export_2.replace(r"\n","<br>")
    final_export=final_export_3.replace(r"\r","<br>")



    if getattr(sys, 'frozen', False):
        folder=askdirectory()
    else:folder=f"{output_path}/docs/Templates"

    with open( f"{folder}/{file_name}.html" , 'w', encoding='utf-8') as f:
        f.write(final_export)
    print(f"le fichier {output_path}/docs/Templates/{file_name}.html imprimé avec succes")

 except Exception as e:
        # Capturer l'erreur et l'écrire dans un fichier log.txt
        with open("log.txt", "w") as log_file:
            log_file.write("Une erreur est survenue :\n")
            traceback.print_exc(file=log_file)  # Écrit l'exception complète dans log.txt
        print(f"Une erreur s'est produite. Consultez log.txt pour plus de détails.  {log_file}")


if __name__ == "__main__":
    main()





             
