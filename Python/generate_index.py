import os

def generate_index_html(directory):
    # Vérifie si le répertoire existe
    if not os.path.isdir(directory):
        print(f"Le répertoire {directory} n'existe pas.")
        return

    # Liste tous les fichiers dans le répertoire
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

    # Crée le contenu du fichier index.html
    index_content = '''
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Liste des Templates - Gustave Roussy</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f7fb;
      margin: 0;
      padding: 0;
    }
    h1, h2 {
      color: #1a73e8;
    }
    .intro {
      background-color: #e7f3ff;
      padding: 15px;
      border-radius: 5px;
      margin: 20px;
      font-size: 1.2em;
      text-align: center;
    }
    .category-title {
      font-size: 1.6em;
      color: #1a73e8;
      margin-top: 20px;
    }
    ul {
      list-style-type: none;
      padding-left: 0;
    }
    li {
      margin-bottom: 10px;
    }
    a {
      text-decoration: none;
      color: #1a73e8;
      font-size: 1.1em;
    }
    a:hover {
      color: #0056b3;
    }
    .visit-only {
      font-size: 0.9em;
      color: #666;
    }
    .hidden {
      display: none;
    }
  </style>
</head>
<body>
  <h1>Bienvenue dans la liste des templates pour le service de Gustave Roussy</h1>
  <div class="intro">
    <p>Vous trouverez ci-dessous les templates disponibles pour l'outil TrialMaster, un standard développé par le service du BBE (DCR) pour la gestion des données cliniques. Certains documents sont réservés à la consultation uniquement et sont affichés en texte plus petit.</p>
    <p>Les fichiers qui commencent par un chiffre sont cachés pour des raisons spécifiques.</p>
  </div>
'''

    # Dictionnaire pour organiser les fichiers par catégorie
    categories = {
        'Inclusion': [],
        'Baseline': [],
        'Cycle': [],
        'QOL': [],
        'Events': [],
        'Eponimous': [],
        'Autre': []
    }

    # Liste des catégories dans l'ordre souhaité
    category_order = ['Inclusion', 'Baseline', 'Cycle', 'QOL', 'Events', 'Eponimous', 'Autre']

    # Trie les fichiers par catégorie et ajoute les fichiers à la bonne catégorie
    for file in html_files:
        if file[0].isdigit() or file.lower() == "lui même.html":
            # Ignore les fichiers qui commencent par un chiffre ou le fichier "lui même"
            continue
        
        # Sépare la catégorie du fichier (avant le tiret)
        category = file.split(' - ')[0] if ' - ' in file else "Autre"
        
        # Ajoute le fichier à la catégorie correspondante
        if category in categories:
            categories[category].append(file)
        else:
            categories['Autre'].append(file)

    # Ajoute les catégories et leurs fichiers au contenu dans l'ordre spécifié
    for category in category_order:
        if categories[category]:  # Si la catégorie contient des fichiers
            index_content += f'  <div class="category-title">{category}</div>\n'
            index_content += '  <ul>\n'
            
            for file in categories[category]:
                if 'visite only' in file.lower():
                    # Fichier "visite only", affiché plus petit
                    index_content += f'    <li class="visit-only"><a href="Templates/{file}">{file}</a></li>\n'
                else:
                    # Fichier normal
                    index_content += f'    <li><a href="Templates/{file}">{file}</a></li>\n'
            
            index_content += '  </ul>\n'

    # Termine le contenu HTML
    index_content += '''
</body>
</html>
'''

    # Écrit le contenu dans le fichier index.html
    with open(os.path.join(os.path.dirname(directory), 'index.html'), 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)

    print("Le fichier index.html a été généré avec succès.")

# Exemple d'utilisation : générer le fichier index.html pour un dossier spécifique
execution_path = rf'{os.getcwd()}/docs/Templates'
generate_index_html(execution_path)
