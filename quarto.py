import os
import quarto

# Contenu du fichier .qmd
qmd_content = '''---
title: "Mon Document Quarto"
author: "Votre Nom"
format: html
---

# Introduction

Ceci est un exemple de document Quarto généré avec Python.

## Exemple de Code Python

```{python}
# Code Python exécuté par Quarto
print("Bonjour, Quarto !")
'''
file_name = "exemple_document.qmd"
with open(file_name, "w") as file: file.write(qmd_content)
os.system(f"quarto render {file_name}")
