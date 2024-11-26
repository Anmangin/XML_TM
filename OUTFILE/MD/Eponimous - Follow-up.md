<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='f731e41d-5cad-4ba4-93ec-403187ceeda8' data-parent='0f946897-8632-4a01-b960-b5a82b8509b1' data-type='form' data-label='Follow-Up'>
<h2> Follow-Up </h2>
<p>Liste des visites avec cette fiches :Follow-Up</p> 
<h3> FU </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> During this follow-up visit, did you have any information on the patient?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If no, reason</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUNO_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Consent withdrawn</b><br>🔘 2 - <b>Lost to follow-up</b><br>🔘 99 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUNO_R </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUNO_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '0' && [FU][FUNO_R] == '99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUNO_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date of last news</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Status of the patient</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUCS]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Alive</b><br>🔘 1 - <b>Dead</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUCS </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> <i><font color="#993333">If alive</font></i></td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUCOM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Disease state?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUDISCS]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Complete response</b><br>🔘 2 - <b>Partial response</b><br>🔘 3 - <b>Stable disease</b><br>🔘 4 - <b>Progressive disease</b><br>🔘 5 - <b>Not evaluable</b><br>🔘 6 - <b>Unknown</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUDISCS </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Occurrence of a second cancer?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FU2NDK]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FU2NDK </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> New anticancer treatment ongoing?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUTRTGO]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUTRTGO </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If yes, treatment name</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUTRT_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0' && [FU][FUTRTGO] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUTRT_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> SAE since the last visit?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUSAEYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUSAEYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If yes, term(s)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUSAE_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0' && [FU][FUSAEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUSAE_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
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


