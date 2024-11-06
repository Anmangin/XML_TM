# Adverse Event [AE]

## Verbatim
- **[AE1]**
- **[AETERM]**

## Coding [AE2]
- **CTCAE SOC** [AESOC]
  - *List of SOC from CTCAE V4.0*
- **CTCAE Term** [AEPT]
  - *List of Terms (PT) from CTCAE V4.0*

## Dates of event [AE3]
- **Ongoing at the beginning of treatment** [AESGO]
- **Start date** [AESDT]  
  Format: DD/MM/YYYY
- **Cycle at which the event started** [AECYCLE]
- **Ongoing at the end of treatment and/or at the end of short-time follow up** [AEEGO]
- **End date** [AEEDT]  
  Format: DD/MM/YYYY

## Details on the case [AE4]
- **Grade** [AEGR]
- **DLT** [AEDLT]  
  Options: 0 - No, 1 - Yes
- **SAE** [AESER]  
  Options: 0 - No, 1 - Yes
- **SAE** [AE5]
- **Date of SAE reporting to PV** [AESERDT]  
  Format: DD/MM/YYYY
- **CIOMS Number** [AECIOMS]

## Additional information [AE6]
- **Related to** [AEREL]  
  Options: 1 - Drug 1, 2 - Drug 2, 3 - Drug 3, 4 - Cancer, 99 - Other  
  If other, specify [AEREL_S]
- **Action** [AEACN]  
  Options: 0 - No action, 1 - Action 1, 2 - Action 2, 99 - Other  
  If other, specify [AEACN_S]
- **Treatment required** [AETRTYN]  
  Options: 0 - No, 1 - Yes
