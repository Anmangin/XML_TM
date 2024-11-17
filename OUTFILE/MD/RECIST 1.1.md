# Version de TB pour ce fichier : 5.0.3.27.Update 3b  
# RECIST 
## RECIST Evaluation 
### RC1 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> Label_re </b></td> 
 <td style='width:600px; text-align:left;'> Tumor assessment period</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> Char - 1 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCDT </b></td> 
 <td style='width:600px; text-align:left;'> Date of local evaluation</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 📅 DD/MM/YYYY  </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 👻FLAG </b></td> 
 <td style='width:600px; text-align:left;'> FLAG</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> Read Only:[Recist.*][RC1.*][FLAG]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
'1'; 
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

### RC2 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒RCTLORD </b></td> 
 <td style='width:600px; text-align:left;'> Order n°</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> DVA:[Recist.*][RC2.*][RCTLORD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
!isEmpty([Recist.1][RC2.@][RCTLSITE]); 
#data Expression 
GroupInstanceNo; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 100 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCTLSITE </b></td> 
 <td style='width:600px; text-align:left;'> Site</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 7:[Recist.*][RC2.*][RCTLSITE]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
FormInstanceNo>1; 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> DVA:[Recist.*][RC2.*][RCTLSITE]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
FormInstanceNo>1 && !isEmpty([Recist.1][RC2][RCTLSITE]); 
#data Expression 
[Recist.1][RC2.@][RCTLSITE]; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Colon</b> <br>🔘 2 - <b>Lung</b> <br>🔘 3 - <b>Liver</b> <br>🔘 4 - <b>Bone</b> <br>🔘 5 - <b>Brain</b> <br>🔘 6 - <b>Nodes</b> <br>🔘 7 - <b>Rectum</b> <br>🔘 8 - <b>Kidneys/Adrenals</b> <br>🔘 99 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCTL_S </b></td> 
 <td style='width:600px; text-align:left;'> Location</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> DVA:[Recist.*][RC2.*][RCTL_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
FormInstanceNo>1 && !isEmpty([Recist.1][RC2.@][RCTL_S]); 
#data Expression 
[Recist.1][RC2.@][RCTL_S]; 
</code></pre> </td><td> </td> </tr><tr><td> 7:[Recist.*][RC2.*][RCTL_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
FormInstanceNo>1; 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCTLDIAM </b></td> 
 <td style='width:600px; text-align:left;'> Longest diameter (mm)</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 2:[Recist.*][RC2.*][RCTLDIAM]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
!isEmpty([Recist.1][RC2.@][RCTLSITE]) && [Recist][RC3][RCTLRESP] != '5'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Enabled:[Recist.*][RC2.*][RCTLDIAM]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
!isEmpty([Recist.1][RC2.@][RCTLSITE]); 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 3 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCTLMOD </b></td> 
 <td style='width:600px; text-align:left;'> Method</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 2:[Recist.*][RC2.*][RCTLMOD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Recist][RC3][RCTLRESP] != '5' && !isEmpty([Recist.1][RC2.@][RCTLSITE]); 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Enabled:[Recist.*][RC2.*][RCTLMOD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
!isEmpty([Recist.1][RC2.@][RCTLSITE]); 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>CT SCAN</b> <br>🔘 2 - <b>MRI</b> <br> </td> 
 </tr>
</table>

### RC3 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒RCTLSUM </b></td> 
 <td style='width:600px; text-align:left;'> <font color="#808080">Sum of longest diameters (mm)</font></td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> DVA:[Recist.*][RC3.*][RCTLSUM]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
var res = 0;
var resp = 0;

res = Number([Recist.@][RC2.1][RCTLDIAM]) + Number([Recist.@][RC2.2][RCTLDIAM])+ Number([Recist.@][RC2.3][RCTLDIAM]) + Number([Recist.@][RC2.4][RCTLDIAM]) + Number([Recist.@][RC2.5][RCTLDIAM]);

resp = [Recist][RC3][RCTLRESP];

if (resp == 5)
    '';
else if (res == 0)
    '0';
else
    res; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 4 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒RCTLMIN </b></td> 
 <td style='width:600px; text-align:left;'> <font color="#808080">Minimum sum of diameters</font></td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 2:[Recist.*][RC3.*][RCTLMIN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Recist][RC3][RCTLRESP] != '5'; 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> DVA:[Recist.*][RC3.*][RCTLMIN]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
true; 
#data Expression 
var res = 0;
var l1 =  [Recist.@][RC2.1][RCTLDIAM];
var l2 =  [Recist.@][RC2.2][RCTLDIAM];
var l3 =  [Recist.@][RC2.3][RCTLDIAM];
var l4 =  [Recist.@][RC2.4][RCTLDIAM];
var l5 =  [Recist.@][RC2.5][RCTLDIAM];

var l1p =  [Recist.1][RC2.1][RCTLDIAM];
var l2p =  [Recist.1][RC2.2][RCTLDIAM];
var l3p =  [Recist.1][RC2.3][RCTLDIAM];
var l4p =  [Recist.1][RC2.4][RCTLDIAM];
var l5p =  [Recist.1][RC2.5][RCTLDIAM];

res = Number([Recist.@][RC2.1][RCTLDIAM]) + Number([Recist.@][RC2.2][RCTLDIAM])+ Number([Recist.@][RC2.3][RCTLDIAM]) + Number([Recist.@][RC2.4][RCTLDIAM]) + Number([Recist.@][RC2.5][RCTLDIAM]);

if ([Recist.<][RC3][RCTLMIN]<res  
|| ( isEmpty(l1) && !isEmpty(l1p))
|| ( isEmpty(l2) && !isEmpty(l2p))
|| ( isEmpty(l3) && !isEmpty(l3p))
|| ( isEmpty(l4) && !isEmpty(l4p))
|| ( isEmpty(l5) && !isEmpty(l5p))
 )[Recist.<][RC3][RCTLMIN];

else res; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Num - 5 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCTLRESP </b></td> 
 <td style='width:600px; text-align:left;'> Response of target lesions</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>7 EditCheck </summary><table><tr><td> Valid:[Recist.*][RC3.*][RCTLRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=true;
if ([Recist][RC3][RCTLRESP]==1) {
if(
( [Recist][RC2.1][RCTLSITE]=='6' && [Recist][RC2.1][RCTLDIAM]>9 ) 
||
([Recist][RC2.1][RCTLSITE]!='6' && !isEmpty([Recist][RC2.1][RCTLSITE]) && 
[Recist][RC2.1][RCTLDIAM]>0 )  )res=false;

else if(
( [Recist][RC2.2][RCTLSITE]=='6' && [Recist][RC2.2][RCTLDIAM]>9 ) 
||
([Recist][RC2.2][RCTLSITE]!='6' && !isEmpty([Recist][RC2.2][RCTLSITE]) && 
[Recist][RC2.2][RCTLDIAM]>0 )  )res=false;

else if(
( [Recist][RC2.3][RCTLSITE]=='6' && [Recist][RC2.3][RCTLDIAM]>9 ) 
||
([Recist][RC2.3][RCTLSITE]!='6' && !isEmpty([Recist][RC2.3][RCTLSITE]) && 
[Recist][RC2.3][RCTLDIAM]>0 )  )res=false;

else if(
( [Recist][RC2.4][RCTLSITE]=='6' && [Recist][RC2.4][RCTLDIAM]>9 ) 
||
([Recist][RC2.4][RCTLSITE]!='6' && !isEmpty([Recist][RC2.4][RCTLSITE]) && 
[Recist][RC2.4][RCTLDIAM]>0 )  )res=false;


else if(
( [Recist][RC2.5][RCTLSITE]=='6' && [Recist][RC2.5][RCTLDIAM]>9 ) 
||
([Recist][RC2.5][RCTLSITE]!='6' && !isEmpty([Recist][RC2.5][RCTLSITE]) && 
[Recist][RC2.5][RCTLDIAM]>0 )  )res=false;
}



res; 
#data Expression 
 
</code></pre> </td><td> Sum of longest diameters has to be 0 for a complete response, actualy the sum is [Recist][RC3][RCTLSUM] . Please correct.</td> </tr><tr><td> Valid:[Recist.*][RC3.*][RCTLRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var sbaseline = Number([Recist.1][RC3][RCTLSUM]);
var sactuel = Number([Recist.@][RC3][RCTLSUM]);

if ( ( (1 -(sactuel / sbaseline) >= 0.3)  && [Recist][RC3][RCTLRESP]=='2') ||
([Recist][RC3][RCTLRESP]!='2') ) true;
else false; 
#data Expression 
 
</code></pre> </td><td> Sum on longest lesion has to decrease at least 30 % from baseline assessment to be evaluate as partial response, please verify.</td> </tr><tr><td> Valid:[Recist.*][RC3.*][RCTLRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
((Number([Recist.@][RC3][RCTLSUM]) / Number([Recist.@][RC3][RCTLMIN]) -1 )>=0.2   


&& [Recist.@][RC3][RCTLRESP]=='4' ) || [Recist.@][RC3][RCTLRESP] !='4' || [Recist.@][RC6][RCNEW] != '0'; 
#data Expression 
 
</code></pre> </td><td> An increase from Nadir to the sum is expected from 20 % (or appearance of new lesions), please verify.</td> </tr><tr><td> 21:[Recist.*][RC3.*][RCTLRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
FormInstanceNo == '1'; 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> Valid:[Recist.*][RC3.*][RCTLRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Recist][RC3][RCTLRESP]==5 || 
(
( isEmpty([Recist][RC2.1][RCTLSITE]) ||
 ( !isEmpty([Recist][RC2.1][RCTLSITE]) && !isEmpty([Recist][RC2.1][RCTLDIAM]) ))
&&
( isEmpty([Recist][RC2.2][RCTLSITE]) ||
 ( !isEmpty([Recist][RC2.2][RCTLSITE]) && !isEmpty([Recist][RC2.2][RCTLDIAM]) ))
&&
( isEmpty([Recist][RC2.3][RCTLSITE]) ||
 ( !isEmpty([Recist][RC2.3][RCTLSITE]) && !isEmpty([Recist][RC2.3][RCTLDIAM]) ))
&&
( isEmpty([Recist][RC2.4][RCTLSITE]) ||
 ( !isEmpty([Recist][RC2.4][RCTLSITE]) && !isEmpty([Recist][RC2.4][RCTLDIAM]) ))
&&
( isEmpty([Recist][RC2.5][RCTLSITE]) ||
 ( !isEmpty([Recist][RC2.5][RCTLSITE]) && !isEmpty([Recist][RC2.5][RCTLDIAM]) ))
) 
#data Expression 
 
</code></pre> </td><td> A diameter is missing, please fill out or select "Not evaluable".</td> </tr><tr><td> Valid:[Recist.*][RC3.*][RCTLRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=false;
if ([Recist][RC3][RCTLRESP]!='5' ) res=true;  

if (!isEmpty([Recist][RC2.1][RCTLSITE]) && isEmpty([Recist][RC2.1][RCTLDIAM])) res=true;
if (!isEmpty([Recist][RC2.2][RCTLSITE]) && isEmpty([Recist][RC2.2][RCTLDIAM])) res=true;
if (!isEmpty([Recist][RC2.3][RCTLSITE]) && isEmpty([Recist][RC2.3][RCTLDIAM]))res=true;
if (!isEmpty([Recist][RC2.4][RCTLSITE]) && isEmpty([Recist][RC2.4][RCTLDIAM])) res=true;
if (!isEmpty([Recist][RC2.5][RCTLSITE]) && isEmpty([Recist][RC2.5][RCTLDIAM])) res=true;


res; 
#data Expression 
 
</code></pre> </td><td> All the target are evaluated, the patient is evaluable, please correct.</td> </tr><tr><td> Valid:[Recist.*][RC3.*][RCTLRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=false;
if ([Recist][RC3][RCTLRESP] =='1' ) res=true;  

else if ([Recist][RC3][RCTLSUM] != '0') res=true;
else res=false; 
#data Expression 
 
</code></pre> </td><td> If the sum of longest diameters is 0, the response should be "Complete response". Please correct.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Complete response</b> <br>🔘 2 - <b>Partial response</b> <br>🔘 3 - <b>Stable disease</b> <br>🔘 4 - <b>Progressive disease</b> <br>🔘 5 - <b>Not evaluable</b> <br> </td> 
 </tr>
</table>

### RC4 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> 🔒RCNTLORD </b></td> 
 <td style='width:600px; text-align:left;'> Order n°</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>1 EditCheck </summary><table><tr><td> DVA:[Recist.*][RC4.*][RCNTLORD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
!isEmpty([Recist.1][RC4][RCNTLSIT]); 
#data Expression 
GroupInstanceNo; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 100 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCNTLSIT </b></td> 
 <td style='width:600px; text-align:left;'> Site</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 7:[Recist.*][RC4.*][RCNTLSIT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
FormInstanceNo>1; 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> DVA:[Recist.*][RC4.*][RCNTLSIT]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
FormInstanceNo>1 && !isEmpty([Recist.1][RC4.@][RCNTLSIT]); 
#data Expression 
[Recist.1][RC4.@][RCNTLSIT]; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Colon</b> <br>🔘 2 - <b>Lung</b> <br>🔘 3 - <b>Liver</b> <br>🔘 4 - <b>Bone</b> <br>🔘 5 - <b>Brain</b> <br>🔘 6 - <b>Nodes</b> <br>🔘 7 - <b>Rectum</b> <br>🔘 8 - <b>Kidneys/Adrenals</b> <br>🔘 99 - <b>Other</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCNTL_S </b></td> 
 <td style='width:600px; text-align:left;'> Location</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 7:[Recist.*][RC4.*][RCNTL_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
FormInstanceNo>1; 
#data Expression 
 
</code></pre> </td><td> </td> </tr><tr><td> DVA:[Recist.*][RC4.*][RCNTL_S]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
!isEmpty([Recist.1][RC4.@][RCNTL_S]) && FormInstanceNo>1; 
#data Expression 
[Recist.1][RC4.@][RCNTL_S]; 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> Char - 50 </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCNTLRAD </b></td> 
 <td style='width:600px; text-align:left;'> Irradiated</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 2:[Recist.*][RC4.*][RCNTLRAD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Recist][RC5][RCNTLRES] != '4' && !isEmpty([Recist.1][RC4.@][RCNTLSIT]); 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Enabled:[Recist.*][RC4.*][RCNTLRAD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
!isEmpty([Recist.1][RC4.@][RCNTLSIT]); 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCNTLPRE </b></td> 
 <td style='width:600px; text-align:left;'> Lesion present</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 2:[Recist.*][RC4.*][RCNTLPRE]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Recist][RC5][RCNTLRES] != '4' && !isEmpty([Recist.1][RC4.@][RCNTLSIT]); 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Enabled:[Recist.*][RC4.*][RCNTLPRE]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
!isEmpty([Recist.1][RC4.@][RCNTLSIT]); 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCNTLMOD </b></td> 
 <td style='width:600px; text-align:left;'> Method</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> 2:[Recist.*][RC4.*][RCNTLMOD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
[Recist][RC5][RCNTLRES] != '4' && !isEmpty([Recist.1][RC4.@][RCNTLSIT]); 
#data Expression 
 
</code></pre> </td><td> This item is required.</td> </tr><tr><td> Enabled:[Recist.*][RC4.*][RCNTLMOD]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
!isEmpty([Recist.1][RC4.@][RCNTLSIT]); 
#data Expression 
 
</code></pre> </td><td> </td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>CT SCAN</b> <br>🔘 2 - <b>MRI</b> <br> </td> 
 </tr>
</table>

### RC5 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCNTLRES </b></td> 
 <td style='width:600px; text-align:left;'> Response of non-target lesions</td>
 <td style='width:600px; text-align:left;'>  <details> <summary>2 EditCheck </summary><table><tr><td> Valid:[Recist.*][RC5.*][RCNTLRES]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var arr=[Recist.@][RC4][RCNTLPRE].ALL;
(arrayAllNos(arr) && [Recist.@][RC5][RCNTLRES]=='1' )||[Recist.@][RC5][RCNTLRES] != '1' 
#data Expression 
 
</code></pre> </td><td> All non target lesion has to be absent for a complete response, please correct.</td> </tr><tr><td> Valid:[Recist.*][RC5.*][RCNTLRES]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var arr=[Recist.@][RC4][RCNTLPRE].ALL;
(arrayAllNos(arr) && [Recist.@][RC5][RCNTLRES] == '1') || !arrayAllNos(arr) || arrayAnyEmpty(arr); 
#data Expression 
 
</code></pre> </td><td> Since all non lesion target is absent, response expected is "Complete response", please correct.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Complete response</b> <br>🔘 2 - <b>Non-CR / Non-PD</b> <br>🔘 3 - <b>Progressive disease</b> <br>🔘 4 - <b>Not evaluable</b> <br> </td> 
 </tr>
</table>

### RC6 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCNEW </b></td> 
 <td style='width:600px; text-align:left;'> Appearance of new lesions</td>
 <td style='width:600px; text-align:left;'>   </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Yes</b> <br>🔘 0 - <b>No</b> <br> </td> 
 </tr>
</table>

### RC7 

<table style='width:100%;'>
<tr>
<th style='width:50px; text-align:center;'><strong>Sas</strong></th>
<th style='width:600px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label&nbsp;de&nbsp;la&nbsp;question&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
<th style='width:300px; text-align:center;'><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Réponses&nbsp;possibles&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></th>
</tr>
<tr>
 <tr> 
<td style='width:50px; text-align:center; color:red; font-size: 10px;'> <b> RCRESP </b></td> 
 <td style='width:600px; text-align:left;'> <b><font color="#ff0033">Global response</font></b></td>
 <td style='width:600px; text-align:left;'>  <details> <summary>7 EditCheck </summary><table><tr><td> Valid:[Recist.*][RC7.*][RCRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=true;

if ([Recist][RC3][RCTLRESP] !='5' 
     && [Recist][RC6][RCNEW] != '1' 
     && [Recist][RC7][RCRESP] == '5') res=false;  

res; 
#data Expression 
 
</code></pre> </td><td> The global response should be evaluable, please verify the results entered.</td> </tr><tr><td> Valid:[Recist.*][RC7.*][RCRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=true;

if ([Recist][RC3][RCTLRESP] =='5' 
      && [Recist][RC5][RCNTLRES] != '3' 
      && [Recist][RC6][RCNEW] != '1' 
      && [Recist][RC7][RCRESP] != '5') res=false;  

res; 
#data Expression 
 
</code></pre> </td><td> The global response should not be evaluable, please verify the results entered.</td> </tr><tr><td> Valid:[Recist.*][RC7.*][RCRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=true;

if ( [Recist][RC6][RCNEW] == '1' 
     && [Recist][RC7][RCRESP] != '4') res=false;  

res; 
#data Expression 
 
</code></pre> </td><td> New lesions has appear on the patient. The global response should be "Progressive disease".
please verify the results entered.</td> </tr><tr><td> Valid:[Recist.*][RC7.*][RCRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=true;

if ( ([Recist][RC3][RCTLRESP] == '4' || [Recist][RC5][RCNTLRES] == '3') 
       && ([Recist][RC7][RCRESP] != '4') ) res=false;  

res; 
#data Expression 
 
</code></pre> </td><td> The global response should be "Progressive disease", please verify the results entered.</td> </tr><tr><td> Valid:[Recist.*][RC7.*][RCRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=true;

if ([Recist][RC3][RCTLRESP] == '1' 
     && [Recist][RC5][RCNTLRES] == '1' 
     && [Recist][RC6][RCNEW] != '1' 
     && [Recist][RC7][RCRESP] != '1') res=false;  

res; 
#data Expression 
 
</code></pre> </td><td> The global response should be "Complete response", please verify the results entered.</td> </tr><tr><td> Valid:[Recist.*][RC7.*][RCRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=true;

if ([Recist][RC3][RCTLRESP] == '3'
     && [Recist][RC5][RCNTLRES] != '2'
     && [Recist][RC6][RCNEW] != '1' 
     && [Recist][RC7][RCRESP] != '3') res=false;  


if ([Recist][RC3][RCTLRESP] == '3'
     && [Recist][RC5][RCNTLRES] != '4'
     && [Recist][RC6][RCNEW] != '1' 
     && [Recist][RC7][RCRESP] != '3') res=false;  


res; 
#data Expression 
 
</code></pre> </td><td> The global response should be "Stable disease", please verify the results entered.</td> </tr><tr><td> Valid:[Recist.*][RC7.*][RCRESP]</td> </tr><tr> <td> <pre><code class='javascript'>#Action Expression 
var res=true;

if ([Recist][RC3][RCTLRESP] == '1'
     && [Recist][RC5][RCNTLRES] == '2'
     && [Recist][RC6][RCNEW] != '1' 
     && [Recist][RC7][RCRESP] != '2') res=false;  

if ([Recist][RC3][RCTLRESP] == '1'
     && [Recist][RC5][RCNTLRES] == '4'
     && [Recist][RC6][RCNEW] != '1' 
     && [Recist][RC7][RCRESP] != '2') res=false;  

if ([Recist][RC3][RCTLRESP] == '2'
     && [Recist][RC5][RCNTLRES] != '3'
     && [Recist][RC6][RCNEW] != '1' 
     && [Recist][RC7][RCRESP] != '2') res=false;  

res; 
#data Expression 
 
</code></pre> </td><td> The global response should be "Partial response", please verify the results entered.</td> </tr></table></details> </td>
 <td style='width:300px; text-align:center;'> 🔘 1 - <b>Complete response</b> <br>🔘 2 - <b>Partial response</b> <br>🔘 3 - <b>Stable disease</b> <br>🔘 4 - <b>Progressive disease</b> <br>🔘 5 - <b>Not evaluable</b> <br> </td> 
 </tr>
</table>

