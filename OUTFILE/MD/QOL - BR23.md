## BR23 
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

### BR23G1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR31 </b></td> 
 <td style='width:600px; text-align:left;'> 31. Avez-vous eu la bouche sèche ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR32 </b></td> 
 <td style='width:600px; text-align:left;'> 32. La nourriture et la boisson avaient-elles un goût inhabituel ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR33 </b></td> 
 <td style='width:600px; text-align:left;'> 33. Est-ce que vos yeux étaient irrités, larmoyants ou douloureux ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR34 </b></td> 
 <td style='width:600px; text-align:left;'> 34. Avez-vous perdu des cheveux ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR35 </b></td> 
 <td style='width:600px; text-align:left;'> 35. Répondez à cette question uniquement si vous avez perdu des cheveux : la perte de vos cheveux vous a-t-elle contrariée ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR36 </b></td> 
 <td style='width:600px; text-align:left;'> 36. Vous êtes-vous sentie malade ou souffrante ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR37 </b></td> 
 <td style='width:600px; text-align:left;'> 37. Avez-vous eu des bouffées de chaleur ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR38 </b></td> 
 <td style='width:600px; text-align:left;'> 38. Avez-vous eu mal à la tête ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR39 </b></td> 
 <td style='width:600px; text-align:left;'> 39. Vous êtes-vous sentie moins attirante du fait de votre maladie ou de votre traitement ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR40 </b></td> 
 <td style='width:600px; text-align:left;'> 40. Vous êtes-vous sentie moins féminine du fait de votre maladie ou de votre traitement ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR41 </b></td> 
 <td style='width:600px; text-align:left;'> 41. Avez-vous trouvé difficile de vous regarder nue ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR42 </b></td> 
 <td style='width:600px; text-align:left;'> 42. Votre corps vous a-t-il déplu ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR43 </b></td> 
 <td style='width:600px; text-align:left;'> 43. Vous êtes-vous inquiétée de votre santé pour l'avenir ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
</table>

### BR23G2 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR44 </b></td> 
 <td style='width:600px; text-align:left;'> 44. Dans quelle mesure vous êtes-vous intéressée à la sexualité ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR45 </b></td> 
 <td style='width:600px; text-align:left;'> 45. Avez-vous eu une activité sexuelle quelconque (avec ou sans rapport) ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR46 </b></td> 
 <td style='width:600px; text-align:left;'> 46. Répondez à cette question uniquement si vous avez eu une activité sexuelle : dans quelle mesure l'activité sexuelle vous a-t-elle procuré du plaisir ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
</table>

### BR23G3 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR47 </b></td> 
 <td style='width:600px; text-align:left;'> 47. Avez-vous eu mal au bras ou à l'épaule ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR48 </b></td> 
 <td style='width:600px; text-align:left;'> 48. Avez-vous eu la main ou le bras enflé ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR49 </b></td> 
 <td style='width:600px; text-align:left;'> 49. Avez-vous eu du mal à lever le bras ou à le déplacer latéralement ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR50 </b></td> 
 <td style='width:600px; text-align:left;'> 50. Avez-vous ressenti des douleurs dans la région du sein traité ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR51 </b></td> 
 <td style='width:600px; text-align:left;'> 51. La région de votre sein traité était-elle enflée ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR52 </b></td> 
 <td style='width:600px; text-align:left;'> 52. La région de votre sein traité était-elle particulièrement sensible ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BR53 </b></td> 
 <td style='width:600px; text-align:left;'> 53. Avez-vous eu des problèmes de peau dans la région de votre sein traité (démangeaisons, peau qui pèle, peau sèche) ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1 - Pas du tout</b> <br>🔘 2 - <b>2 - Un peu</b> <br>🔘 3 - <b>3 - Assez</b> <br>🔘 4 - <b>4 - Beaucoup</b> <br> </td> 
 </tr>
</table>

