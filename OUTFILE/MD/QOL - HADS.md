<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='e3a2537a-eef5-4965-b71e-a693ecb14d93' data-parent='b7e0bfe8-1e2f-4e73-a5bb-a735960d0608' data-type='form' data-label='HADS'>
<h2> HADS </h2>
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

<h3> HADSG1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je me sens tendu ou énervé</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>la plupart du temps</b><br>🔘 2 - <b>souvent</b><br>🔘 1 - <b>de temps en temps</b><br>🔘 0 - <b>jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS01 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai une sensation de peur comme si quelque chose d&apos;horrible allait m&apos;arriver</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>oui, très nettement</b><br>🔘 2 - <b>oui, mais ce n’est pas grave</b><br>🔘 1 - <b>un peu, mais cela ne m’inquiète pas</b><br>🔘 0 - <b>pas du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS02 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je me fais du souci</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>très souvent</b><br>🔘 2 - <b>assez souvent</b><br>🔘 1 - <b>occasionnellement</b><br>🔘 0 - <b>très occasionnellement</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS03 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je peux rester tranquillement assis à ne rien faire et me sentir d&amp;eacutecontract&amp;eacute</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>oui, quoi qu’il arrive</b><br>🔘 1 - <b>oui, en général</b><br>🔘 2 - <b>rarement</b><br>🔘 3 - <b>jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS04 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'&amp;eacuteprouve des sensations de peur et j'ai l'estomac nou&amp;eacute</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>jamais</b><br>🔘 1 - <b>parfois</b><br>🔘 2 - <b>assez souvent</b><br>🔘 3 - <b>très souvent</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS05 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J’ai la bougeotte et n’arrive pas à tenir en place</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>oui, c’est tout à fait le cas</b><br>🔘 2 - <b>un peu</b><br>🔘 1 - <b>pas tellement</b><br>🔘 0 - <b>pas du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS06 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'&amp;eacuteprouve des sensations soudaines de panique</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>vraiment très souvent</b><br>🔘 2 - <b>assez souvent</b><br>🔘 1 - <b>pas très souvent</b><br>🔘 0 - <b>jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS7 </b></td> 
 </tr>
</table>

<h3> HADSG2 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je prends plaisir aux mêmes choses qu’autrefois</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>oui, tout autant</b><br>🔘 1 - <b>pas autant</b><br>🔘 2 - <b>un peu seulement</b><br>🔘 3 - <b>presque plus</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS08 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je ris facilement et vois le bon côté des choses</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>autant que par le passé</b><br>🔘 2 - <b>plus autant qu’avant</b><br>🔘 1 - <b>vraiment moins qu’avant</b><br>🔘 0 - <b>plus du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS09 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je suis de bonne humeur</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>jamais</b><br>🔘 2 - <b>rarement</b><br>🔘 1 - <b>assez souvent</b><br>🔘 0 - <b>la plupart du temps</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS10 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J’ai l’impression de fonctionner au ralenti</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>presque toujours</b><br>🔘 2 - <b>très souvent</b><br>🔘 1 - <b>parfois</b><br>🔘 0 - <b>jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS11 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je ne m’intéresse plus à mon apparence</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>plus du tout</b><br>🔘 2 - <b>je n’y accorde pas autant d’attention que je le devrais</b><br>🔘 1 - <b>il se peut que je n’y fasse plus autant attention</b><br>🔘 0 - <b>j’y prête autant d’attention que par le passé</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS12 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je me r&amp;eacutejouis d'avance à l'idée de faire certaines choses</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>autant qu’auparavant</b><br>🔘 1 - <b>un peu moins qu’avant</b><br>🔘 2 - <b>bien moins qu’avant</b><br>🔘 3 - <b>presque jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS13 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je peux prendre plaisir &amp;agrave un bon livre ou &amp;agrave une bonne &amp;eacutemission radio ou de t&amp;eacutel&amp;eacutevision</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>souvent</b><br>🔘 1 - <b>parfois</b><br>🔘 2 - <b>rarement</b><br>🔘 3 - <b>très rarement</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS14 </b></td> 
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


