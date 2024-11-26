<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='7c8500a3-27fa-47f1-80d3-a1a1b2a519a1' data-parent='fcd47032-d8b3-42e8-99d8-85660e1ec957' data-type='form' data-label='F06 - Description of Prior Breast cancer disease'>
<h2> F06 - Description of Prior Breast cancer disease </h2>
<p>Liste des visites avec cette fiches :Baseline</p> 
<h3> PRC1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date of initial diagnosis \r\n<i>(first biopsy)</i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BIOP </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Side of primary</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Unilateral</b><br>🔘 2 - <b>Bilateral</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TUMSIDE </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Tumor size (mm)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[F06 - Description of Prior Breast cancer disease.*][PRC1.*][TUMSIZE]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
Number([F06 - Description of Prior Breast cancer disease][PRC1][TUMSIZE])>0 
#data Expression 
 
</code></pre> </td><td> Size can't be 0</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TUMSIZE </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[F06 - Description of Prior Breast cancer disease.*][PRC1.*][T]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var size= Number([F06 - Description of Prior Breast cancer disease][PRC1][TUMSIZE]);
var t = [F06 - Description of Prior Breast cancer disease][PRC1][T];
isEmpty([F06 - Description of Prior Breast cancer disease][PRC1][TUMSIZE]) 
||
isEmpty([F06 - Description of Prior Breast cancer disease][PRC1][T])
||
(t = "T1" && size <= 20)
||
(t = "T2" && size <= 50 && size>20 )
||
(t = "T3" && size > 50)
||
(t = "T4" && size > 50) 
#data Expression 
 
</code></pre> </td><td> Lenth is not compatible with the T filled ([F06 - Description of Prior Breast cancer disease][PRC1][TUMSIZE]), please correct</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 Tx - <b>Tx - Primary tumor cannot be assessed</b><br>🔘 T1 - <b>T1 - Tumor ≤ 20 mm in greatest dimension</b><br>🔘 T2 - <b>T2 - Tumor > 20 mm but ≤ 50 mm in greatest dimension</b><br>🔘 T3 - <b>T3 - Tumor > 50 mm in greatest dimension</b><br>🔘 T4 - <b>T4 - Tumor of any size with direct extension to the chest wall and/or to the skin (ulceration or skin nodules)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> T </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> N</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 Nx - <b>Nx - Regional lymph nodes cannot be assessed (for example, previously removed)</b><br>🔘 N0 - <b>N0 - No regional lymph node metastases</b><br>🔘 N+ - <b>N+ - Tumor of any size with direct extension to the chest wall and/or to the skin (ulceration or skin nodules)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> N </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> ►Number of total invaded lymph nodes &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n<i>if too many to count, fill with 99</i></td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[F06 - Description of Prior Breast cancer disease.*][PRC1.*][N_LYMPH]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[F06 - Description of Prior Breast cancer disease][PRC1][N] == 'N+' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> N_LYMPH </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Tumor Stage</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Stage I</b><br>🔘 2 - <b>Stage II</b><br>🔘 3 - <b>Stage III</b><br>🔘 4 - <b>Stage IV</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Stage </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Tumor grade</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Grade 1</b><br>🔘 2 - <b>Grade 2</b><br>🔘 3 - <b>Grade 3</b><br>🔘 X - <b>Grade X</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> GRADE </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Histologic type</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Ductal</b><br>🔘 2 - <b>Lobular</b><br>🔘 3 - <b>Mixed ductal and lobular</b><br>🔘 4 - <b>Unknown</b><br>🔘 5 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HISTO </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> ►Other, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[PRC1.*][HISTO_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PRC1][HISTO] == '5'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HISTO_S </b></td> 
 </tr>
</table>

<h3> PRC2 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> ER receptor</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Negative</b><br>🔘 1 - <b>Positive</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ERR </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> PR receptor</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Negative</b><br>🔘 1 - <b>Positive</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRR </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Ki67</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b><br>🔘 1 - <b>Done</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Ki67 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> ►Ki67 staining (%)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[PRC2.*][KI_PCT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PRC2][Ki67] == '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> KI_PCT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> HER2</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Negative</b><br>🔘 1 - <b>Positive</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HER2 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> FISH</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not amplified</b><br>🔘 1 - <b>Amplified</b><br>🔘 9 - <b>Not done</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FISH </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> HER2 Immunohistochemistry</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>0</b><br>🔘 1 - <b>1+</b><br>🔘 2 - <b>2+</b><br>🔘 3 - <b>+3</b><br>🔘 99 - <b>Not done</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HER2_RES </b></td> 
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


