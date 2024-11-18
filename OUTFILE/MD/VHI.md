## Voice Handicap Index 
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

### VHIG1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF1 </b></td> 
 <td style='width:600px; text-align:left;'> F1. On a du mal à m'entendre à cause de ma voix.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF2 </b></td> 
 <td style='width:600px; text-align:left;'> F2. On me comprend difficilement dans un milieu bruyant.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF8 </b></td> 
 <td style='width:600px; text-align:left;'> F8. Mes problèmes de voix limitent ma vie personnelle et sociale.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF9 </b></td> 
 <td style='width:600px; text-align:left;'> F9. Je me sens exclu(e) des conversations à cause de ma voix.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIF10 </b></td> 
 <td style='width:600px; text-align:left;'> F10. Mes problèmes de voix entraînent une perte de revenu.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIP3 </b></td> 
 <td style='width:600px; text-align:left;'> P3. Les gens me posent des questions sur ma voix.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIP5 </b></td> 
 <td style='width:600px; text-align:left;'> P5. J'ai l'impression que je dois me forcer physiquement pour parler.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIP6 </b></td> 
 <td style='width:600px; text-align:left;'> P6. La clarté de ma voix est imprévisible.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIE4 </b></td> 
 <td style='width:600px; text-align:left;'> E4. Mes problèmes de voix me contrarient.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIE6 </b></td> 
 <td style='width:600px; text-align:left;'> E6. Je me sens handicapé(e) à cause de ma voix.</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Jamais</b> <br>🔘 1 - <b>Presque jamais</b> <br>🔘 2 - <b>Parfois</b> <br>🔘 3 - <b>Presque toujours</b> <br>🔘 4 - <b>Toujours</b> <br> </td> 
 </tr>
</table>

### VHIG2 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIVOICE </b></td> 
 <td style='width:600px; text-align:left;'> Comment votre voix est-elle aujourd'hui ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Normale (bonne qualité)</b> <br>🔘 1 - <b>Un peu anormale</b> <br>🔘 2 - <b>Assez anormale</b> <br>🔘 3 - <b>Très anormale</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VHIQOL </b></td> 
 <td style='width:600px; text-align:left;'> Sur une échelle de 0 à 10, à quel degré votre problème de voix influence-t-il votre qualité de vie ?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>0 Pas du tout</b> <br>🔘 1 - <b>1</b> <br>🔘 2 - <b>2</b> <br>🔘 3 - <b>3</b> <br>🔘 4 - <b>4</b> <br>🔘 5 - <b>5</b> <br>🔘 6 - <b>6</b> <br>🔘 7 - <b>7</b> <br>🔘 8 - <b>8</b> <br>🔘 9 - <b>9</b> <br>🔘 10 - <b>10 Enormément</b> <br> </td> 
 </tr>
</table>

