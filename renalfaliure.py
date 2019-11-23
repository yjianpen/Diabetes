from math import exp




'''
Function:renalFailure
Parameters:
    AFRO:1 Afro-Caribbean ethnicity; 0 otherwise
    AGEDIAG:age of diagnosis
    FEMALE:1 for female; 0 for male
    BMI: Body mass index(m/kg^2 )
    eGFR:Estimated glomerular filtration rate (ml/min/1.73m2 ) from Modification of Diet in Renal Disease (MDRD) formula
    HAEM:Haemoglobin g/dL
    LDL:Low density lipoprotein cholesterol (mmol/l)
    MMALB:Presence of micro- or macro-albuminuria. 1 for urine albumin ≥50mg/l; 0 otherwise
    SBP:Systolic blood pressure (mm Hg)
    WBC:White blood cell count
    AMPHIST:1 for history of amputation; 0 otherwise
    BLINDHIST:1 for history of blindness; 0 otherwise
    DIAHIST:year of diabetes history
Return:
    chance of renalFailure for this year
'''

def RenalFailure(AFRO,AGEDIAG,FEMALE,BMI,eGFR,HAEM,LDL,MMALB,SBP,WBC,AMPHIST,BLINDHIST,DIAHIST):
    Lambda=3.549
    AFROM=0.686
    AGEDIAGM=-0.029
    FEMALEM=-0.869
    BMIM=-0.054
    if eGFR<60:
        eGFRM=-1.031
    else:
        eGFRM=-0.487
    HAEMM=-0.268
    LDLM=0.027
    MMALBM=1.3673
    SBPM=0.085
    WBCM=0.029
    AMPHISTM=1.108
    BLINDHISTM=0.732
    p1=exp(Lambda+AFRO*AFROM+AGEDIAGM*AGEDIAG+FEMALEM*FEMALE+BMI*BMIM+eGFR/10*eGFRM+HAEM*HAEMM+LDL*10*LDLM+MMALB*MMALBM+SBP/10*SBPM+WBC*WBCM+AMPHIST*AMPHISTM+BLINDHIST*BLINDHISTM)*DIAHIST
    p2=exp(Lambda+AFRO*AFROM+AGEDIAGM*AGEDIAG+FEMALEM*FEMALE+BMI*BMIM+eGFR/10*eGFRM+HAEM*HAEMM+LDL*10*LDLM+MMALB*MMALBM+SBP/10*SBPM+WBC*WBCM+AMPHIST*AMPHISTM+BLINDHIST*BLINDHISTM)*(DIAHIST+1)
    p=1-exp(p1-p2)
    return p
