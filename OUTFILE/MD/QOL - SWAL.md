<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='c862df0b-cb2a-40d1-a61e-fd764cbcb3c1' data-parent='7e89fe53-84a3-46ea-8e2b-1afe3c979c61' data-type='form' data-label='SWAL-QOL'>
<h2> SWAL-QOL </h2>
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

<h3> SWALG1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Vivre avec mes troubles de déglutition est difficile ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL01 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Mes problèmes de déglutition sont une gêne majeure dans ma vie ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL02 </b></td> 
 </tr>
</table>

<h3> SWALG2 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Presque tous les jours, je ne fais pas attention si je mange ou pas</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL03 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je prends plus de temps que les autres pour manger</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL04 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai rarement faim</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL05 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Mon repas me prend beaucoup de temps</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL06 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je ne prends plus de plaisir à manger</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL07 </b></td> 
 </tr>
</table>

<h3> SWALG3 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je tousse</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL08 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je m'étouffe en mangeant des aliments</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL09 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je m'étouffe en buvant</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL10 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai une salive épaisse et/ou des glaires</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL11 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai envie de vomir</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL12 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je me racle la gorge</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL13 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai des problèmes pour mâcher</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL14 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai trop de salive ou de crachats</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL15 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je n'arrive pas à me dégager la gorge</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL16 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Les aliments restent coincés dans ma gorge</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL17 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Les aliments restent collés dans ma bouche</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL18 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Les aliments ou les liquides ressortent par ma bouche</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL19 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Les aliments ou les liquides ressortent par mon nez</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL20 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je n'arrive pas à tousser quand les aliments sont coincés</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL21 </b></td> 
 </tr>
</table>

<h3> SWALG4 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Le choix de mes aliments est difficile</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b><br>🔘 2 - <b>D'accord</b><br>🔘 3 - <b>Incertain</b><br>🔘 4 - <b>Pas d'accord</b><br>🔘 5 - <b>Pas du tout d'accord</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL22 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Il est difficile de trouver une alimentation adaptée que j'aime</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b><br>🔘 2 - <b>D'accord</b><br>🔘 3 - <b>Incertain</b><br>🔘 4 - <b>Pas d'accord</b><br>🔘 5 - <b>Pas du tout d'accord</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL23 </b></td> 
 </tr>
</table>

<h3> SWALG5 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Les gens ont du mal à comprendre ce que je dis</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b><br>🔘 2 - <b>La plupart du temps</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL24 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> C'est difficile pour moi de parler clairement</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b><br>🔘 2 - <b>La plupart du temps</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL25 </b></td> 
 </tr>
</table>

<h3> SWALG6 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai peur d'étouffer en mangeant</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL26 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai peur d'avoir une pneumonie</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL27 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai peur de m'étouffer quand je bois</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL28 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je ne sais jamais si je vais étouffer</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours</b><br>🔘 2 - <b>Souvent</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL29 </b></td> 
 </tr>
</table>

<h3> SWALG7 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Ma déglutition me déprime</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL30 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je suis gêné(e) par ma déglutition</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL31 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je suis contrarié(e) par ma déglutition</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL32 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Mes problèmes de déglutition sont frustrants</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL33 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je suis impatient(e) de régler ce problème</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toujours vrai</b><br>🔘 2 - <b>Souvent vrai</b><br>🔘 3 - <b>Parfois vrai</b><br>🔘 4 - <b>Rarement vrai</b><br>🔘 5 - <b>Pas vrai du tout</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL34 </b></td> 
 </tr>
</table>

<h3> SWALG8 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je ne mange plus à l'extérieur</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b><br>🔘 2 - <b>D'accord</b><br>🔘 3 - <b>Incertain</b><br>🔘 4 - <b>Pas d'accord</b><br>🔘 5 - <b>Pas du tout d'accord</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL35 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> C'est difficile d'avoir une vie sociale</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b><br>🔘 2 - <b>D'accord</b><br>🔘 3 - <b>Incertain</b><br>🔘 4 - <b>Pas d'accord</b><br>🔘 5 - <b>Pas du tout d'accord</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL36 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai changé de travail et/ou de loisirs à cause de ces problèmes</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b><br>🔘 2 - <b>D'accord</b><br>🔘 3 - <b>Incertain</b><br>🔘 4 - <b>Pas d'accord</b><br>🔘 5 - <b>Pas du tout d'accord</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL37 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je ne profite plus des fêtes ou des vacances</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b><br>🔘 2 - <b>D'accord</b><br>🔘 3 - <b>Incertain</b><br>🔘 4 - <b>Pas d'accord</b><br>🔘 5 - <b>Pas du tout d'accord</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL38 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Ma position vis à vis de ma famille ou de mes amis a changé</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout à fait d'accord</b><br>🔘 2 - <b>D'accord</b><br>🔘 3 - <b>Incertain</b><br>🔘 4 - <b>Pas d'accord</b><br>🔘 5 - <b>Pas du tout d'accord</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL39 </b></td> 
 </tr>
</table>

<h3> SWALG9 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je me sens faible</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b><br>🔘 2 - <b>La plupart du temps</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL40 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> J'ai des problèmes pour dormir</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b><br>🔘 2 - <b>La plupart du temps</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL41 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je suis fatigué(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b><br>🔘 2 - <b>La plupart du temps</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL42 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je me réveille la nuit</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b><br>🔘 2 - <b>La plupart du temps</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL43 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Je me sens épuisé(e)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Tout le temps</b><br>🔘 2 - <b>La plupart du temps</b><br>🔘 3 - <b>Parfois</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL44 </b></td> 
 </tr>
</table>

<h3> SWALG10 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Quelqu'un vous a t'il aidé à remplir ce questionnaire ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Non, je l'ai fait seul</b><br>🔘 1 - <b>Oui quelqu'un m'a aidé</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL45 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Si quelqu'un vous a aidé, comment l'a t'il fait ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Il a lu les questions et écrit vos réponses</b><br>🔘 2 - <b>A répondu aux questions pour vous ?</b><br>🔘 3 - <b>A fait autre chose</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SWAL46 </b></td> 
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


