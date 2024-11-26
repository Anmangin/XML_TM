<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='3b339e7c-ae6b-48de-be45-a269fcfd8d6a' data-parent='fcd47032-d8b3-42e8-99d8-85660e1ec957' data-type='form' data-label='Vital sign and Clinical Examination'>
<h2> Vital sign and Clinical Examination </h2>
<p>Liste des visites avec cette fiches :Baseline</p> 
<h3> VS1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Clinical Examination done ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b><br>🔘 1 - <b>Done</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date of clinical assessment</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[VS.*][VS1.*][VSDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[VS][VS1][VSYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSDT </b></td> 
 </tr>
</table>

<h3> VS2 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Height (cm)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[HEIGHT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([HEIGHT] == '') ||
((140 <= [HEIGHT]) && ([HEIGHT] <= 200)) 
#data Expression 
 
</code></pre> </td><td> The height of the patient should be between 140 and 200cm. Please confirm the data.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HEIGHT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> WEIGHT (kg)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[WEIGHT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([WEIGHT] == '') ||
((40 <= [WEIGHT]) && ([WEIGHT] <= 180)) 
#data Expression 
 
</code></pre> </td><td> The weight of the patient should be between 40 and 180kg. Please confirm the data.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> WEIGHT </b></td> 
 </tr>
</table>

<h3> VS3 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> PS (performance status measured using the ECOG Scale )</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[VSPS]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([VSPS] == '') ||
((0 <= [VSPS]) && ([VSPS] <= 4)) 
#data Expression 
 
</code></pre> </td><td> The ECOG performance status must be between 0 and 4. Please correct the data.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSPS </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Systolic blood pressure (mmHG)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[VSSYS]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([VSSYS] == '') ||
((90 <= [VSSYS]) && ([VSSYS] <= 160)) 
#data Expression 
 
</code></pre> </td><td> The systolic blood pressure (SBP) of the patient should be between 90 and 160 mmHg. Please confirm the data.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSSYS </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Diastolic blood pressure (mmHG)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[VSDIAG]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([VSDIAG] == '') ||
((60 <= [VSDIAG]) && ([VSDIAG] <= 100)) 
#data Expression 
 
</code></pre> </td><td> The diastolic blood pressure (DBP) of the patient should be between 60 and 100 mmHg. Please confirm the data.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSDIAG </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> ECG</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b><br>🔘 1 - <b>Done</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ECG </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date of ECG</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[VS.*][VS3.*][ECGDAT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[VS][VS1][VSYN] == '1' && [VS][VS3][ECG]=="1"; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ECGDAT </b></td> 
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


