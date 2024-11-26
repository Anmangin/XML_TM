<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='7c0bd6b7-27c4-4824-8c4a-620ad6504a6d' data-parent='5a1b7bad-36eb-4009-a58a-65f3682973ab' data-type='form' data-label='Progression'>
<h2> Progression </h2>
<p>Liste des visites avec cette fiches :Events</p> 
<h3> PD </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Did the patient progressed/relapsed?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date of cancer progression or relapse</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Progression or relapse?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDTYP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Progression</b><br>🔘 2 - <b>Relapse</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDTYP </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Diagnostic of progression or relapse based on:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDDIAGC </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Imaging</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDIMGYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDIMGYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Clinical exam</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDCLINYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDCLINYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Tumor markers</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDBIOYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDBIOYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Local progression or relapse</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDLOCYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDLOCYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Regional progression or relapse</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDREGYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDREGYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Metastasis progression or relapse</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMETAYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMETAYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If yes, specify location</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTLOC </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Brain</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTBR]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTBR </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Lungs</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTLG]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTLG </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Bones</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTBN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTBN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Liver</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTLV]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTLV </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Other</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTOTH]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTOTH </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTOT_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1' && [PD][PDMTOTH] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTOT_S </b></td> 
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


