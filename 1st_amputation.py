import numpy as np
from numpy.random import normal
def first_amputation_vector(age,hbA1c,female,ATFIB,HDL,heart_rate,SBP,WBC,MIC_ALB,PVD,Stroke_Hist):
	vector=0
	if female:
		vector-=0.965
	if ATFIB:
		vector+=1.088
	vector=-14.844+0.023*age+0.248*hbA1c+(-0.059)*HDL*10/38.6+heart_rate/10*0.098+SBP/10*0.086+WBC*0.040
	if MIC_ALB:
		vector+=0.602
	if PVD:
		vector+=1.010
	if Stroke_Hist:
		vector+=1.299
	print("vector",vector)
	return np.exp(vector)*diabetes_years**(2.067)
def first_amputation(age1,age2,hbA1c,female,ATFIB,HDL,heart_rate,SBP,WBC,MIC_ALB,PVD,Stroke_Hist,diabetes_years):
	v1=first_amputation_vector(age1,hbA1c,female,ATFIB,HDL,heart_rate,SBP,WBC,MIC_ALB,PVD,Stroke_Hist)
	v2=first_amputation_vector(age2,hbA1c,female,ATFIB,HDL,heart_rate,SBP,WBC,MIC_ALB,PVD,Stroke_Hist)
	print("v1","v2",v1,v2)
	return 1-np.exp(v1-v2)
age1=70
age2=71
hbA1c=6
female=True
ATFIB=False
HDL=60
heart_rate=80
SBP=100
WBC=8
diabetes_years=8
MIC_ALB,PVD,Stroke_Hist=(False,False,False)
print(first_amputation(age1,age2,hbA1c,female,ATFIB,HDL,heart_rate,SBP,WBC,MIC_ALB,PVD,Stroke_Hist,diabetes_years))

