<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='660f89dc-9b0e-4843-abe2-205444ca4fa0' data-parent='ca6bd388-d19c-45e8-97e6-8eb9820d0f84' data-type='form' data-label='5D3L'>
<h2> 5D3L </h2>
<p>Liste des visites avec cette fiches :Quality of Life</p> 
<h3> QLQHEAD </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Questionnaire rempli par le patient</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date de remplissage du questionnaire par le patient</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQHEAD.*][QLQDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQHEAD][QLQYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Raison de non remplissage du questionnaire</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQHEAD.*][QLQNO_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQHEAD][QLQYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQNO_R </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date à laquelle le questionnaire aurait dû être rempli</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQHEAD.*][QLQEXPDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQHEAD][QLQYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQEXPDT </b></td> 
 </tr>
</table>

<h3> 5D3L </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Mobilité</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Je n’ai aucun problème pour me déplacer à pied.</b><br>🔘 2 - <b>J’ai des problèmes pour me déplacer à pied.</b><br>🔘 3 - <b>Je suis obligé(e) de rester alité(e).</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL1 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Autonomie de la personne</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1-Je n’ai aucun problème pour prendre soin de moi.</b><br>🔘 2 - <b>2- J’ai des problèmes pour me laver ou m’habiller tout(e) seul(e).</b><br>🔘 3 - <b>3-Je suis incapable de me laver ou de m’habiller tout(e) seul(e).</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL2 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Activités courantes</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1-Je n’ai aucun problème pour accomplir mes activités courantes</b><br>🔘 2 - <b>2-J’ai des problèmes pour accomplir mes activités courantes.</b><br>🔘 3 - <b>3-Je suis incapable d’accomplir mes activités courantes.</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL3 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Douleurs/gêne</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1-Je n’ai ni douleurs ni gêne.</b><br>🔘 2 - <b>2-J’ai des douleurs ou une gêne modérée(s).</b><br>🔘 3 - <b>3-J’ai des douleurs ou une gêne extrême(s).</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL4 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Anxiété/Dépression</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1-Je ne suis ni anxieux(se) ni déprimé(e).</b><br>🔘 2 - <b>2-Je suis modérément anxieux(se) ou déprimé(e).</b><br>🔘 3 - <b>3-Je suis extrêmement anxieux(se) ou déprimé(e).</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL5 </b></td> 
 </tr>
</table>

</section></section> 
  </div><script>function generateSidebar() {

    // Récupère tous les éléments H1 et H2
    var headersH1 = document.querySelectorAll('h1');
    var headersH2 = document.querySelectorAll('h2');
    var sidebarLinks = document.getElementById('sidebar-links');
    var sections = document.querySelectorAll('.content section');
    
    // Créer des liens pour chaque H1 dans la sidebar
    sections.forEach(section => {
        
        let type=section.getAttribute('data-type')
        var link = document.createElement('a');
        link.href = '#' + section.id;  // Associe le lien à l'ID du H1
        link.textContent = section.getAttribute('data-label');
        link.setAttribute('data-target', section.id);
        link.classList.add(type);  // Lien H1
        // Si le type est "form", ajoute un tiret ou une indentation
        if (type === "form") {
            // Ajouter un tiret avant le texte du lien
            link.textContent = "" + link.textContent;  // Tiret simple

            // Ou ajouter une indentation (par exemple, un espacement supplémentaire)
            link.style.marginLeft = "20px";  // Déplacement à droite, ajustable
        } else {
            // Sinon, applique une police plus grosse et un fond bleuté
            link.style.fontSize = "18px";  // Augmente la taille de la police
            link.style.backgroundColor = "#e0f7fa";  // Fond bleu clair (légèrement bleuté)
            link.style.padding = "5px";  // Un peu de padding pour l'espace autour du texte
            link.style.borderRadius = "4px";  // Coins arrondis pour l'esthétique
        }

        sidebarLinks.appendChild(link);
    })
        
  

    // Gestion des événements de clic sur les liens de la sidebar
    const links = document.querySelectorAll('.sidebar a');

    links.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            
            const targetId = link.getAttribute('data-target');  // L'ID de la section ciblée
            let selected_section = document.getElementById(targetId);
            let parenttargetId = selected_section.getAttribute('data-parent');
            let select_section = selected_section.getAttribute('data-type');
            let select_label= selected_section.getAttribute('data-label');

            let sections = document.querySelectorAll('.content section');
            console.log(parenttargetId, select_section)
            console.log("selection de la visite ",select_label, " targetId:", targetId, " " , "parenttargetId :",parenttargetId )

            //console.log(targetId,parenttargetId)
           i=0
            sections.forEach(section => {
                // console.log(section)
                i+=1
                let sectionid= section.id;
                let parentid= section.getAttribute('data-parent');
                let type= section.getAttribute('data-type');
                let label= section.getAttribute('data-label');
                                
                section.classList.remove('show', 'hidden');
                let affichage="hidden";

                if ( select_section=="form" && type=="visit"    && sectionid==parenttargetId    )affichage="show"
                else if (select_section==type && (sectionid==targetId))affichage="show"
                else if (select_section=="visit" && type=="form" && parenttargetId==parentid )affichage="show"

                // if (select_section=="form" && (sectionid == targetId || sectionid==parenttargetId  )) affichage="show"
                // else if  (select_section=="visit" && (sectionid == targetId || sectionid==parenttargetId || parentid==targetId || parentid==parenttargetId  )) affichage="show"
                
                section.classList.add(affichage)
                console.log("------------->test du ",label, ":",affichage  , "parenttargetId:",parenttargetId , "sectionid:",sectionid)

            });

        });
    })
}



window.onload = generateSidebar;
</script> </body>


