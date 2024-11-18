# Fichier non compatible avec la version en cours de TM : actuel:5.0.3.27.Update 3b, version du fichier : 4.2.1.23  
## SWAL-QOL 
Liste des visites avec cette fiches :Quality of Life 

### QLQHEAD 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQYN </b></td> 
 <td style='width:600px; text-align:left;'> Questionnaire rempli par le patient</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQDT </b></td> 
 <td style='width:600px; text-align:left;'> Date de remplissage du questionnaire par le patient</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQHEAD.*][QLQDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQHEAD][QLQYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQNO_R </b></td> 
 <td style='width:600px; text-align:left;'> Raison de non remplissage du questionnaire</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQHEAD.*][QLQNO_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQHEAD][QLQYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQEXPDT </b></td> 
 <td style='width:600px; text-align:left;'> Date à laquelle le questionnaire aurait dû être rempli</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQHEAD.*][QLQEXPDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQHEAD][QLQYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
</table>

### SWALG1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL01 </b></td> 
 <td style='width:600px; text-align:left;'> Vivre avec mes troubles de déglutition est difficile ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL02 </b></td> 
 <td style='width:600px; text-align:left;'> Mes problèmes de déglutition sont une gêne majeure dans ma vie ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
</table>

### SWALG2 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL03 </b></td> 
 <td style='width:600px; text-align:left;'> Presque tous les jours, je ne fais pas attention si je mange ou pas</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL04 </b></td> 
 <td style='width:600px; text-align:left;'> Je prends plus de temps que les autres pour manger</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL05 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai rarement faim</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL06 </b></td> 
 <td style='width:600px; text-align:left;'> Mon repas me prend beaucoup de temps</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL07 </b></td> 
 <td style='width:600px; text-align:left;'> Je ne prends plus de plaisir à manger</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
</table>

### SWALG3 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL08 </b></td> 
 <td style='width:600px; text-align:left;'> Je tousse</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL09 </b></td> 
 <td style='width:600px; text-align:left;'> Je m'étouffe en mangeant des aliments</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL10 </b></td> 
 <td style='width:600px; text-align:left;'> Je m'étouffe en buvant</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL11 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai une salive épaisse et/ou des glaires</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL12 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai envie de vomir</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL13 </b></td> 
 <td style='width:600px; text-align:left;'> Je me racle la gorge</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL14 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai des problèmes pour mâcher</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL15 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai trop de salive ou de crachats</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL16 </b></td> 
 <td style='width:600px; text-align:left;'> Je n'arrive pas à me dégager la gorge</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL17 </b></td> 
 <td style='width:600px; text-align:left;'> Les aliments restent coincés dans ma gorge</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL18 </b></td> 
 <td style='width:600px; text-align:left;'> Les aliments restent collés dans ma bouche</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL19 </b></td> 
 <td style='width:600px; text-align:left;'> Les aliments ou les liquides ressortent par ma bouche</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL20 </b></td> 
 <td style='width:600px; text-align:left;'> Les aliments ou les liquides ressortent par mon nez</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL21 </b></td> 
 <td style='width:600px; text-align:left;'> Je n'arrive pas à tousser quand les aliments sont coincés</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
</table>

### SWALG4 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL22 </b></td> 
 <td style='width:600px; text-align:left;'> Le choix de mes aliments est difficile</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b> <br>🔘 2 - <b>D'accord</b> <br>🔘 3 - <b>Incertain</b> <br>🔘 4 - <b>Pas d'accord</b> <br>🔘 5 - <b>Pas du tout d'accord</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL23 </b></td> 
 <td style='width:600px; text-align:left;'> Il est difficile de trouver une alimentation adaptée que j'aime</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b> <br>🔘 2 - <b>D'accord</b> <br>🔘 3 - <b>Incertain</b> <br>🔘 4 - <b>Pas d'accord</b> <br>🔘 5 - <b>Pas du tout d'accord</b> <br> </td> 
 </tr>
</table>

### SWALG5 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL24 </b></td> 
 <td style='width:600px; text-align:left;'> Les gens ont du mal à comprendre ce que je dis</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b> <br>🔘 2 - <b>La plupart du temps</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Quelques fois</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL25 </b></td> 
 <td style='width:600px; text-align:left;'> C'est difficile pour moi de parler clairement</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b> <br>🔘 2 - <b>La plupart du temps</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Quelques fois</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
</table>

### SWALG6 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL26 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai peur d'étouffer en mangeant</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL27 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai peur d'avoir une pneumonie</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL28 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai peur de m'étouffer quand je bois</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL29 </b></td> 
 <td style='width:600px; text-align:left;'> Je ne sais jamais si je vais étouffer</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b> <br>🔘 2 - <b>Souvent</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Rarement</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
</table>

### SWALG7 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL30 </b></td> 
 <td style='width:600px; text-align:left;'> Ma déglutition me déprime</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL31 </b></td> 
 <td style='width:600px; text-align:left;'> Je suis gêné(e) par ma déglutition</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL32 </b></td> 
 <td style='width:600px; text-align:left;'> Je suis contrarié(e) par ma déglutition</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL33 </b></td> 
 <td style='width:600px; text-align:left;'> Mes problèmes de déglutition sont frustrants</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL34 </b></td> 
 <td style='width:600px; text-align:left;'> Je suis impatient(e) de régler ce problème</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b> <br>🔘 2 - <b>Souvent vrai</b> <br>🔘 3 - <b>Parfois vrai</b> <br>🔘 4 - <b>Rarement vrai</b> <br>🔘 5 - <b>Pas vrai du tout</b> <br> </td> 
 </tr>
</table>

### SWALG8 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL35 </b></td> 
 <td style='width:600px; text-align:left;'> Je ne mange plus à l'extérieur</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b> <br>🔘 2 - <b>D'accord</b> <br>🔘 3 - <b>Incertain</b> <br>🔘 4 - <b>Pas d'accord</b> <br>🔘 5 - <b>Pas du tout d'accord</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL36 </b></td> 
 <td style='width:600px; text-align:left;'> C'est difficile d'avoir une vie sociale</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b> <br>🔘 2 - <b>D'accord</b> <br>🔘 3 - <b>Incertain</b> <br>🔘 4 - <b>Pas d'accord</b> <br>🔘 5 - <b>Pas du tout d'accord</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL37 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai changé de travail et/ou de loisirs à cause de ces problèmes</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b> <br>🔘 2 - <b>D'accord</b> <br>🔘 3 - <b>Incertain</b> <br>🔘 4 - <b>Pas d'accord</b> <br>🔘 5 - <b>Pas du tout d'accord</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL38 </b></td> 
 <td style='width:600px; text-align:left;'> Je ne profite plus des fêtes ou des vacances</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b> <br>🔘 2 - <b>D'accord</b> <br>🔘 3 - <b>Incertain</b> <br>🔘 4 - <b>Pas d'accord</b> <br>🔘 5 - <b>Pas du tout d'accord</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL39 </b></td> 
 <td style='width:600px; text-align:left;'> Ma position vis à vis de ma famille ou de mes amis a changé</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b> <br>🔘 2 - <b>D'accord</b> <br>🔘 3 - <b>Incertain</b> <br>🔘 4 - <b>Pas d'accord</b> <br>🔘 5 - <b>Pas du tout d'accord</b> <br> </td> 
 </tr>
</table>

### SWALG9 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL40 </b></td> 
 <td style='width:600px; text-align:left;'> Je me sens faible</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b> <br>🔘 2 - <b>La plupart du temps</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Quelques fois</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL41 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai des problèmes pour dormir</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b> <br>🔘 2 - <b>La plupart du temps</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Quelques fois</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL42 </b></td> 
 <td style='width:600px; text-align:left;'> Je suis fatigué(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b> <br>🔘 2 - <b>La plupart du temps</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Quelques fois</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL43 </b></td> 
 <td style='width:600px; text-align:left;'> Je me réveille la nuit</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b> <br>🔘 2 - <b>La plupart du temps</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Quelques fois</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL44 </b></td> 
 <td style='width:600px; text-align:left;'> Je me sens épuisé(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b> <br>🔘 2 - <b>La plupart du temps</b> <br>🔘 3 - <b>Parfois</b> <br>🔘 4 - <b>Quelques fois</b> <br>🔘 5 - <b>Jamais</b> <br> </td> 
 </tr>
</table>

### SWALG10 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL45 </b></td> 
 <td style='width:600px; text-align:left;'> Quelqu'un vous a t'il aidé à remplir ce questionnaire ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Non, je l'ai fait seul</b> <br>🔘 1 - <b>Oui quelqu'un m'a aidé</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL46 </b></td> 
 <td style='width:600px; text-align:left;'> Si quelqu'un vous a aidé, comment l'a t'il fait ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Il a lu les questions et écrit vos réponses</b> <br>🔘 2 - <b>A répondu aux questions pour vous ?</b> <br>🔘 3 - <b>A fait autre chose</b> <br> </td> 
 </tr>
</table>

