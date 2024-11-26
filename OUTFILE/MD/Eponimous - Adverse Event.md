<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='6743bcec-d7ce-410f-8877-a667bcfa9546' data-parent='da0079c6-646f-4f1a-a060-1079721bdb1b' data-type='form' data-label='Adverse Event'>
<h2> Adverse Event </h2>
<p>Liste des visites avec cette fiches :Adverse Events</p> 
<h3> AE1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Verbatim</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AETERM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> description of event</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEDESC </b></td> 
 </tr>
</table>

<h3> AE2 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> CTCAE SOC</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 Radio bouton trop long </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AESOC </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> CTCAE Term</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Dynamic codelist filter:[Adverse Event.*][AE2.*][AEPT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
if ([Adverse Event][AE2][AESOC] == 1) '1';
else if ([Adverse Event][AE2][AESOC] == 2) '2';
else if ([Adverse Event][AE2][AESOC] == 3) '3';
else if ([Adverse Event][AE2][AESOC] == 4) '4';
else if ([Adverse Event][AE2][AESOC] == 5) '5';
else if ([Adverse Event][AE2][AESOC] == 6) '6';
else if ([Adverse Event][AE2][AESOC] == 7) '7';
else if ([Adverse Event][AE2][AESOC] == 8) '8';
else if ([Adverse Event][AE2][AESOC] == 9) '9';
else if ([Adverse Event][AE2][AESOC] == 10) '10';
else if ([Adverse Event][AE2][AESOC] == 11) '11';
else if ([Adverse Event][AE2][AESOC] == 12) '12';
else if ([Adverse Event][AE2][AESOC] == 13) '13';
else if ([Adverse Event][AE2][AESOC] == 14) '14';
else if ([Adverse Event][AE2][AESOC] == 15) '15';
else if ([Adverse Event][AE2][AESOC] == 16) '16';
else if ([Adverse Event][AE2][AESOC] == 17) '17';
else if ([Adverse Event][AE2][AESOC] == 18) '18';
else if ([Adverse Event][AE2][AESOC] == 19) '19';
else if ([Adverse Event][AE2][AESOC] == 20) '20';
else if ([Adverse Event][AE2][AESOC] == 21) '21';
else if ([Adverse Event][AE2][AESOC] == 22) '22';
else if ([Adverse Event][AE2][AESOC] == 23) '23';
else if ([Adverse Event][AE2][AESOC] == 24) '24';
else if ([Adverse Event][AE2][AESOC] == 25) '25';
else if ([Adverse Event][AE2][AESOC] == 26) '26'; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 Radio bouton trop long </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEPT </b></td> 
 </tr>
</table>

<h3> AE3 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Ongoing  at the <br> beginning of treatment</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[Adverse Event.*][AE3.*][AESGO]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
isEmpty([Adverse Event][AE3][AESDT]); 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AESGO </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Start date <i>(if day is not know, fill with UK e.g : UK/01/2001)</i></td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[Adverse Event.*][AE3.*][AESDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Adverse Event][AE3][AESGO] != '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AESDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Ongoing at <br>the end of treatment  and/or <br> at the end of short-time follow up</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[Adverse Event.*][AE3.*][AEEGO]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
isEmpty([Adverse Event][AE3][AEEDT]); 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEEGO </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> End date <i>(if day or month is not know, fill with UK e.g : UK/UK/2001)</i></td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> Valid:[Adverse Event.*][AE3.*][AEEDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
isDate1LEDate2([Adverse Event][AE3][AESDT],[Adverse Event][AE3][AEEDT]); 
#data Expression 
 
</code></pre> </td><td> The toxicity end date has to be after the toxicity start date, please correct.</td> </tr><tr><td> Enabled:[Adverse Event.*][AE3.*][AEEDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Adverse Event][AE3][AEEGO] != '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEEDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Cycle at which the event <u>started</u></td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[Adverse Event.*][AE3.*][AECYCLE]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Adverse Event][AE3][AESGO] != '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AECYCLE </b></td> 
 </tr>
</table>

<h3> AE4 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Grade</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[AEGR]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[AEGR] > 0 && [AEGR] < 6; 
#data Expression 
 
</code></pre> </td><td> The grade should be between 1 and 5. Please correct.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEGR </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> DLT</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEDLT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> <b><font color="#ff0033">SAE</font></b></td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AESER </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> FLAG</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> DVC:[Adverse Event.*][AE4.*][FLAG]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
'1' 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 👻FLAG </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 </tr>
</table>

<h3> AE5 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date of SAE reporting to PV</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AESERDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> CIOMS Number</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[AECIOMS]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var cioms = [AECIOMS];
var lg = cioms.length;

lg == 9 || lg == 0; 
#data Expression 
 
</code></pre> </td><td> The CIOMS number must contain 9 digits. Please correct.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AECIOMS </b></td> 
 </tr>
</table>

<h3> AE6 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Related to</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Drug 1</b><br>🔘 2 - <b>Drug 2</b><br>🔘 3 - <b>Drug 3</b><br>🔘 4 - <b>Cancer</b><br>🔘 99 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEREL </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> <font color="#0033ff">If other, specify</font></td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[Adverse Event.*][AE6.*][AEREL_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Adverse Event][AE6][AEREL] == '99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEREL_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Action</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>No action</b><br>🔘 1 - <b>Action 1</b><br>🔘 2 - <b>Action 2</b><br>🔘 99 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEACN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> <font color="#0033ff">If other, specify</font></td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[Adverse Event.*][AE6.*][AEACN_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Adverse Event][AE6][AEACN] == '99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AEACN_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Treatment required</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> AETRTYN </b></td> 
 </tr>
</table>

<h3> AEMEDDRA </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Verbatim term:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒MEDVERB </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> SOC code:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒SOCCOD </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> SOC name:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒SOCNAM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> PT code:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒PTCOD </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> PT term:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒PTNAM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> LLT code:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒LLTCOD </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> LLT term</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒LLTNAM </b></td> 
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


