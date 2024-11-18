# Fichier non compatible avec la version en cours de TM : actuel:5.0.3.27.Update 3b, version du fichier : 4.2.1.23  
# Quality of Life 
## HADS 
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

### HADSG1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS01 </b></td> 
 <td style='width:600px; text-align:left;'> Je me sens tendu ou énervé</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>la plupart du temps</b> <br>🔘 2 - <b>souvent</b> <br>🔘 1 - <b>de temps en temps</b> <br>🔘 0 - <b>jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS02 </b></td> 
 <td style='width:600px; text-align:left;'> J'ai une sensation de peur comme si quelque chose d&apos;horrible allait m&apos;arriver</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>oui, très nettement</b> <br>🔘 2 - <b>oui, mais ce n’est pas grave</b> <br>🔘 1 - <b>un peu, mais cela ne m’inquiète pas</b> <br>🔘 0 - <b>pas du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS03 </b></td> 
 <td style='width:600px; text-align:left;'> Je me fais du souci</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>très souvent</b> <br>🔘 2 - <b>assez souvent</b> <br>🔘 1 - <b>occasionnellement</b> <br>🔘 0 - <b>très occasionnellement</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS04 </b></td> 
 <td style='width:600px; text-align:left;'> Je peux rester tranquillement assis à ne rien faire et me sentir d&amp;eacutecontract&amp;eacute</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>oui, quoi qu’il arrive</b> <br>🔘 1 - <b>oui, en général</b> <br>🔘 2 - <b>rarement</b> <br>🔘 3 - <b>jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS05 </b></td> 
 <td style='width:600px; text-align:left;'> J'&amp;eacuteprouve des sensations de peur et j'ai l'estomac nou&amp;eacute</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>jamais</b> <br>🔘 1 - <b>parfois</b> <br>🔘 2 - <b>assez souvent</b> <br>🔘 3 - <b>très souvent</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS06 </b></td> 
 <td style='width:600px; text-align:left;'> J’ai la bougeotte et n’arrive pas à tenir en place</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>oui, c’est tout à fait le cas</b> <br>🔘 2 - <b>un peu</b> <br>🔘 1 - <b>pas tellement</b> <br>🔘 0 - <b>pas du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS7 </b></td> 
 <td style='width:600px; text-align:left;'> J'&amp;eacuteprouve des sensations soudaines de panique</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>vraiment très souvent</b> <br>🔘 2 - <b>assez souvent</b> <br>🔘 1 - <b>pas très souvent</b> <br>🔘 0 - <b>jamais</b> <br> </td> 
 </tr>
</table>

### HADSG2 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS08 </b></td> 
 <td style='width:600px; text-align:left;'> Je prends plaisir aux mêmes choses qu’autrefois</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>oui, tout autant</b> <br>🔘 1 - <b>pas autant</b> <br>🔘 2 - <b>un peu seulement</b> <br>🔘 3 - <b>presque plus</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS09 </b></td> 
 <td style='width:600px; text-align:left;'> Je ris facilement et vois le bon côté des choses</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>autant que par le passé</b> <br>🔘 2 - <b>plus autant qu’avant</b> <br>🔘 1 - <b>vraiment moins qu’avant</b> <br>🔘 0 - <b>plus du tout</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS10 </b></td> 
 <td style='width:600px; text-align:left;'> Je suis de bonne humeur</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>jamais</b> <br>🔘 2 - <b>rarement</b> <br>🔘 1 - <b>assez souvent</b> <br>🔘 0 - <b>la plupart du temps</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS11 </b></td> 
 <td style='width:600px; text-align:left;'> J’ai l’impression de fonctionner au ralenti</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>presque toujours</b> <br>🔘 2 - <b>très souvent</b> <br>🔘 1 - <b>parfois</b> <br>🔘 0 - <b>jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS12 </b></td> 
 <td style='width:600px; text-align:left;'> Je ne m’intéresse plus à mon apparence</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 3 - <b>plus du tout</b> <br>🔘 2 - <b>je n’y accorde pas autant d’attention que je le devrais</b> <br>🔘 1 - <b>il se peut que je n’y fasse plus autant attention</b> <br>🔘 0 - <b>j’y prête autant d’attention que par le passé</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS13 </b></td> 
 <td style='width:600px; text-align:left;'> Je me r&amp;eacutejouis d'avance à l'idée de faire certaines choses</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>autant qu’auparavant</b> <br>🔘 1 - <b>un peu moins qu’avant</b> <br>🔘 2 - <b>bien moins qu’avant</b> <br>🔘 3 - <b>presque jamais</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HADS14 </b></td> 
 <td style='width:600px; text-align:left;'> Je peux prendre plaisir &amp;agrave un bon livre ou &amp;agrave une bonne &amp;eacutemission radio ou de t&amp;eacutel&amp;eacutevision</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>souvent</b> <br>🔘 1 - <b>parfois</b> <br>🔘 2 - <b>rarement</b> <br>🔘 3 - <b>très rarement</b> <br> </td> 
 </tr>
</table>

