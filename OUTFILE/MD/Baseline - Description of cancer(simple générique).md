## Description of cancer 
Liste des visites avec cette fiches :Events 

### F08_1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DIAGDT </b></td> 
 <td style='width:600px; text-align:left;'> Date of initial diagnosis</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPTUMOR </b></td> 
 <td style='width:600px; text-align:left;'> Type of  tumor</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Acute lymphoblastic leukemia</b> <br>🔘 2 - <b>Acute myeloblastic leukemia</b> <br>🔘 3 - <b>Burkitt's lymphoma</b> <br>🔘 4 - <b>Hodgkin's lymphoma</b> <br>🔘 5 - <b>Neuroblastoma</b> <br>🔘 6 - <b>Medulloblastoma</b> <br>🔘 7 - <b>Atypical rhabdoid teratoid tumor</b> <br>🔘 8 - <b>Ewing sarcoma</b> <br>🔘 9 - <b>Osteosarcoma</b> <br>🔘 10 - <b>Undifferentiated carcinoma of nasopharyngeal type</b> <br>🔘 11 - <b>Wilms' tumor</b> <br>🔘 12 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPTUMOR_ </b></td> 
 <td style='width:600px; text-align:left;'> Other type of tumor,please specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[F08_1.*][TPTUMOR_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[F08_1][TPTUMOR] == '12' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> COMMENT </b></td> 
 <td style='width:600px; text-align:left;'> Comment</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 200 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Num - 50 </td> 
 </tr>
</table>

