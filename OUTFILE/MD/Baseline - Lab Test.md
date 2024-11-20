## Laboratory Tests 
Liste des visites avec cette fiches :Baseline 

### LAB1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LabRND </b></td> 
 <td style='width:600px; text-align:left;'> Tests Not done</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 200 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LabDT </b></td> 
 <td style='width:600px; text-align:left;'> Date of sampling</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[Laboratory Tests.*][LAB1.*][LabDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Laboratory Tests][LAB1][LabRND] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LABVTIME </b></td> 
 <td style='width:600px; text-align:left;'> Visit timepoint</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 6 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Labname </b></td> 
 <td style='width:600px; text-align:left;'> Name of the laboratory</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[Laboratory Tests.*][LAB1.*][Labname]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Laboratory Tests][LAB1][LabRND] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒LABCOM </b></td> 
 <td style='width:600px; text-align:left;'> <font color="#ff0000">A significantly abnormal laboratory value should be reported in the AE section.\r\n\r\nAn abnormal laboratory value is considered significant if it has a grade ≥2 according to NCI-CTCAE v5.0.</font></td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 1 </td> 
 </tr>
</table>

### LAB2 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LabtestN </b></td> 
 <td style='width:600px; text-align:left;'> Laboratory Test</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LABND </b></td> 
 <td style='width:600px; text-align:left;'> Not done</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> DVA:[Laboratory Tests.*][LAB2.*][LABND]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
if ([Laboratory Tests][LAB1][LabRND] == '1') '1'
else [Laboratory Tests][LAB2][LABND]; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 200 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LABTESTR </b></td> 
 <td style='width:600px; text-align:left;'> Result</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[Laboratory Tests.*][LAB2.*][LabtestR]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Laboratory Tests][LAB2][LABND] == 0; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Normal</b> <br>🔘 2 - <b>Abnormal (Not Clinically Significant)</b> <br>🔘 3 - <b>Abnormal (Clinically Significant)</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LabtestV </b></td> 
 <td style='width:600px; text-align:left;'> Value</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[Laboratory Tests.*][LAB2.*][LabtestV]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Laboratory Tests][LAB2][LabtestR] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 8 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒LabUnits </b></td> 
 <td style='width:600px; text-align:left;'> Units</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒LLN </b></td> 
 <td style='width:600px; text-align:left;'> LLN</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒labtestM </b></td> 
 <td style='width:600px; text-align:left;'> ULN</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 👻ExportUn </b></td> 
 <td style='width:600px; text-align:left;'> Export unit</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
</table>

