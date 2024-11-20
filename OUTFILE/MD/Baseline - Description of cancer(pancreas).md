# ERREUR DANS LES DOSSIERS DU FICHIER  
unknown/loc est vide TBNodeId:91038
## F07 : Description of disease 
Liste des visites avec cette fiches :Baseline 

### 1-Initial diagnosis 

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
 <td style='width:600px; text-align:left;'> Date of primary tumor diagnosis</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCPRIM </b></td> 
 <td style='width:600px; text-align:left;'> Primary location not found</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCBODY </b></td> 
 <td style='width:600px; text-align:left;'> Body of pancreas</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Body of pancreas]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCHEAD </b></td> 
 <td style='width:600px; text-align:left;'> Head of pancreas</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Head of pancreas]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCTAIL </b></td> 
 <td style='width:600px; text-align:left;'> Tail of pancreas</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Tail of pancreas]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Other__s </b></td> 
 <td style='width:600px; text-align:left;'> Other, specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Other specify]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCDIAG_ </b></td> 
 <td style='width:600px; text-align:left;'> Other location ,specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Other location specify]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0' && [1-Initial diagnosis][Other specify] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
</table>

### 2 - At the time of the inclusion 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TNM </b></td> 
 <td style='width:600px; text-align:left;'> <u>TNM stage:</u></td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 1 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STGIT </b></td> 
 <td style='width:600px; text-align:left;'> T - ENETS:</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>T1</b> <br>🔘 2 - <b>T2</b> <br>🔘 3 - <b>T3</b> <br>🔘 4 - <b>T4</b> <br>🔘 0 - <b>Tx</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STGIN </b></td> 
 <td style='width:600px; text-align:left;'> N:</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>N0</b> <br>🔘 1 - <b>N1</b> <br>🔘 2 - <b>N2</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STGIM </b></td> 
 <td style='width:600px; text-align:left;'> M:</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>M0</b> <br>🔘 1 - <b>M1</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HGRAD </b></td> 
 <td style='width:600px; text-align:left;'> Histologic grading at inclusion</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Grade 1</b> <br>🔘 2 - <b>Grade 2</b> <br>🔘 3 - <b>Grade 3</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> L1 </b></td> 
 <td style='width:600px; text-align:left;'> <font color="#ffffff">.</font></td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 1 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METAINC </b></td> 
 <td style='width:600px; text-align:left;'> Presence of metastasis at inclusion:</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METADT </b></td> 
 <td style='width:600px; text-align:left;'> If yes, date of appearance of first metastasis:</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> Enabled:[Description of disease.*][2 - At the time of the inclusion.*][If yes_ date of appearance of first metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Description of disease][2 - At the time of the inclusion][Presence of metastasis at inclusion]=='1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> Valid:[Description of disease.*][2 - At the time of the inclusion.*][If yes_ date of appearance of first metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
DaysBetween([Description of disease][1-Initial diagnosis][Date of primary tumor diagnosis],[Description of disease][2 - At the time of the inclusion][If yes_ date of appearance of first metastasis])>=0 || isNaN(DaysBetween([Description of disease][1-Initial diagnosis][Date of primary tumor diagnosis],[Description of disease][2 - At the time of the inclusion][If yes_ date of appearance of first metastasis])) 
#data Expression 
 
</code></pre> </td><td> This date should be after (or equal) date of primary tumor diagnosis</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METABRAI </b></td> 
 <td style='width:600px; text-align:left;'> Brain metastasis</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Brain metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METABONE </b></td> 
 <td style='width:600px; text-align:left;'> bone metastasis</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][bone metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METALIVE </b></td> 
 <td style='width:600px; text-align:left;'> Liver metastasis</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Liver metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MLIVINV </b></td> 
 <td style='width:600px; text-align:left;'> If liver, involment > 50 %</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][If liver involment SUP 50 ]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Liver metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>No</b> <br>🔘 1 - <b>Yes</b> <br>🔘 2 - <b>Unknown</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METAPERI </b></td> 
 <td style='width:600px; text-align:left;'> Peritoneal cavity metastasis</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Peritoneal cavity metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METALUNG </b></td> 
 <td style='width:600px; text-align:left;'> Lung metastasis</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Lung metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METAOTHE </b></td> 
 <td style='width:600px; text-align:left;'> Other sites of metastase</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Other sites of metastase]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METAoths </b></td> 
 <td style='width:600px; text-align:left;'> Other site, please specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Other site please specify]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Other sites of metastase] == '1' && [2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
</table>

### 3- Tumor functioning 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TUFONC </b></td> 
 <td style='width:600px; text-align:left;'> Is the tumor functioning</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPTUM </b></td> 
 <td style='width:600px; text-align:left;'> If yes, type</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[3- Tumor functioning.*][If yes type]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[3- Tumor functioning][Is the tumor functioning] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Insulinoma</b> <br>🔘 2 - <b>Gastrinoma</b> <br>🔘 3 - <b>Glucagonoma</b> <br>🔘 4 - <b>VIPoma</b> <br>🔘 5 - <b>Somatostatinoma</b> <br>🔘 6 - <b>Cushing’s syndrome</b> <br>🔘 7 - <b>Parathroid hormone-related peptid syndrome</b> <br>🔘 8 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPTUM_S </b></td> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[3- Tumor functioning.*][If other specify]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[3- Tumor functioning][Is the tumor functioning] == '1' && [3- Tumor functioning][If yes type] == '8' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Num - 50 </td> 
 </tr>
</table>

### 4 - Inherited syndroms 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SYNDYN </b></td> 
 <td style='width:600px; text-align:left;'> Inherited syndroms</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPSYND </b></td> 
 <td style='width:600px; text-align:left;'> If yes, type</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[4 - Inherited syndroms.*][If yes type inherited syndrome]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[4 - Inherited syndroms][Inherited syndroms] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Multiple Endocrine Neoplasia (NEM) type I</b> <br>🔘 2 - <b>Von Hippel-Lindau (VHL) disease</b> <br>🔘 3 - <b>Tuberous sclerosis (STB)</b> <br>🔘 4 - <b>Neurofibromatosis type 1 (NF1)</b> <br>🔘 5 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPSYND_S </b></td> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[4 - Inherited syndroms.*][If other specify inherited syndrome]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[4 - Inherited syndroms][If yes type inherited syndrome] == '5' && [4 - Inherited syndroms][Inherited syndroms] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
</table>

### 5 - Patholgy _ primary analysis 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ANAPRI </b></td> 
 <td style='width:600px; text-align:left;'> Pathology on  primary</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[Description of disease.*][5 - Patholgy _ primary analysis.*][Pathology on  primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Description of disease][5 - Patholgy _ primary analysis][Pathology on  primary]=='1' ||
([Description of disease][5 - Patholgy _ primary analysis][Pathology on  primary] == '0' &&
[Description of disease][6 - Patholgy _ Metastasis analysis][pathology on Metastasis]!= '0' &&[Description of disease][2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' ) 
#data Expression 
 
</code></pre> </td><td> at leat 1 KI analysis has to be done</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b> <br>🔘 1 - <b>Done</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DATPA </b></td> 
 <td style='width:600px; text-align:left;'> Date</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> Enabled:[5 - Patholgy _ primary analysis.*][Date of primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[5 - Patholgy _ primary analysis][Pathology on  primary] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> Valid:[Description of disease.*][5 - Patholgy _ primary analysis.*][Date of primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
DaysBetween([Description of disease][1-Initial diagnosis][Date of primary tumor diagnosis],[Description of disease][5 - Patholgy _ primary analysis][Date of primary])>=0 || isNaN( DaysBetween([Description of disease][1-Initial diagnosis][Date of primary tumor diagnosis],[Description of disease][5 - Patholgy _ primary analysis][Date of primary])); 
#data Expression 
 
</code></pre> </td><td> This date should be after (or equal) date of primary tumor diagnosis</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> NECPA </b></td> 
 <td style='width:600px; text-align:left;'> Necrosis</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[5 - Patholgy _ primary analysis.*][Necrosis on primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[5 - Patholgy _ primary analysis][Pathology on  primary] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CountPri </b></td> 
 <td style='width:600px; text-align:left;'> Highest mitotic count number (highest mitotic activity / 2mm2, x40 )</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[5 - Patholgy _ primary analysis.*][Countprim]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[5 - Patholgy _ primary analysis][Pathology on  primary] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 2 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Ki67PA </b></td> 
 <td style='width:600px; text-align:left;'> Ki67 number (/ 2000 cells, x 40)</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[5 - Patholgy _ primary analysis.*][Ki67 number on primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[5 - Patholgy _ primary analysis][Pathology on  primary] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 2 </td> 
 </tr>
</table>

### 6 - Patholgy _ Metastasis analysis 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th style='width:300px; text-align:center;'><strong>Check</strong></th>
<th style='width:300px; text-align:center;'><strongRéponses possibles</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ANAMT </b></td> 
 <td style='width:600px; text-align:left;'> pathology on Metastasis</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b> <br>🔘 1 - <b>Done</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DATEMT </b></td> 
 <td style='width:600px; text-align:left;'> Date</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> Enabled:[6 - Patholgy _ Metastasis analysis.*][date for metastas analysis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[6 - Patholgy _ Metastasis analysis][pathology on Metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> Valid:[Description of disease.*][6 - Patholgy _ Metastasis analysis.*][date for metastas analysis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
DaysBetween([Description of disease][2 - At the time of the inclusion][If yes_ date of appearance of first metastasis],[Description of disease][6 - Patholgy _ Metastasis analysis][date for metastas analysis])>=0 || isNaN(DaysBetween([Description of disease][2 - At the time of the inclusion][If yes_ date of appearance of first metastasis],[Description of disease][6 - Patholgy _ Metastasis analysis][date for metastas analysis])); 
#data Expression 
 
</code></pre> </td><td> This date should be after  date of appearance of first metastasis</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> NECMT </b></td> 
 <td style='width:600px; text-align:left;'> Necrosis</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[6 - Patholgy _ Metastasis analysis.*][Necrosis on metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[6 - Patholgy _ Metastasis analysis][pathology on Metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> countmet </b></td> 
 <td style='width:600px; text-align:left;'> Highest mitotic count number (highest mitotic activity / 2mm2, x40 )</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[6 - Patholgy _ Metastasis analysis.*][CountMeta]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[6 - Patholgy _ Metastasis analysis][pathology on Metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 2 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> KI67MT </b></td> 
 <td style='width:600px; text-align:left;'> Ki67 number (/ 2000 cells, x 40)</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[6 - Patholgy _ Metastasis analysis.*][Ki67 number for metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[6 - Patholgy _ Metastasis analysis][pathology on Metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 2 </td> 
 </tr>
</table>

