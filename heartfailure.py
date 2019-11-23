from math import exp




'''
Function:firstHeartFailure
Parameters:
    AGEDIAG:age of diagnosis
    ATFIB:1 for atrial fibrillation; 0 otherwise.
    BMI: Body mass index(m/kg^2 )
    eGFR:Estimated glomerular filtration rate (ml/min/1.73m2 ) from Modification of Diet in Renal Disease (MDRD) formula
    HAEM:Haemoglobin g/dL
    LDL:Low density lipoprotein cholesterol (mmol/l)
    PVD:1 for peripheral vascular disease; 0 otherwise.
    MMALB:Presence of micro- or macro-albuminuria. 1 for urine albumin ≥50mg/l; 0 otherwise
    AMPHIST:1 for history of amputation; 0 otherwise
    ULCERHIST:1 for history of Ulcer; 0 otherwise
    DIAHIST:year of diabetes
Return:
    chance of firstHeartFailure for this year
'''

def firstHeartFailure(AGEDIAG,ATFIB,BMI,eGFR,LDL,MMALB,PVD,AMPHIST,ULCERHIST,DIAHIST):
    Lambda=-12.332
    Roh=1.514
    AGEDIAGM=0.068
    BMIM=0.072
    if eGFR<60:
        eGFRM=-0.220
    else:
        eGFRM=0
    LDLM=0.012
    ATFIBM=1.562
    MMALBM=0.771
    PVDM=0.479
    AMPHISTM=1.108
    ULCERHISTM=0.654
    p1=exp(Lambda+AGEDIAGM*AGEDIAG+BMI*BMIM+ATFIBM*ATFIB+eGFR/10*eGFRM+LDL*10*LDLM+MMALB*MMALBM+PVD*PVDM+AMPHIST*AMPHISTM+ULCERHIST*ULCERHISTM)*DIAHIST**Roh
    p1=exp(Lambda+AGEDIAGM*AGEDIAG+BMI*BMIM+ATFIBM*ATFIB+eGFR/10*eGFRM+LDL*10*LDLM+MMALB*MMALBM+PVD*PVDM+AMPHIST*AMPHISTM+ULCERHIST*ULCERHISTM)*(DIAHIST+1)**Roh
    p=1-exp(p1-p2)
    return p
