# ERREUR DANS LES DOSSIERS DU FICHIER  
Fiche/COMMUN est vide TBNodeId:89887
## F06 - Description of Prior Breast cancer disease 
Liste des visites avec cette fiches :Baseline 

### PRC1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Num - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> BIOP </b></td> 
 <td style='width:600px; text-align:left;'> Date of initial diagnosis \r\n<i>(first biopsy)</i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TUMSIDE </b></td> 
 <td style='width:600px; text-align:left;'> Side of primary</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Unilateral</b> <br>🔘 2 - <b>Bilateral</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TUMSIZE </b></td> 
 <td style='width:600px; text-align:left;'> Tumor size (mm)</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[F06 - Description of Prior Breast cancer disease.*][PRC1.*][TUMSIZE]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
Number([F06 - Description of Prior Breast cancer disease][PRC1][TUMSIZE])>0 
#data Expression 
 
</code></pre> </td><td> Size can't be 0</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 3 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> T </b></td> 
 <td style='width:600px; text-align:left;'> T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[F06 - Description of Prior Breast cancer disease.*][PRC1.*][T]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var size= Number([F06 - Description of Prior Breast cancer disease][PRC1][TUMSIZE]);
var t = [F06 - Description of Prior Breast cancer disease][PRC1][T];
isEmpty([F06 - Description of Prior Breast cancer disease][PRC1][TUMSIZE]) 
||
isEmpty([F06 - Description of Prior Breast cancer disease][PRC1][T])
||
(t = "T1" && size <= 20)
||
(t = "T2" && size <= 50 && size>20 )
||
(t = "T3" && size > 50)
||
(t = "T4" && size > 50) 
#data Expression 
 
</code></pre> </td><td> Lenth is not compatible with the T filled ([F06 - Description of Prior Breast cancer disease][PRC1][TUMSIZE]), please correct</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 Tx - <b>Tx - Primary tumor cannot be assessed</b> <br>🔘 T1 - <b>T1 - Tumor ≤ 20 mm in greatest dimension</b> <br>🔘 T2 - <b>T2 - Tumor > 20 mm but ≤ 50 mm in greatest dimension</b> <br>🔘 T3 - <b>T3 - Tumor > 50 mm in greatest dimension</b> <br>🔘 T4 - <b>T4 - Tumor of any size with direct extension to the chest wall and/or to the skin (ulceration or skin nodules)</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> N </b></td> 
 <td style='width:600px; text-align:left;'> N</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 Nx - <b>Nx - Regional lymph nodes cannot be assessed (for example, previously removed)</b> <br>🔘 N0 - <b>N0 - No regional lymph node metastases</b> <br>🔘 N+ - <b>N+ - Tumor of any size with direct extension to the chest wall and/or to the skin (ulceration or skin nodules)</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> N_LYMPH </b></td> 
 <td style='width:600px; text-align:left;'> ►Number of total invaded lymph nodes &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\r\n<i>if too many to count, fill with 99</i></td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[F06 - Description of Prior Breast cancer disease.*][PRC1.*][N_LYMPH]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[F06 - Description of Prior Breast cancer disease][PRC1][N] == 'N+' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 2 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Stage </b></td> 
 <td style='width:600px; text-align:left;'> Tumor Stage</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Stage I</b> <br>🔘 2 - <b>Stage II</b> <br>🔘 3 - <b>Stage III</b> <br>🔘 4 - <b>Stage IV</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> GRADE </b></td> 
 <td style='width:600px; text-align:left;'> Tumor grade</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Grade 1</b> <br>🔘 2 - <b>Grade 2</b> <br>🔘 3 - <b>Grade 3</b> <br>🔘 X - <b>Grade X</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HISTO </b></td> 
 <td style='width:600px; text-align:left;'> Histologic type</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Ductal</b> <br>🔘 2 - <b>Lobular</b> <br>🔘 3 - <b>Mixed ductal and lobular</b> <br>🔘 4 - <b>Unknown</b> <br>🔘 5 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HISTO_S </b></td> 
 <td style='width:600px; text-align:left;'> ►Other, specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[PRC1.*][HISTO_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PRC1][HISTO] == '5'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
</table>

### PRC2 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ERR </b></td> 
 <td style='width:600px; text-align:left;'> ER receptor</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Negative</b> <br>🔘 1 - <b>Positive</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> PRR </b></td> 
 <td style='width:600px; text-align:left;'> PR receptor</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Negative</b> <br>🔘 1 - <b>Positive</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Ki67 </b></td> 
 <td style='width:600px; text-align:left;'> Ki67</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b> <br>🔘 1 - <b>Done</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> KI_PCT </b></td> 
 <td style='width:600px; text-align:left;'> ►Ki67 staining (%)</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[PRC2.*][KI_PCT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[PRC2][Ki67] == '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 3 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HER2 </b></td> 
 <td style='width:600px; text-align:left;'> HER2</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Negative</b> <br>🔘 1 - <b>Positive</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> FISH </b></td> 
 <td style='width:600px; text-align:left;'> FISH</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not amplified</b> <br>🔘 1 - <b>Amplified</b> <br>🔘 9 - <b>Not done</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HER2_RES </b></td> 
 <td style='width:600px; text-align:left;'> HER2 Immunohistochemistry</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>0</b> <br>🔘 1 - <b>1+</b> <br>🔘 2 - <b>2+</b> <br>🔘 3 - <b>+3</b> <br>🔘 99 - <b>Not done</b> <br> </td> 
 </tr>
</table>

