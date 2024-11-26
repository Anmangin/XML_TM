<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='313cf5b9-f307-4a77-a123-7f9db3755f5b' data-parent='a9bff01d-2cfe-4812-85f2-e7b31b28dc59' data-type='form' data-label='SF-36'>
<h2> SF-36 </h2>
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

<h3> SF36G1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 1. Dans l'ensemble, pensez-vous que votre santé est :</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Excellente</b><br>🔘 2 - <b>Très bonne</b><br>🔘 3 - <b>Bonne</b><br>🔘 4 - <b>Médiocre</b><br>🔘 5 - <b>Mauvaise</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFGH1 </b></td> 
 </tr>
</table>

<h3> SF36G2 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 2. Par rapport au même jour de la semaine dernière, comment trouvez-vous votre état de santé en ce moment ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Bien meilleur que la semaine dernière</b><br>🔘 2 - <b>Plutôt meilleur</b><br>🔘 3 - <b>À peu près pareil</b><br>🔘 4 - <b>Plutôt moins bon</b><br>🔘 5 - <b>Beaucoup moins bon</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFHT </b></td> 
 </tr>
</table>

<h3> SF36G3 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> a. Efforts physiques importants tels que courir, soulever un objet lourd, faire du sport</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP1 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> b. Efforts physiques modérés tels que déplacer une table, passer l'aspirateur, jouer aux boules</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP2 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> c. Soulever et porter les courses</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP3 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> d. Monter plusieurs étages par l'escalier</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP4 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> e. Monter un étage par l'escalier</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP5 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> f. Se pencher en avant, se mettre à genoux, s'accroupir</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP6 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> g. Marcher plus d'un km à pied</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP7 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> h. Marcher plusieurs centaines de mètres</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP8 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> i. Marcher une centaine de mètres</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP9 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> j. Prendre un bain, une douche ou s'habiller</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Oui, beaucoup limité(e)</b><br>🔘 2 - <b>Oui, un peu limité(e)</b><br>🔘 3 - <b>Non, pas du tout limité(e)</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFP10 </b></td> 
 </tr>
</table>

<h3> SF36G4 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> a. Avez-vous réduit le temps passé à votre travail ou à vos activités habituelles ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Quelques fois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFR1 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> b. Avez-vous accompli moins de choses que vous auriez souhaité ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Quelques fois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFRP2 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> c. Avez-vous dû arrêter de faire certaines choses ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Quelques fois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFRP3 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> d. Avez-vous eu des difficultés à faire votre travail ou toute autre activité ? (par exemple, cela vous a demandé un effort supplémentaire)</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Quelques fois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFRP4 </b></td> 
 </tr>
</table>

<h3> SF36G5 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> a. Avez-vous réduit le temps passé à votre travail ou à vos activités habituelles ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Quelques fois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFRE1 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> b. Avez-vous accompli moins de choses que vous auriez souhaité ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Quelques fois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFRE2 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> c. Avez-vous eu des difficultés à faire ce que vous aviez à faire avec autant de soin et d'attention que d'habitude ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Quelques fois</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFRE3 </b></td> 
 </tr>
</table>

<h3> SF36G6 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 6. Au cours de cette dernière semaine dans quelle mesure votre état de santé, physique ou émotionnel, vous a-t-il gêné(e) dans votre vie sociale et vos relations avec les autres, votre famille, vos amis, vos connaissances</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un petit peu</b><br>🔘 3 - <b>Moyennement</b><br>🔘 4 - <b>Beaucoup</b><br>🔘 5 - <b>Enormément</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFSF1 </b></td> 
 </tr>
</table>

<h3> SF36G7 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 7. Au cours de cette dernière semaine, quelle a été l'intensité de vos douleurs physiques ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Nulle</b><br>🔘 2 - <b>Très faible</b><br>🔘 3 - <b>Faible</b><br>🔘 4 - <b>Moyenne</b><br>🔘 5 - <b>Grande</b><br>🔘 6 - <b>Très grande</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFBP1 </b></td> 
 </tr>
</table>

<h3> SF36G8 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 8. Au cours de cette dernière semaine, dans quelle mesure vos douleurs physiques vous ont-elles limité(e) dans votre travail ou vos activités domestiques ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un petit peu</b><br>🔘 3 - <b>Moyennement</b><br>🔘 4 - <b>Beaucoup</b><br>🔘 5 - <b>Enormément</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFBP2 </b></td> 
 </tr>
</table>

<h3> SF36G9 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> a. vous vous êtes senti(e) dynamique ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Souvent</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Rarement</b><br>🔘 6 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFVT1 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> b. vous vous êtes senti(e) très nerveux(se) ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Souvent</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Rarement</b><br>🔘 6 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFMH1 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> c. vous vous êtes senti(e) si découragé(e) que rien ne pouvait vous remonter le moral ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Souvent</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Rarement</b><br>🔘 6 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFMH2 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> d. vous vous êtes senti(e) calme et détendu(e) ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Souvent</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Rarement</b><br>🔘 6 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFMH3 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> e. vous vous êtes senti(e) débordant(e) d'énergie ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Souvent</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Rarement</b><br>🔘 6 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFVT2 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> f. vous vous êtes senti(e) triste et abattu(e) ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Souvent</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Rarement</b><br>🔘 6 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFMH4 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> g. vous vous êtes senti(e) épuisé(e) ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Souvent</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Rarement</b><br>🔘 6 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFVT3 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> h. vous vous êtes senti(e) heureux(se) ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Souvent</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Rarement</b><br>🔘 6 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFMH5 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> i. vous vous êtes senti(e) fatigué(e) ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Très souvent</b><br>🔘 3 - <b>Souvent</b><br>🔘 4 - <b>Quelques fois</b><br>🔘 5 - <b>Rarement</b><br>🔘 6 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFVT4 </b></td> 
 </tr>
</table>

<h3> SF36G10 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 10. Au cours de cette dernière semaine, y a-t-il eu des moments où votre état de santé, physique ou émotionnel, vous a gêné(e) dans votre vie et vos relations avec les autres, votre famille, vos amis, vos connaissances ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>En permanence</b><br>🔘 2 - <b>Une bonne partie du temps</b><br>🔘 3 - <b>De temps en temps</b><br>🔘 4 - <b>Rarement</b><br>🔘 5 - <b>Jamais</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFSF2 </b></td> 
 </tr>
</table>

<h3> SF36G11 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> a. Je tombe malade plus facilement que les autres</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Totalement vraie</b><br>🔘 2 - <b>Plutôt vraie</b><br>🔘 3 - <b>Je ne sais pas</b><br>🔘 4 - <b>Plutôt fausse</b><br>🔘 5 - <b>Totalement fausse</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFGH2 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> b. Je me porte aussi bien que n'importe qui</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Totalement vraie</b><br>🔘 2 - <b>Plutôt vraie</b><br>🔘 3 - <b>Je ne sais pas</b><br>🔘 4 - <b>Plutôt fausse</b><br>🔘 5 - <b>Totalement fausse</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFGH3 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> c. Je m'attends à ce que ma santé se dégrade</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Totalement vraie</b><br>🔘 2 - <b>Plutôt vraie</b><br>🔘 3 - <b>Je ne sais pas</b><br>🔘 4 - <b>Plutôt fausse</b><br>🔘 5 - <b>Totalement fausse</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFGH4 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> d. Je suis en excellente santé</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Totalement vraie</b><br>🔘 2 - <b>Plutôt vraie</b><br>🔘 3 - <b>Je ne sais pas</b><br>🔘 4 - <b>Plutôt fausse</b><br>🔘 5 - <b>Totalement fausse</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q0SFGH5 </b></td> 
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


