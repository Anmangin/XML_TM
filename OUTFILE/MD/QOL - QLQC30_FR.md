## QLQC30_FR 
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
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQEYN </b></td> 
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
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQEDT </b></td> 
 <td style='width:600px; text-align:left;'> Date de remplissage du questionnaire par le patient</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQEHEAD.*][QLQEDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQEHEAD][QLQEYN] == '1'; 
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
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQENO_R </b></td> 
 <td style='width:600px; text-align:left;'> Raison de non remplissage du questionnaire</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQEHEAD.*][QLQENO_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQEHEAD][QLQEYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 200 </td> 
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
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> QLQEEXPD </b></td> 
 <td style='width:600px; text-align:left;'> Date à laquelle le questionnaire aurait dû être rempli</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQEHEAD.*][QLQEEXPDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQEHEAD][QLQEYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Num - 50 </td> 
 </tr>
</table>

### QLQC30G1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q01 </b></td> 
 <td style='width:600px; text-align:left;'> 1. Avez-vous des difficultés à faire certains efforts physiques prénibles comme porter un sac à provision chargé ou une valise ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q01]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q02 </b></td> 
 <td style='width:600px; text-align:left;'> 2. Avez-vous des difficultés à faire une LONGUE promenade ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q02]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q03 </b></td> 
 <td style='width:600px; text-align:left;'> 3. Avez-vous des difficultés à faire un PETIT tour dehors ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q03]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q04 </b></td> 
 <td style='width:600px; text-align:left;'> 4. Etes-vous obligé(e) de rester au lit ou dans un fauteuil pendant la journée ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q04]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q05 </b></td> 
 <td style='width:600px; text-align:left;'> 5. Avez-vous besoin d'aide pour manger, vous habiller, faire votre toilette ou aller aux WC ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G1.*][Q05]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
</table>

### QLQC30G2 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q06 </b></td> 
 <td style='width:600px; text-align:left;'> 6. Avez-vous été gêné(e) pour faire votre travail ou vos activités de tous les jours ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q06]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q07 </b></td> 
 <td style='width:600px; text-align:left;'> 7. Avez-vous été gêné(e) dans vos activités de loisirs ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q07]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q08 </b></td> 
 <td style='width:600px; text-align:left;'> 8. Avez-vous eu le souffle court ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q08]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q09 </b></td> 
 <td style='width:600px; text-align:left;'> 9. Avez-vous ressenti de la douleur ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q09]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q10 </b></td> 
 <td style='width:600px; text-align:left;'> 10. Avez-vous eu besoin de repos ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q10]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q11 </b></td> 
 <td style='width:600px; text-align:left;'> 11. Avez-vous eu des difficultés à dormir ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q11]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q12 </b></td> 
 <td style='width:600px; text-align:left;'> 12. Vous êtes-vous senti(e) faible ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q12]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q13 </b></td> 
 <td style='width:600px; text-align:left;'> 13. Avez-vous manqué d'appétit ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q13]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q14 </b></td> 
 <td style='width:600px; text-align:left;'> 14. Avez-vous eu des nausées (mal au coeur) ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q14]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q15 </b></td> 
 <td style='width:600px; text-align:left;'> 15. Avez-vous vomi ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q15]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q16 </b></td> 
 <td style='width:600px; text-align:left;'> 16. Avez-vous été constipé(e) ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q16]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q17 </b></td> 
 <td style='width:600px; text-align:left;'> 17. Avez-vous eu de la diarrhée ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q17]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q18 </b></td> 
 <td style='width:600px; text-align:left;'> 18. Etiez-vous fatigué(e) ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q18]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q19 </b></td> 
 <td style='width:600px; text-align:left;'> 19. Des douleurs ont-elles perturbé vos activités quotidiennes ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q19]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q20 </b></td> 
 <td style='width:600px; text-align:left;'> 20. Avez-vous eu des difficultés à vous concentrer sur certaines choses, par exemple, pour lire le journal ou regarder la télévision ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q20]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q21 </b></td> 
 <td style='width:600px; text-align:left;'> 21. Vous êtes-vous senti(e) tendu(e) ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q21]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q22 </b></td> 
 <td style='width:600px; text-align:left;'> 22. Vous êtes-vous fait du souci ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q22]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q23 </b></td> 
 <td style='width:600px; text-align:left;'> 23. Vous êtes-vous senti(e) irritable ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q23]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q24 </b></td> 
 <td style='width:600px; text-align:left;'> 24. Vous êtes-vous senti(e) déprimé(e) ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q24]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q25 </b></td> 
 <td style='width:600px; text-align:left;'> 25. Avez-vous eu des difficultés à vous souvenir de certaines choses ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q25]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q26 </b></td> 
 <td style='width:600px; text-align:left;'> 26. Votre état physique ou votre traitement médical vous ont-ils gêné(e) dans votre vie FAMILIALE ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q26]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q27 </b></td> 
 <td style='width:600px; text-align:left;'> 27. Votre état physique ou votre traitement médical vous ont-ils gêné(e) dans vos activités SOCIALES (par exemple, sortir avec des amis, aller au cinéma, ...) ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q27]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q28 </b></td> 
 <td style='width:600px; text-align:left;'> 28. Votre état physique ou votre traitement médical vous ont-ils causé des problèmes financiers ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G2.*][Q28]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Pas du tout</b> <br>🔘 2 - <b>Un peu</b> <br>🔘 3 - <b>Assez</b> <br>🔘 4 - <b>Beaucoup</b> <br> </td> 
 </tr>
</table>

### QLQC30G3 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q29 </b></td> 
 <td style='width:600px; text-align:left;'> 29. Comment évalueriez-vous votre ETAT DE SANTE au cours de la semaine passée ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G3.*][Q29]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Valid:[Q29]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var q29 = [Q29];

Number(q29) >= 1 && Number(q29) <= 7; 
#data Expression 
 
</code></pre> </td><td> The answer to this question can only be between 1 and 7. Please verify and correct.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 1 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Q30 </b></td> 
 <td style='width:600px; text-align:left;'> 30. Comment évalueriez-vous l'ensemble de votre QUALITE DE VIE au cours de la semaine passée ?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 5:[QLQC30_FR.*][QLQC30G3.*][Q30]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[QLQC30_FR][QLQEHEAD][QLQEYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Valid:[Q30]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var q30 = [Q30];

Number(q30) >= 1 && Number(q30) <= 7; 
#data Expression 
 
</code></pre> </td><td> The answer to this question can only be between 1 and 7. Please verify and correct.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 1 </td> 
 </tr>
</table>

