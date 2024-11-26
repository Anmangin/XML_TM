<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='84a15017-6051-4194-a8fd-0d259cc7a39a' data-parent='8b909dda-168c-48b3-9bb6-5a042ae53f2b' data-type='form' data-label='QLQC30_FR'>
<h2> QLQC30_FR </h2>
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
 <td style='width:600px; text-align:left;'> Questionnaire rempli par le patient</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQEYN </b></td> 
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
 <td style='width:600px; text-align:left;'> Date de remplissage du questionnaire par le patient</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQEHEAD.*][QLQEDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQEDT </b></td> 
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
 <td style='width:600px; text-align:left;'> Raison de non remplissage du questionnaire</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQEHEAD.*][QLQENO_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQEHEAD][QLQEYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQENO_R </b></td> 
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
 <tr> 
 <td style='width:600px; text-align:left;'> Date à laquelle le questionnaire aurait dû être rempli</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQEHEAD.*][QLQEEXPDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQEHEAD][QLQEYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQEEXPD </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 </tr>
</table>

<h3> QLQC30G1 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 1. Avez-vous des difficultés à faire certains efforts physiques prénibles comme porter un sac à provision chargé ou une valise ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q01]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q01 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 2. Avez-vous des difficultés à faire une LONGUE promenade ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q02]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q02 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 3. Avez-vous des difficultés à faire un PETIT tour dehors ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q03]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q03 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 4. Etes-vous obligé(e) de rester au lit ou dans un fauteuil pendant la journée ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q04]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q04 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 5. Avez-vous besoin d'aide pour manger, vous habiller, faire votre toilette ou aller aux WC ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q05]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q05 </b></td> 
 </tr>
</table>

<h3> QLQC30G2 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 6. Avez-vous été gêné(e) pour faire votre travail ou vos activités de tous les jours ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q06]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q06 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 7. Avez-vous été gêné(e) dans vos activités de loisirs ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q07]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q07 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 8. Avez-vous eu le souffle court ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q08]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q08 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 9. Avez-vous ressenti de la douleur ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q09]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q09 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 10. Avez-vous eu besoin de repos ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q10]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q10 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 11. Avez-vous eu des difficultés à dormir ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q11]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q11 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 12. Vous êtes-vous senti(e) faible ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q12]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q12 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 13. Avez-vous manqué d'appétit ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q13]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q13 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 14. Avez-vous eu des nausées (mal au coeur) ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q14]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q14 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 15. Avez-vous vomi ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q15]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q15 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 16. Avez-vous été constipé(e) ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q16]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q16 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 17. Avez-vous eu de la diarrhée ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q17]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q17 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 18. Etiez-vous fatigué(e) ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q18]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q18 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 19. Des douleurs ont-elles perturbé vos activités quotidiennes ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q19]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q19 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 20. Avez-vous eu des difficultés à vous concentrer sur certaines choses, par exemple, pour lire le journal ou regarder la télévision ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q20]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q20 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 21. Vous êtes-vous senti(e) tendu(e) ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q21]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q21 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 22. Vous êtes-vous fait du souci ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q22]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q22 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 23. Vous êtes-vous senti(e) irritable ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q23]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q23 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 24. Vous êtes-vous senti(e) déprimé(e) ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q24]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q24 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 25. Avez-vous eu des difficultés à vous souvenir de certaines choses ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q25]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q25 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 26. Votre état physique ou votre traitement médical vous ont-ils gêné(e) dans votre vie FAMILIALE ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q26]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q26 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 27. Votre état physique ou votre traitement médical vous ont-ils gêné(e) dans vos activités SOCIALES (par exemple, sortir avec des amis, aller au cinéma, ...) ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q27]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q27 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 28. Votre état physique ou votre traitement médical vous ont-ils causé des problèmes financiers ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q28]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b><br>🔘 2 - <b>Un peu</b><br>🔘 3 - <b>Assez</b><br>🔘 4 - <b>Beaucoup</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q28 </b></td> 
 </tr>
</table>

<h3> QLQC30G3 </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 29. Comment évalueriez-vous votre ETAT DE SANTE au cours de la semaine passée ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G3.*][Q29]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Valid:[Q29]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var q29 = [Q29];

Number(q29) >= 1 && Number(q29) <= 7; 
#data Expression 
 
</code></pre> </td><td> The answer to this question can only be between 1 and 7. Please verify and correct.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q29 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> 30. Comment évalueriez-vous l'ensemble de votre QUALITE DE VIE au cours de la semaine passée ?</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G3.*][Q30]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Valid:[Q30]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var q30 = [Q30];

Number(q30) >= 1 && Number(q30) <= 7; 
#data Expression 
 
</code></pre> </td><td> The answer to this question can only be between 1 and 7. Please verify and correct.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q30 </b></td> 
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


