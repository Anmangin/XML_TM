# ERREUR DANS LES DOSSIERS DU FICHIER  
Fiche/COMMUN est vide TBNodeId:92255
## Prior chemotherapy 
Liste des visites avec cette fiches :Baseline 

### SYSTYN 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SYSTYN </b></td> 
 <td style='width:600px; text-align:left;'> Prior Chemotherapy / Target Therapy / Immunotherapy:</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PACNB </b></td> 
 <td style='width:600px; text-align:left;'> Total number of prior anticancer lines\r\nPlease one line by prior anticancer lines in the following table.</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[Prior chemotherapy.*][SYSTYN.*][PACNB]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Prior chemotherapy][SYSTYN][SYSTYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 2 </td> 
 </tr>
</table>

### SYST 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TRTTYP </b></td> 
 <td style='width:600px; text-align:left;'> Nature of treatment</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Chemotherapy & immunotherapy</b> <br>🔘 2 - <b>Target therapy</b> <br>🔘 3 - <b>Immunotherapy only</b> <br>🔘 4 - <b>Chemotherapy only</b> <br>🔘 5 - <b>other systemic treatment</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PROTO </b></td> 
 <td style='width:600px; text-align:left;'> Name of protocol</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRFOR </b></td> 
 <td style='width:600px; text-align:left;'> Treatment for</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Locally/locally advanced disease</b> <br>🔘 2 - <b>Metastatic disease</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DRG </b></td> 
 <td style='width:600px; text-align:left;'> <b>Name of drugs\r\n</b>(one or more drugs in one row)<i>\r\n</i></td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SYSTSDT </b></td> 
 <td style='width:600px; text-align:left;'> Start date</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SYSTEDT </b></td> 
 <td style='width:600px; text-align:left;'> End date</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[Prior chemotherapy.*][SYST.*][SYSTEDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var db=[Prior chemotherapy][SYST.@][SYSTSDT];
var fn = [Prior chemotherapy][SYST.@][SYSTEDT];

isDate1LEDate2(db,fn); 
#data Expression 
 
</code></pre> </td><td> la date de fin est avant la date de début, merci de corriger.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRSTOP_R </b></td> 
 <td style='width:600px; text-align:left;'> Reason of stop</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Progression</b> <br>🔘 2 - <b>Toxicity</b> <br>🔘 3 - <b>Complete remission</b> <br>🔘 4 - <b>Partial remission</b> <br>🔘 5 - <b>End of protocole</b> <br>🔘 6 - <b>Patient's choice</b> <br>🔘 7 - <b>Other, please specify</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRSTOP_S </b></td> 
 <td style='width:600px; text-align:left;'> other reason, please specify</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRPROGDT </b></td> 
 <td style='width:600px; text-align:left;'> Date of progression</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[Prior chemotherapy.*][SYST.*][PRPROGDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Prior chemotherapy][SYST.@][PRSTOP_R] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
</table>

