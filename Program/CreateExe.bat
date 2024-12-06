@echo off
REM Changer le répertoire de travail si nécessaire
cd /d "C:\Users\a_mangin\Documents\GitHub\XML_TM\Program"

xcopy "C:\Users\a_mangin\Documents\GitHub\XML_TM\Python\config.json" "C:\Users\a_mangin\Documents\GitHub\XML_TM\Program\dist\Python\config.json" /E /I /H /Y
xcopy "C:\Users\a_mangin\Documents\GitHub\XML_TM\Python\style.css" "C:\Users\a_mangin\Documents\GitHub\XML_TM\Program\dist\Python\style.css" /E /I /H /Y
xcopy "C:\Users\a_mangin\Documents\GitHub\XML_TM\Python\Template_CRF.html" "C:\Users\a_mangin\Documents\GitHub\XML_TM\Program\dist\Python\Template_CRF.html" /E /I /H /Y
xcopy "C:\Users\a_mangin\Documents\GitHub\XML_TM\Python\sidebar.js" "C:\Users\a_mangin\Documents\GitHub\XML_TM\Program\dist\Python\sidebar.js" /E /I /H /Y

REM Lancer PyInstaller avec les paramètres nécessaires
pyinstaller --onefile --icon=images.ico --add-data "dist/Python/config.json;Python" --add-data "dist/Python/style.css;Python" --add-data "dist/Python/sidebar.js;Python" --add-data "dist/Python/Template_CRF.html;Python" ../Python/interface.py


REM Attendre avant de fermer la fenêtre (facultatif)
pause