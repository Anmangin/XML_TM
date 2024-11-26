<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='782096f3-fc2f-4631-9dc0-d17715452fe7' data-parent='9df2ff11-fb28-4ca9-8e3a-acbaef48ab82' data-type='form' data-label='TREATMENT ADMINISTRATION FORM'>
<h2> TREATMENT ADMINISTRATION FORM </h2>
<p>Liste des visites avec cette fiches :Cycle</p> 
<h3> TA1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Cycle number</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TACYCLE </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Treatment administered?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TAYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If no, specify the reason</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TA1.*][TA_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TA1][TAYN]== '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toxicity</b><br>🔘 2 - <b>Investigator’s decision</b><br>🔘 3 - <b>Organization problem</b><br>🔘 4 - <b>Patient refusal</b><br>🔘 5 - <b>Error</b><br>🔘 99 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TA_R </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify please</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TA1.*][TA_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TA1][TAYN]=='0'&&
[TA1][TA_R]=='99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TA_S </b></td> 
 </tr>
</table>

<h3> TADOSE </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date of treatment administration</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][TADOSE.*][TADT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TA1][TAYN] =='1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TADT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Theoretical total dose received during the cycle (mg)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DOSE_T </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Total dose received during this cycle (mg)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][TADOSE.*][DOSE]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TA1][TAYN]=='1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DOSE </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If total dose received is different from theoretical dose, reason</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][TADOSE.*][DOSEDIF_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TA1][TAYN] =='1' &&
!isEmpty([TRT][TADOSE][DOSE_T]) &&
!isEmpty([TRT][TADOSE][DOSE]) &&
[TRT][TADOSE][DOSE_T] != [TRT][TADOSE][DOSE]; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Dose modification during the cycle</b><br>🔘 2 - <b>Dose discontinuation during the cycle</b><br>🔘 3 - <b>Dose modification and discontinuation</b><br>🔘 99 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DOSEDIFR </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify please</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][TADOSE.*][DOSEDIF_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TA1][TAYN] =='1' &&
[TRT][TADOSE][DOSE] != [TRT][TADOSE][DOSE_T] &&
[TRT][TADOSE][DOSEDIF_R] =='99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DOSEDIFS </b></td> 
 </tr>
</table>

<h3> DMODIF </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Type of modification</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DMODIF.*][DMOD_T]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '1' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Dose reduced</b><br>🔘 2 - <b>Dose increased</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DMOD_T </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Reason for modification</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DMODIF.*][DMOD_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '1' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toxicity</b><br>🔘 2 - <b>Investigator’s decision</b><br>🔘 3 - <b>Organization problem</b><br>🔘 4 - <b>Patient refusal</b><br>🔘 5 - <b>Error</b><br>🔘 99 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DMODR </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify please</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DMODIF.*][DMOD_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([TRT][TADOSE][DOSEDIF_R] == '1' || [TRT][TADOSE][DOSEDIF_R] == '3') && [TRT][DMODIF][DMOD_R]=='99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DMODS </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Start date of dose modification</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 5:[TRT.*][DMODIF.*][DMOD_DT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '1' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Valid:[TRT.*][DMODIF.*][DMOD_DT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var dmodifdt = [TRT][DMODIF][DMOD_DT];
var date = [TRT][TADOSE][TADT];

isDate1LEDate2(date,dmodifdt); 
#data Expression 
 
</code></pre> </td><td> This item is invalid.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DMOD_DT </b></td> 
 </tr>
</table>

<h3> DISC </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Reason for discontinuation</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DISC.*][TADISC_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '2' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toxicity</b><br>🔘 2 - <b>Investigator’s decision</b><br>🔘 3 - <b>Organization problem</b><br>🔘 4 - <b>Patient refusal</b><br>🔘 5 - <b>Error</b><br>🔘 99 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TADISC_R </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify please</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DISC.*][TADISC_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([TRT][TADOSE][DOSEDIF_R] == '2' || [TRT][TADOSE][DOSEDIF_R] == '3') && 
[TRT][DISC][TADISC_R] == '99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TADISC_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Number of days of dose discontinuation during this cycle</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DISC.*][DISCNBD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '2' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DISCNBD </b></td> 
 </tr>
</table>

<h3> CYCLENXT </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Will the patient continue the treatment? If no, please complete the End of Treatment form</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CYCNXTYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> FLAG</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> DVA:[CYCLENXT.*][FLAG]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
if([CYCLENXT][CYCNXTYN] == '1')
   '1';
else
   ''; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 👻FLAG </b></td> 
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


