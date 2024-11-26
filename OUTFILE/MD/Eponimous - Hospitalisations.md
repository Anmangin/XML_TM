<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='f7c2094c-9441-4b0e-9326-6dfa5f45cf4a' data-parent='26bb58d6-2966-4639-92f6-b83e86a4f797' data-type='form' data-label='Hospitalisation Yes/No'>
<h2> Hospitalisation Yes/No </h2>
<p>Liste des visites avec cette fiches :Hospitalisation</p> 
<h3> HO1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Was the patient hospitalised or admitted to an emergency unit at least once during the study?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> <i><font color="#993333">If yes, please complete an Hospitalisation form.</font></i></td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOYNC </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Start date of collection of hospitalisation data</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOCOLSDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> End date of collection of hospitalisation data</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOCOLEDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Flag Hosp YN</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> DVC:[Hospitalisation YN.*][HO1.*][FLAGHOYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
if ([Hospitalisation YN][HO1][HOYN] == '1')
    '1';
else
    ''; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 👻FLAGHOYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 </tr>
</table>

</section><section id='ac276d80-abfb-439f-b7ca-b4ec15c1d175' data-parent='26bb58d6-2966-4639-92f6-b83e86a4f797' data-type='form' data-label='Hospitalisation'>
<h2> Hospitalisation </h2>
<p>Liste des visites avec cette fiches :Hospitalisation</p> 
<h3> HO2 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Start date</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOSDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> End date</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOEDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Hospitalisation in the recruitment centre</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOENCTYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If no, centre name</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[HO2.*][HOENCT_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[HO2][HOENCTYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOENCT_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> GHM</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOGHM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Type of cares (multiple responses possible)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOTYPCOM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Surgery</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOTYPS </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Chemotherapy</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOTYPCT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Radiotherapy</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOTYPRT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Supportive care</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOTYPSC </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Palliative care</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOTYPPC </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Other</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOTYPO </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[HO2.*][HOTYPO_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[HO2][HOTYPO] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOTYPO_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Ward (multiple responses possible)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWCOM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Day hospital</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWDH </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Inpatient medical unit</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWIMU </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Inpatient surgical unit</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWISU </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Emergency unit</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWEU </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Intensive care unit</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWICU </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If intensive care unit, number of days</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[HO2.*][HOWICUNB]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[HO2][HOWICU] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWICUNB </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Home care hospitalisation</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWHCH </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Other</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWO </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[HO2.*][HOWO_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[HO2][HOWO] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOWO_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Primary reason for hospitalisation</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Surgical intervention</b><br>🔘 2 - <b>Administration of chemotherapy</b><br>🔘 3 - <b>Radiotherapy</b><br>🔘 4 - <b>Toxicity</b><br>🔘 5 - <b>Progression</b><br>🔘 6 - <b>Palliative care</b><br>🔘 99 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HOREAS </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If toxicity, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[HO2.*][HORSTX_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[HO2][HOREAS] == '4'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HORSTX_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[HO2.*][HORSO_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[HO2][HOREAS] == '99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HORSO_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Flag Hosp</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> DVA:[Hospitalisation.*][HO2.*][FLAGHOSP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
if (!isEmpty([Hospitalisation.@][HO2][HOSDT]))
    '1';
else
    ''; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 👻FLAGHOSP </b></td> 
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


