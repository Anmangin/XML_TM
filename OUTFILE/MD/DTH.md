# Version de TB pour ce fichier : 5.0.3.27.Update 3b  
# Events 
## Death 
### DTH 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DTHDT </b></td> 
 <td style='width:600px; text-align:left;'> Date of death</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DTH_R </b></td> 
 <td style='width:600px; text-align:left;'> Primary cause of death</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Cancer</b> <br>🔘 2 - <b>Toxicity due to study treatment</b> <br>🔘 3 - <b>Second cancer</b> <br>🔘 4 - <b>Intercurrent illness</b> <br>🔘 5 - <b>Unknown</b> <br>🔘 99 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DTH_S </b></td> 
 <td style='width:600px; text-align:left;'> Specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[DTH.*][DTH_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[DTH][DTH_R] == '2' || [DTH][DTH_R] == '4' || [DTH][DTH_R] == '99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 200 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Num - 50 </td> 
 </tr>
</table>

