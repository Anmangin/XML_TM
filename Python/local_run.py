import os
import subprocess

# Récupérer le chemin actuel
execution_path = os.getcwd()

# Construire le chemin vers le dossier contenant les fichiers XML
path = os.path.join(execution_path, 'INFILE', 'XML')

# Vérifier que le chemin existe
if not os.path.exists(path):
    print(f"Le dossier {path} n'existe pas.")
    exit(1)

# Lister tous les fichiers XML dans le dossier
xml_files = [f for f in os.listdir(path) if f.endswith('.xml')]

if not xml_files:
    print(f"Aucun fichier XML trouvé dans le dossier {path}.")
    exit(0)

# Parcourir chaque fichier XML et exécuter le script Python avec son chemin comme argument
for xml_file in xml_files:
    xml_path = os.path.join(path, xml_file)
    try:
        print(f"Lancement du script pour le fichier : {xml_path}")
        subprocess.run(['python', 'Python/update.py', xml_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution pour le fichier {xml_path} : {e}")
