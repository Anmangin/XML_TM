## 5D3L 
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

### 5D3L 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL1 </b></td> 
 <td style='width:600px; text-align:left;'> Mobilité</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Je n’ai aucun problème pour me déplacer à pied.</b> <br>🔘 2 - <b>J’ai des problèmes pour me déplacer à pied.</b> <br>🔘 3 - <b>Je suis obligé(e) de rester alité(e).</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL2 </b></td> 
 <td style='width:600px; text-align:left;'> Autonomie de la personne</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1-Je n’ai aucun problème pour prendre soin de moi.</b> <br>🔘 2 - <b>2- J’ai des problèmes pour me laver ou m’habiller tout(e) seul(e).</b> <br>🔘 3 - <b>3-Je suis incapable de me laver ou de m’habiller tout(e) seul(e).</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL3 </b></td> 
 <td style='width:600px; text-align:left;'> Activités courantes</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1-Je n’ai aucun problème pour accomplir mes activités courantes</b> <br>🔘 2 - <b>2-J’ai des problèmes pour accomplir mes activités courantes.</b> <br>🔘 3 - <b>3-Je suis incapable d’accomplir mes activités courantes.</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL4 </b></td> 
 <td style='width:600px; text-align:left;'> Douleurs/gêne</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1-Je n’ai ni douleurs ni gêne.</b> <br>🔘 2 - <b>2-J’ai des douleurs ou une gêne modérée(s).</b> <br>🔘 3 - <b>3-J’ai des douleurs ou une gêne extrême(s).</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CDTL5 </b></td> 
 <td style='width:600px; text-align:left;'> Anxiété/Dépression</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>1-Je ne suis ni anxieux(se) ni déprimé(e).</b> <br>🔘 2 - <b>2-Je suis modérément anxieux(se) ou déprimé(e).</b> <br>🔘 3 - <b>3-Je suis extrêmement anxieux(se) ou déprimé(e).</b> <br> </td> 
 </tr>
</table>

