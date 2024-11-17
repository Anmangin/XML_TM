# Version de TB pour ce fichier : 5.0.3.27.Update 3b  
# Events 
## Progression 
### PD 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDYN </b></td> 
 <td style='width:600px; text-align:left;'> Did the patient progressed/relapsed?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDDT </b></td> 
 <td style='width:600px; text-align:left;'> Date of cancer progression or relapse</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDTYP </b></td> 
 <td style='width:600px; text-align:left;'> Progression or relapse?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDTYP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Progression</b> <br>🔘 2 - <b>Relapse</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDDIAGC </b></td> 
 <td style='width:600px; text-align:left;'> Diagnostic of progression or relapse based on:</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 1 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDIMGYN </b></td> 
 <td style='width:600px; text-align:left;'> Imaging</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDIMGYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDCLINYN </b></td> 
 <td style='width:600px; text-align:left;'> Clinical exam</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDCLINYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDBIOYN </b></td> 
 <td style='width:600px; text-align:left;'> Tumor markers</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDBIOYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDLOCYN </b></td> 
 <td style='width:600px; text-align:left;'> Local progression or relapse</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDLOCYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDREGYN </b></td> 
 <td style='width:600px; text-align:left;'> Regional progression or relapse</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDREGYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMETAYN </b></td> 
 <td style='width:600px; text-align:left;'> Metastasis progression or relapse</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMETAYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTLOC </b></td> 
 <td style='width:600px; text-align:left;'> If yes, specify location</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 1 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTBR </b></td> 
 <td style='width:600px; text-align:left;'> Brain</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTBR]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTLG </b></td> 
 <td style='width:600px; text-align:left;'> Lungs</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTLG]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTBN </b></td> 
 <td style='width:600px; text-align:left;'> Bones</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTBN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTLV </b></td> 
 <td style='width:600px; text-align:left;'> Liver</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTLV]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTOTH </b></td> 
 <td style='width:600px; text-align:left;'> Other</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTOTH]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PDMTOT_S </b></td> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[PD.*][PDMTOT_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PD][PDYN] == '1' && [PD][PDMETAYN] == '1' && [PD][PDMTOTH] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Num - 50 </td> 
 </tr>
</table>

