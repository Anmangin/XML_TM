<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='a8afc052-92dc-484d-856e-469cbbf24cf8' data-parent='b56cebc0-506b-4532-b33c-805b73fcf564' data-type='form' data-label='STAI'>
<h2> STAI </h2>
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

<h3> STAI </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 1. Je me sens calme</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI01 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 2. Je me sens en sécurité, sans inquiétude, en sûreté</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI02 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 3. Je suis tendu(e), crispé(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI03 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 4. Je me sens surmené(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI04 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 5. Je me sens tranquille, bien dans ma peau</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI05 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 6. Je me sens ému(e), bouleversé(e), contrarié(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI06 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 7. L'idée de malheurs éventuels me tracasse en ce moment</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI07 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 8. Je me sens content(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI08 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 9. Je me sens effrayé(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI09 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 10. Je me sens à mon aise</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI10 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 11. Je sens que j'ai confiance en moi</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI11 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 12. Je me sens nerveux(se), irritable</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI12 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 13. J'ai la frousse, la trouille j'ai peur</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI13 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 14. Je me sens indécis(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI14 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 15. Je suis décontracté(e), détendu(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI15 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 16. Je suis satisfait(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI16 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 17. Je suis inquièt(e), soucieux(se)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI17 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 18. Je ne sais plus où j'en suis, je me sens déconcerté(e), dérouté(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI18 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 19. Je me sens solide, posé(e), pondéré(e), réfléchi(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI19 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 20. Je me sens de bonne humeur, aimable</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b><br>🔘 2 - <b>Plutôt non</b><br>🔘 3 - <b>Plutôt oui</b><br>🔘 4 - <b>Oui</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI20 </b></td> 
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


