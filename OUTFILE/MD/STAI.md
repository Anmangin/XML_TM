# Version de TB pour ce fichier : 4.2.1.23  
# Fichier non compatible avec la version en cours de TM : actuel:5.0.3.27.Update 3b, version du fichier : 4.2.1.23  
# Quality of Life 
## STAI 
### QLQHEAD 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
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

### STAI 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI01 </b></td> 
 <td style='width:600px; text-align:left;'> 1. Je me sens calme</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI02 </b></td> 
 <td style='width:600px; text-align:left;'> 2. Je me sens en sécurité, sans inquiétude, en sûreté</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI03 </b></td> 
 <td style='width:600px; text-align:left;'> 3. Je suis tendu(e), crispé(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI04 </b></td> 
 <td style='width:600px; text-align:left;'> 4. Je me sens surmené(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI05 </b></td> 
 <td style='width:600px; text-align:left;'> 5. Je me sens tranquille, bien dans ma peau</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI06 </b></td> 
 <td style='width:600px; text-align:left;'> 6. Je me sens ému(e), bouleversé(e), contrarié(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI07 </b></td> 
 <td style='width:600px; text-align:left;'> 7. L'idée de malheurs éventuels me tracasse en ce moment</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI08 </b></td> 
 <td style='width:600px; text-align:left;'> 8. Je me sens content(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI09 </b></td> 
 <td style='width:600px; text-align:left;'> 9. Je me sens effrayé(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI10 </b></td> 
 <td style='width:600px; text-align:left;'> 10. Je me sens à mon aise</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI11 </b></td> 
 <td style='width:600px; text-align:left;'> 11. Je sens que j'ai confiance en moi</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI12 </b></td> 
 <td style='width:600px; text-align:left;'> 12. Je me sens nerveux(se), irritable</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI13 </b></td> 
 <td style='width:600px; text-align:left;'> 13. J'ai la frousse, la trouille j'ai peur</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI14 </b></td> 
 <td style='width:600px; text-align:left;'> 14. Je me sens indécis(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI15 </b></td> 
 <td style='width:600px; text-align:left;'> 15. Je suis décontracté(e), détendu(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI16 </b></td> 
 <td style='width:600px; text-align:left;'> 16. Je suis satisfait(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI17 </b></td> 
 <td style='width:600px; text-align:left;'> 17. Je suis inquièt(e), soucieux(se)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI18 </b></td> 
 <td style='width:600px; text-align:left;'> 18. Je ne sais plus où j'en suis, je me sens déconcerté(e), dérouté(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI19 </b></td> 
 <td style='width:600px; text-align:left;'> 19. Je me sens solide, posé(e), pondéré(e), réfléchi(e)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STAI20 </b></td> 
 <td style='width:600px; text-align:left;'> 20. Je me sens de bonne humeur, aimable</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Non</b> <br>🔘 2 - <b>Plutôt non</b> <br>🔘 3 - <b>Plutôt oui</b> <br>🔘 4 - <b>Oui</b> <br> </td> 
 </tr>
</table>
