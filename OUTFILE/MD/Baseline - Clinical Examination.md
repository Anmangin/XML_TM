<body>


<h2> Vital sign and Clinical Examination  </h2>
Liste des visites avec cette fiches :Baseline 

<h3> VS1 </h3> 

<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
<tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Clinical Examination done ?</td>
 <td class='check' style='width:600px; text-align:left;'>   </td> <!--$htmlbalise--> 

 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b><br>🔘 1 - <b>Done</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSYN </b></td> 
 </tr> 
 <tr> 
 <td style='width:600px; text-align:left;'> Date of clinical assessment</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[VS.*][VS1.*][VSDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[VS][VS1][VSYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td> <!--$htmlbalise--> 

 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSDT </b></td> 
 </tr> 
</table>

<h3> VS2 </h3> 

<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
<tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Height (cm)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[HEIGHT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([HEIGHT] == '') ||
((140 <= [HEIGHT]) && ([HEIGHT] <= 200)) 
#data Expression 
 
</code></pre> </td><td> The height of the patient should be between 140 and 200cm. Please confirm the data.</td> </tr></table></details> </td> <!--$htmlbalise--> 

 <td style='width:300px; text-align:center;'> Num - 50 </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HEIGHT </b></td> 
 </tr> 
 <tr> 
 <td style='width:600px; text-align:left;'> WEIGHT (kg)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[WEIGHT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([WEIGHT] == '') ||
((40 <= [WEIGHT]) && ([WEIGHT] <= 180)) 
#data Expression 
 
</code></pre> </td><td> The weight of the patient should be between 40 and 180kg. Please confirm the data.</td> </tr></table></details> </td> <!--$htmlbalise--> 

 <td style='width:300px; text-align:center;'> Num - 50 </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> WEIGHT </b></td> 
 </tr> 
</table>

<h3> VS3 </h3> 

<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
<tr>
 <tr> 
 <td style='width:600px; text-align:left;'> PS (performance status measured using the ECOG Scale )</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[VSPS]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([VSPS] == '') ||
((0 <= [VSPS]) && ([VSPS] <= 4)) 
#data Expression 
 
</code></pre> </td><td> The ECOG performance status must be between 0 and 4. Please correct the data.</td> </tr></table></details> </td> <!--$htmlbalise--> 

 <td style='width:300px; text-align:center;'> Num - 50 </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSPS </b></td> 
 </tr> 
 <tr> 
 <td style='width:600px; text-align:left;'> Systolic blood pressure (mmHG)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[VSSYS]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([VSSYS] == '') ||
((90 <= [VSSYS]) && ([VSSYS] <= 160)) 
#data Expression 
 
</code></pre> </td><td> The systolic blood pressure (SBP) of the patient should be between 90 and 160 mmHg. Please confirm the data.</td> </tr></table></details> </td> <!--$htmlbalise--> 

 <td style='width:300px; text-align:center;'> Num - 50 </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSSYS </b></td> 
 </tr> 
 <tr> 
 <td style='width:600px; text-align:left;'> Diastolic blood pressure (mmHG)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[VSDIAG]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
([VSDIAG] == '') ||
((60 <= [VSDIAG]) && ([VSDIAG] <= 100)) 
#data Expression 
 
</code></pre> </td><td> The diastolic blood pressure (DBP) of the patient should be between 60 and 100 mmHg. Please confirm the data.</td> </tr></table></details> </td> <!--$htmlbalise--> 

 <td style='width:300px; text-align:center;'> Num - 50 </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> VSDIAG </b></td> 
 </tr> 
 <tr> 
 <td style='width:600px; text-align:left;'> ECG</td>
 <td class='check' style='width:600px; text-align:left;'>   </td> <!--$htmlbalise--> 

 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b><br>🔘 1 - <b>Done</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ECG </b></td> 
 </tr> 
 <tr> 
 <td style='width:600px; text-align:left;'> Date of ECG</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[VS.*][VS3.*][ECGDAT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[VS][VS1][VSYN] == '1' && [VS][VS3][ECG]=="1"; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td> <!--$htmlbalise--> 

 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ECGDAT </b></td> 
 </tr> 
</table>

</body>


