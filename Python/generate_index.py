import os
import markdown  # Importer le module markdown

def generate_index_html(directory):
    # Vérifie si le répertoire existe
    if not os.path.isdir(directory+"/Templates"):
        print(f"Le répertoire {directory} Templates  n'existe pas.")
        return

    # Liste tous les fichiers HTML dans le répertoire
    html_files = [f for f in os.listdir(directory +"/Templates") if f.endswith('.html')]

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

    td h1 {
  /* Les règles CSS que tu veux appliquer aux <h1> à l'intérieur des <td> */
  font-size: 16px;
  color: blue;
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
    .md-content {
      background-color: #f0f8ff;
      padding: 10px;
      margin-top: 10px;
      border-radius: 5px;
      font-size: 0.95em;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
  table-layout: auto; /* Permet aux colonnes de s'ajuster en fonction du contenu */
  
}

thead {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
  table-layout: auto; /* Permet aux colonnes de s'ajuster en fonction du contenu */
}

th, td {
  padding: 2px;
  text-align: left;
  border: 1px solid #ddd;
  height: 30px; /* Hauteur fixe pour toutes les cellules */
  word-wrap: break-word; /* Empêche le texte de déborder des cellules */
}

th.crf {
  width: 30%; /* Utilisation d'un pourcentage pour la largeur */
  background-color: #e7f3ff;
}

th.doc {
  width: 70%; /* Utilisation d'un pourcentage pour la largeur */
  background-color: #e7f3ff;
}

td.crf {
  width: 30%;
   background-color: #e7f3ff;
}

td.doc {
  width: 70%;
}

.category-title {
  font-size: 1.6em;
  color: #1a73e8;
  margin-top: 20px;
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
            index_content += '''
<table  width="100%">
  <thead  width="100%">
    <tr>
     <th class="crf" width="30%">Lien CRF</th>
      <th class="doc" width="70%">Doc disponible</th>
    </tr>
  </thead>
  <tbody>
    <tr>

'''
            
            for file in categories[category]:
                # Charge le fichier markdown correspondant si il existe
                md_file = file.replace('.html', '.md')
                md_content = ''
                md_lines_count=0
                if os.path.isfile(f"docs/MD/{md_file}"):
                    with open(f"docs/MD/{md_file}", 'r', encoding='utf-8') as f:
                        md_content = f.read()
                        print(md_content)

                # Convertir le markdown en HTML (si du contenu est présent)
                md_html = ''
                if md_content:
                    md_html = f'<div class="md-content">{markdown.markdown(md_content)}</div>'
                    md_lines_count = len(md_html.splitlines())

                
     
                index_content += f'  <td class="crf"> <a href="docs/Templates/{file}">{file}</a> </td> \n '
                if  md_lines_count>1 : index_content += f'  <td class=doc > {md_html} </td> </tr>\n '
                else:index_content += f'  <td class="doc"> N/A </td> </tr>\n '

          
            index_content += f'</tbody></table>' 

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
execution_path = rf'{os.getcwd()}/docs'
generate_index_html(execution_path)
