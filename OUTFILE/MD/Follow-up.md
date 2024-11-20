## Follow-Up 
Liste des visites avec cette fiches :Follow-Up 

### FU 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUYN </b></td> 
 <td style='width:600px; text-align:left;'> During this follow-up visit, did you have any information on the patient?</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUNO_R </b></td> 
 <td style='width:600px; text-align:left;'> If no, reason</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUNO_R]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Consent withdrawn</b> <br>🔘 2 - <b>Lost to follow-up</b> <br>🔘 99 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUNO_S </b></td> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUNO_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '0' && [FU][FUNO_R] == '99'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 200 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUDT </b></td> 
 <td style='width:600px; text-align:left;'> Date of last news</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUDT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUCS </b></td> 
 <td style='width:600px; text-align:left;'> Status of the patient</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUCS]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Alive</b> <br>🔘 1 - <b>Dead</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUCOM </b></td> 
 <td style='width:600px; text-align:left;'> <i><font color="#993333">If alive</font></i></td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 1 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUDISCS </b></td> 
 <td style='width:600px; text-align:left;'> Disease state?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUDISCS]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Complete response</b> <br>🔘 2 - <b>Partial response</b> <br>🔘 3 - <b>Stable disease</b> <br>🔘 4 - <b>Progressive disease</b> <br>🔘 5 - <b>Not evaluable</b> <br>🔘 6 - <b>Unknown</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FU2NDK </b></td> 
 <td style='width:600px; text-align:left;'> Occurrence of a second cancer?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FU2NDK]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUTRTGO </b></td> 
 <td style='width:600px; text-align:left;'> New anticancer treatment ongoing?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUTRTGO]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUTRT_S </b></td> 
 <td style='width:600px; text-align:left;'> If yes, treatment name</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUTRT_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0' && [FU][FUTRTGO] == '1'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 200 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUSAEYN </b></td> 
 <td style='width:600px; text-align:left;'> SAE since the last visit?</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUSAEYN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FUSAE_S </b></td> 
 <td style='width:600px; text-align:left;'> If yes, term(s)</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> 5:[FU.*][FUSAE_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[FU][FUYN] == '1' && [FU][FUCS] == '0' && [FU][FUSAEYN] == '1'; 
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

