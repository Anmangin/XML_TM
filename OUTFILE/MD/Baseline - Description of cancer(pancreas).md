<body>


<!-- Sidebar -->
<div class=sidebar id=sidebar>
<h3>Table des matières</h3>
<div id=sidebar-links></div>
</div> 
<div class=content> 
<section id='618aa01c-4547-4535-a7d5-7285ac62256c' data-parent='fcd47032-d8b3-42e8-99d8-85660e1ec957' data-type='form' data-label='F07 : Description of disease'>
<h2> F07 : Description of disease </h2>
<p>Liste des visites avec cette fiches :Baseline</p> 
<h3> 1-Initial diagnosis </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date of primary tumor diagnosis</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DIAGDT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Primary location not found</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCPRIM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Body of pancreas</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Body of pancreas]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCBODY </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Head of pancreas</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Head of pancreas]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCHEAD </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Tail of pancreas</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Tail of pancreas]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCTAIL </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Other, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Other specify]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Other__s </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Other location ,specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[1-Initial diagnosis.*][Other location specify]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[1-Initial diagnosis][Primary location not found] == '0' && [1-Initial diagnosis][Other specify] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> LOCDIAG_ </b></td> 
 </tr>
</table>

<h3> 2 - At the time of the inclusion </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> <u>TNM stage:</u></td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TNM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> T - ENETS:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>T1</b><br>🔘 2 - <b>T2</b><br>🔘 3 - <b>T3</b><br>🔘 4 - <b>T4</b><br>🔘 0 - <b>Tx</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STGIT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> N:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>N0</b><br>🔘 1 - <b>N1</b><br>🔘 2 - <b>N2</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STGIN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> M:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>M0</b><br>🔘 1 - <b>M1</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> STGIM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Histologic grading at inclusion</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Grade 1</b><br>🔘 2 - <b>Grade 2</b><br>🔘 3 - <b>Grade 3</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> HGRAD </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> <font color="#ffffff">.</font></td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> L1 </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Presence of metastasis at inclusion:</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METAINC </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If yes, date of appearance of first metastasis:</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> Enabled:[Description of disease.*][2 - At the time of the inclusion.*][If yes_ date of appearance of first metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Description of disease][2 - At the time of the inclusion][Presence of metastasis at inclusion]=='1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> Valid:[Description of disease.*][2 - At the time of the inclusion.*][If yes_ date of appearance of first metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
DaysBetween([Description of disease][1-Initial diagnosis][Date of primary tumor diagnosis],[Description of disease][2 - At the time of the inclusion][If yes_ date of appearance of first metastasis])>=0 || isNaN(DaysBetween([Description of disease][1-Initial diagnosis][Date of primary tumor diagnosis],[Description of disease][2 - At the time of the inclusion][If yes_ date of appearance of first metastasis])) 
#data Expression 
 
</code></pre> </td><td> This date should be after (or equal) date of primary tumor diagnosis</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METADT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Brain metastasis</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Brain metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METABRAI </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> bone metastasis</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][bone metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METABONE </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Liver metastasis</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Liver metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METALIVE </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If liver, involment > 50 %</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][If liver involment SUP 50 ]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Liver metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>No</b><br>🔘 1 - <b>Yes</b><br>🔘 2 - <b>Unknown</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MLIVINV </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Peritoneal cavity metastasis</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Peritoneal cavity metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METAPERI </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Lung metastasis</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Lung metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METALUNG </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Other sites of metastase</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Other sites of metastase]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METAOTHE </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Other site, please specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[2 - At the time of the inclusion.*][Other site please specify]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[2 - At the time of the inclusion][Other sites of metastase] == '1' && [2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> METAoths </b></td> 
 </tr>
</table>

<h3> 3- Tumor functioning </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Is the tumor functioning</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TUFONC </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If yes, type</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[3- Tumor functioning.*][If yes type]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[3- Tumor functioning][Is the tumor functioning] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Insulinoma</b><br>🔘 2 - <b>Gastrinoma</b><br>🔘 3 - <b>Glucagonoma</b><br>🔘 4 - <b>VIPoma</b><br>🔘 5 - <b>Somatostatinoma</b><br>🔘 6 - <b>Cushing’s syndrome</b><br>🔘 7 - <b>Parathroid hormone-related peptid syndrome</b><br>🔘 8 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPTUM </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[3- Tumor functioning.*][If other specify]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[3- Tumor functioning][Is the tumor functioning] == '1' && [3- Tumor functioning][If yes type] == '8' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPTUM_S </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> MISSING_VAR</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> MISSING_ </b></td> 
 </tr>
</table>

<h3> 4 - Inherited syndroms </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Inherited syndroms</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> SYNDYN </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If yes, type</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[4 - Inherited syndroms.*][If yes type inherited syndrome]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[4 - Inherited syndroms][Inherited syndroms] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Multiple Endocrine Neoplasia (NEM) type I</b><br>🔘 2 - <b>Von Hippel-Lindau (VHL) disease</b><br>🔘 3 - <b>Tuberous sclerosis (STB)</b><br>🔘 4 - <b>Neurofibromatosis type 1 (NF1)</b><br>🔘 5 - <b>Other</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPSYND </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> If other, specify</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[4 - Inherited syndroms.*][If other specify inherited syndrome]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[4 - Inherited syndroms][If yes type inherited syndrome] == '5' && [4 - Inherited syndroms][Inherited syndroms] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> TPSYND_S </b></td> 
 </tr>
</table>

<h3> 5 - Patholgy _ primary analysis </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Pathology on  primary</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Valid:[Description of disease.*][5 - Patholgy _ primary analysis.*][Pathology on  primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Description of disease][5 - Patholgy _ primary analysis][Pathology on  primary]=='1' ||
([Description of disease][5 - Patholgy _ primary analysis][Pathology on  primary] == '0' &&
[Description of disease][6 - Patholgy _ Metastasis analysis][pathology on Metastasis]!= '0' &&[Description of disease][2 - At the time of the inclusion][Presence of metastasis at inclusion] == '1' ) 
#data Expression 
 
</code></pre> </td><td> at leat 1 KI analysis has to be done</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b><br>🔘 1 - <b>Done</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ANAPRI </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> Enabled:[5 - Patholgy _ primary analysis.*][Date of primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[5 - Patholgy _ primary analysis][Pathology on  primary] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> Valid:[Description of disease.*][5 - Patholgy _ primary analysis.*][Date of primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
DaysBetween([Description of disease][1-Initial diagnosis][Date of primary tumor diagnosis],[Description of disease][5 - Patholgy _ primary analysis][Date of primary])>=0 || isNaN( DaysBetween([Description of disease][1-Initial diagnosis][Date of primary tumor diagnosis],[Description of disease][5 - Patholgy _ primary analysis][Date of primary])); 
#data Expression 
 
</code></pre> </td><td> This date should be after (or equal) date of primary tumor diagnosis</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DATPA </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Necrosis</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[5 - Patholgy _ primary analysis.*][Necrosis on primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[5 - Patholgy _ primary analysis][Pathology on  primary] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> NECPA </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Highest mitotic count number (highest mitotic activity / 2mm2, x40 )</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[5 - Patholgy _ primary analysis.*][Countprim]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[5 - Patholgy _ primary analysis][Pathology on  primary] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> CountPri </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Ki67 number (/ 2000 cells, x 40)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[5 - Patholgy _ primary analysis.*][Ki67 number on primary]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[5 - Patholgy _ primary analysis][Pathology on  primary] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Ki67PA </b></td> 
 </tr>
</table>

<h3> 6 - Patholgy _ Metastasis analysis </h3>
<table style='width:100%;'>
<tr>
<th style='width:600px; text-align:center;'><strong>Label de la question </strong></th>
<th class='check' style='width:300px; text-align:center;'><strong>Check</strong></th> <!--$htmlbalise-->
<th style='width:300px; text-align:center;'><strong>Réponses possibles</strong></th>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
</tr>
 <tr> 
 <td style='width:600px; text-align:left;'> pathology on Metastasis</td>
 <td class='check' style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 0 - <b>Not done</b><br>🔘 1 - <b>Done</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> ANAMT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Date</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> Enabled:[6 - Patholgy _ Metastasis analysis.*][date for metastas analysis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[6 - Patholgy _ Metastasis analysis][pathology on Metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> Valid:[Description of disease.*][6 - Patholgy _ Metastasis analysis.*][date for metastas analysis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
DaysBetween([Description of disease][2 - At the time of the inclusion][If yes_ date of appearance of first metastasis],[Description of disease][6 - Patholgy _ Metastasis analysis][date for metastas analysis])>=0 || isNaN(DaysBetween([Description of disease][2 - At the time of the inclusion][If yes_ date of appearance of first metastasis],[Description of disease][6 - Patholgy _ Metastasis analysis][date for metastas analysis])); 
#data Expression 
 
</code></pre> </td><td> This date should be after  date of appearance of first metastasis</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> DATEMT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Necrosis</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[6 - Patholgy _ Metastasis analysis.*][Necrosis on metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[6 - Patholgy _ Metastasis analysis][pathology on Metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b><br>🔘 0 - <b>No</b> </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> NECMT </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Highest mitotic count number (highest mitotic activity / 2mm2, x40 )</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[6 - Patholgy _ Metastasis analysis.*][CountMeta]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[6 - Patholgy _ Metastasis analysis][pathology on Metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> countmet </b></td> 
 </tr>
 <tr> 
 <td style='width:600px; text-align:left;'> Ki67 number (/ 2000 cells, x 40)</td>
 <td class='check' style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Enabled:[6 - Patholgy _ Metastasis analysis.*][Ki67 number for metastasis]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[6 - Patholgy _ Metastasis analysis][pathology on Metastasis] == '1' 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'>  </td> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> KI67MT </b></td> 
 </tr>
</table>

</section></section> 
  </div><script>function generateSidebar() {

    // Récupère tous les éléments H1 et H2
    var headersH1 = document.querySelectorAll('h1');
    var headersH2 = document.querySelectorAll('h2');
    var sidebarLinks = document.getElementById('sidebar-links');
    var sections = document.querySelectorAll('.content section');
    
    // Créer des liens pour chaque H1 dans la sidebar
    sections.forEach(section => {
        
        let type=section.getAttribute('data-type')
        var link = document.createElement('a');
        link.href = '#' + section.id;  // Associe le lien à l'ID du H1
        link.textContent = section.getAttribute('data-label');
        link.setAttribute('data-target', section.id);
        link.classList.add(type);  // Lien H1
        // Si le type est "form", ajoute un tiret ou une indentation
        if (type === "form") {
            // Ajouter un tiret avant le texte du lien
            link.textContent = "" + link.textContent;  // Tiret simple

            // Ou ajouter une indentation (par exemple, un espacement supplémentaire)
            link.style.marginLeft = "20px";  // Déplacement à droite, ajustable
        } else {
            // Sinon, applique une police plus grosse et un fond bleuté
            link.style.fontSize = "18px";  // Augmente la taille de la police
            link.style.backgroundColor = "#e0f7fa";  // Fond bleu clair (légèrement bleuté)
            link.style.padding = "5px";  // Un peu de padding pour l'espace autour du texte
            link.style.borderRadius = "4px";  // Coins arrondis pour l'esthétique
        }

        sidebarLinks.appendChild(link);
    })
        
  

    // Gestion des événements de clic sur les liens de la sidebar
    const links = document.querySelectorAll('.sidebar a');

    links.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            
            const targetId = link.getAttribute('data-target');  // L'ID de la section ciblée
            let selected_section = document.getElementById(targetId);
            let parenttargetId = selected_section.getAttribute('data-parent');
            let select_section = selected_section.getAttribute('data-type');
            let select_label= selected_section.getAttribute('data-label');

            let sections = document.querySelectorAll('.content section');
            console.log(parenttargetId, select_section)
            console.log("selection de la visite ",select_label, " targetId:", targetId, " " , "parenttargetId :",parenttargetId )

            //console.log(targetId,parenttargetId)
           i=0
            sections.forEach(section => {
                // console.log(section)
                i+=1
                let sectionid= section.id;
                let parentid= section.getAttribute('data-parent');
                let type= section.getAttribute('data-type');
                let label= section.getAttribute('data-label');
                                
                section.classList.remove('show', 'hidden');
                let affichage="hidden";

                if ( select_section=="form" && type=="visit"    && sectionid==parenttargetId    )affichage="show"
                else if (select_section==type && (sectionid==targetId))affichage="show"
                else if (select_section=="visit" && type=="form" && parenttargetId==parentid )affichage="show"

                // if (select_section=="form" && (sectionid == targetId || sectionid==parenttargetId  )) affichage="show"
                // else if  (select_section=="visit" && (sectionid == targetId || sectionid==parenttargetId || parentid==targetId || parentid==parenttargetId  )) affichage="show"
                
                section.classList.add(affichage)
                console.log("------------->test du ",label, ":",affichage  , "parenttargetId:",parenttargetId , "sectionid:",sectionid)

            });

        });
    })
}



window.onload = generateSidebar;
</script> </body>


