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
import tkinter as tk
from tkinter import filedialog, messagebox
from XML_Function import lire_et_trier_donnees,exporter_donnees_markdown_eCRF

def select_input_file():
    filepath = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    if filepath:
        input_path_var.set(filepath)

def select_output_folder():
    folderpath = filedialog.askdirectory()
    if folderpath:
        output_path_var.set(folderpath)

def run_program():
    if getattr(sys, 'frozen', False):
        execution_path = sys._MEIPASS
    else :execution_path = os.getcwd()
    Pathin = input_path_var.get()
    file_name = os.path.basename(Pathin).replace('.xml', '')
    output_path = output_path_var.get()
    unic_form = single_record_var.get()
    print(unic_form)

    # Lecture des données et configuration
    config_path = os.path.join(execution_path, "Python\config.json")

    data = lire_et_trier_donnees(Pathin, config_path)
   

    JSON_EXPORT= exporter_donnees_markdown_eCRF(data,unic_form)
    

    css = Path(f"{execution_path}/Python/style.css").read_text(encoding='utf-8')

# SORTIE MD QUAND C'est pour le stancard.

            
    JSON_Data = f"const jsonData = {json.dumps(JSON_EXPORT)};"
    chemin_html = f"{execution_path}/Python/Template_CRF.html"
    contenu_html = Path(chemin_html).read_text(encoding='utf-8')
    final_export_0=contenu_html.replace("// <JSONDATA>",JSON_Data)
    final_export_1=final_export_0.replace("/* <css></css> */",css)
    final_export_2=final_export_1.replace(r"\r\n","<br>")
    final_export_3=final_export_2.replace(r"\n","<br>")
    final_export=final_export_3.replace(r"\r","<br>")
    with open( f"{output_path}/{file_name}.html" , 'w', encoding='utf-8') as f:
        f.write(final_export)
    print(f"le fichier {output_path}/{file_name}.html imprimé avec succes")
  




    if not Pathin or not output_path:
        messagebox.showerror("Erreur", "Veuillez fournir les deux chemins avant de lancer le programme.")
        return

    # Remplacer ceci par l'appel à votre programme de conversion
    try:
        messagebox.showinfo("Succès", "Le programme a été exécuté avec succès !")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

def export_record():
    print("Lancement de programme")

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Convertisseur XML vers HTML")
root.geometry("400x300")

# Variables pour stocker les chemins et l'option de fiche unique
input_path_var = tk.StringVar()
output_path_var = tk.StringVar()
single_record_var = tk.BooleanVar()

# Widgets de l'interface
input_label = tk.Label(root, text="Fichier XML d'entrée :")
input_label.pack(pady=5)
input_entry = tk.Entry(root, textvariable=input_path_var, width=40)
input_entry.pack(pady=5)
input_button = tk.Button(root, text="Choisir un fichier", command=select_input_file)
input_button.pack(pady=5)

output_label = tk.Label(root, text="Dossier de sortie :")
output_label.pack(pady=5)
output_entry = tk.Entry(root, textvariable=output_path_var, width=40)
output_entry.pack(pady=5)
output_button = tk.Button(root, text="Choisir un dossier", command=select_output_folder)
output_button.pack(pady=5)

single_record_checkbox = tk.Checkbutton(root, text="Fiche unique", variable=single_record_var)
single_record_checkbox.pack(pady=5)

run_button = tk.Button(root, text="Lancer le programme", command=run_program)
run_button.pack(pady=10)

# Lancement de l'interface
root.mainloop()
