## TREATMENT ADMINISTRATION FORM 
Liste des visites avec cette fiches :Cycle 

### TA1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TACYCLE </b></td> 
 <td style='width:600px; text-align:left;'> Cycle number</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Num - 3 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TAYN </b></td> 
 <td style='width:600px; text-align:left;'> Treatment administered?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TA_R </b></td> 
 <td style='width:600px; text-align:left;'> If no, specify the reason</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TA1.*][TA_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TA1][TAYN]== '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toxicity</b> <br>🔘 2 - <b>Investigator’s decision</b> <br>🔘 3 - <b>Organization problem</b> <br>🔘 4 - <b>Patient refusal</b> <br>🔘 5 - <b>Error</b> <br>🔘 99 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TA_S </b></td> 
 <td style='width:600px; text-align:left;'> If other, specify please</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TA1.*][TA_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TA1][TAYN]=='0'&&
[TA1][TA_R]=='99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
</table>

### TADOSE 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TADT </b></td> 
 <td style='width:600px; text-align:left;'> Date of treatment administration</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][TADOSE.*][TADT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TA1][TAYN] =='1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DOSE_T </b></td> 
 <td style='width:600px; text-align:left;'> Theoretical total dose received during the cycle (mg)</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Num - 5 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DOSE </b></td> 
 <td style='width:600px; text-align:left;'> Total dose received during this cycle (mg)</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][TADOSE.*][DOSE]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TA1][TAYN]=='1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 5 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DOSEDIFR </b></td> 
 <td style='width:600px; text-align:left;'> If total dose received is different from theoretical dose, reason</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][TADOSE.*][DOSEDIF_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TA1][TAYN] =='1' &&
!isEmpty([TRT][TADOSE][DOSE_T]) &&
!isEmpty([TRT][TADOSE][DOSE]) &&
[TRT][TADOSE][DOSE_T] != [TRT][TADOSE][DOSE]; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Dose modification during the cycle</b> <br>🔘 2 - <b>Dose discontinuation during the cycle</b> <br>🔘 3 - <b>Dose modification and discontinuation</b> <br>🔘 99 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DOSEDIFS </b></td> 
 <td style='width:600px; text-align:left;'> If other, specify please</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][TADOSE.*][DOSEDIF_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TA1][TAYN] =='1' &&
[TRT][TADOSE][DOSE] != [TRT][TADOSE][DOSE_T] &&
[TRT][TADOSE][DOSEDIF_R] =='99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
</table>

### DMODIF 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DMOD_T </b></td> 
 <td style='width:600px; text-align:left;'> Type of modification</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DMODIF.*][DMOD_T]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '1' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Dose reduced</b> <br>🔘 2 - <b>Dose increased</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DMODR </b></td> 
 <td style='width:600px; text-align:left;'> Reason for modification</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DMODIF.*][DMOD_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '1' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toxicity</b> <br>🔘 2 - <b>Investigator’s decision</b> <br>🔘 3 - <b>Organization problem</b> <br>🔘 4 - <b>Patient refusal</b> <br>🔘 5 - <b>Error</b> <br>🔘 99 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DMODS </b></td> 
 <td style='width:600px; text-align:left;'> If other, specify please</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DMODIF.*][DMOD_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([TRT][TADOSE][DOSEDIF_R] == '1' || [TRT][TADOSE][DOSEDIF_R] == '3') && [TRT][DMODIF][DMOD_R]=='99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DMOD_DT </b></td> 
 <td style='width:600px; text-align:left;'> Start date of dose modification</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 5:[TRT.*][DMODIF.*][DMOD_DT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '1' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Valid:[TRT.*][DMODIF.*][DMOD_DT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var dmodifdt = [TRT][DMODIF][DMOD_DT];
var date = [TRT][TADOSE][TADT];

isDate1LEDate2(date,dmodifdt); 
#data Expression 
 
</code></pre> </td><td> This item is invalid.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
</table>

### DISC 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TADISC_R </b></td> 
 <td style='width:600px; text-align:left;'> Reason for discontinuation</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DISC.*][TADISC_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '2' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Toxicity</b> <br>🔘 2 - <b>Investigator’s decision</b> <br>🔘 3 - <b>Organization problem</b> <br>🔘 4 - <b>Patient refusal</b> <br>🔘 5 - <b>Error</b> <br>🔘 99 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TADISC_S </b></td> 
 <td style='width:600px; text-align:left;'> If other, specify please</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DISC.*][TADISC_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([TRT][TADOSE][DOSEDIF_R] == '2' || [TRT][TADOSE][DOSEDIF_R] == '3') && 
[TRT][DISC][TADISC_R] == '99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DISCNBD </b></td> 
 <td style='width:600px; text-align:left;'> Number of days of dose discontinuation during this cycle</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[TRT.*][DISC.*][DISCNBD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[TRT][TADOSE][DOSEDIF_R] == '2' ||
[TRT][TADOSE][DOSEDIF_R] == '3'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 3 </td> 
 </tr>
</table>

### CYCLENXT 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CYCNXTYN </b></td> 
 <td style='width:600px; text-align:left;'> Will the patient continue the treatment? If no, please complete the End of Treatment form</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 👻FLAG </b></td> 
 <td style='width:600px; text-align:left;'> FLAG</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> DVA:[CYCLENXT.*][FLAG]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
if([CYCLENXT][CYCNXTYN] == '1')
   '1';
else
   ''; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
</table>

