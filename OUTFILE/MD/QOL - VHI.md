<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='faa69887-2406-4a4f-a923-59f7f90b2630' data-parent='4a55c8a4-655d-4688-96eb-fdef5763314b' data-type='form' data-label='Voice Handicap Index'>
<h2> Voice Handicap Index </h2>
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

<h3> VHIG1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> F1. On a du mal à m'entendre à cause de ma voix.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF1 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> F2. On me comprend difficilement dans un milieu bruyant.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF2 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> F8. Mes problèmes de voix limitent ma vie personnelle et sociale.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF8 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> F9. Je me sens exclu(e) des conversations à cause de ma voix.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF9 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> F10. Mes problèmes de voix entraînent une perte de revenu.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF10 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> P3. Les gens me posent des questions sur ma voix.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIP3 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> P5. J'ai l'impression que je dois me forcer physiquement pour parler.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIP5 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> P6. La clarté de ma voix est imprévisible.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIP6 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> E4. Mes problèmes de voix me contrarient.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIE4 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> E6. Je me sens handicapé(e) à cause de ma voix.</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b><br>🔘 1 - <b>Presque jamais</b><br>🔘 2 - <b>Parfois</b><br>🔘 3 - <b>Presque toujours</b><br>🔘 4 - <b>Toujours</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIE6 </b></td> 
 </tr>
</table>

<h3> VHIG2 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Comment votre voix est-elle aujourd'hui ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Normale (bonne qualité)</b><br>🔘 1 - <b>Un peu anormale</b><br>🔘 2 - <b>Assez anormale</b><br>🔘 3 - <b>Très anormale</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIVOICE </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Sur une échelle de 0 à 10, à quel degré votre problème de voix influence-t-il votre qualité de vie ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>0 Pas du tout</b><br>🔘 1 - <b>1</b><br>🔘 2 - <b>2</b><br>🔘 3 - <b>3</b><br>🔘 4 - <b>4</b><br>🔘 5 - <b>5</b><br>🔘 6 - <b>6</b><br>🔘 7 - <b>7</b><br>🔘 8 - <b>8</b><br>🔘 9 - <b>9</b><br>🔘 10 - <b>10 Enormément</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIQOL </b></td> 
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


