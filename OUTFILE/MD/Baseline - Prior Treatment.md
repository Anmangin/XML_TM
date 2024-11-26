<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='2de287f1-8064-40eb-a877-60ec2138615e' data-parent='fcd47032-d8b3-42e8-99d8-85660e1ec957' data-type='form' data-label='Prior chemotherapy'>
<h2> Prior chemotherapy </h2>
<p>Liste des visites avec cette fiches :Baseline</p> 
<h3> SYSTYN </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Prior Chemotherapy / Target Therapy / Immunotherapy:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SYSTYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Total number of prior anticancer lines\r\nPlease one line by prior anticancer lines in the following table.</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[Prior chemotherapy.*][SYSTYN.*][PACNB]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Prior chemotherapy][SYSTYN][SYSTYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PACNB </b></td> 
 </tr>
</table>

<h3> SYST </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Nature of treatment</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Chemotherapy & immunotherapy</b><br>🔘 2 - <b>Target therapy</b><br>🔘 3 - <b>Immunotherapy only</b><br>🔘 4 - <b>Chemotherapy only</b><br>🔘 5 - <b>other systemic treatment</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TRTTYP </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Name of protocol</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PROTO </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Treatment for</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Locally/locally advanced disease</b><br>🔘 2 - <b>Metastatic disease</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRFOR </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> <b>Name of drugs\r\n</b>(one or more drugs in one row)<i>\r\n</i></td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DRG </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Start date</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SYSTSDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> End date</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[Prior chemotherapy.*][SYST.*][SYSTEDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var db=[Prior chemotherapy][SYST.@][SYSTSDT];
var fn = [Prior chemotherapy][SYST.@][SYSTEDT];

isDate1LEDate2(db,fn); 
#data Expression 
 
</code></pre> </td><td> la date de fin est avant la date de début, merci de corriger.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SYSTEDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Reason of stop</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Progression</b><br>🔘 2 - <b>Toxicity</b><br>🔘 3 - <b>Complete remission</b><br>🔘 4 - <b>Partial remission</b><br>🔘 5 - <b>End of protocole</b><br>🔘 6 - <b>Patient's choice</b><br>🔘 7 - <b>Other, please specify</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRSTOP_R </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> other reason, please specify</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRSTOP_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date of progression</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[Prior chemotherapy.*][SYST.*][PRPROGDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Prior chemotherapy][SYST.@][PRSTOP_R] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRPROGDT </b></td> 
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


