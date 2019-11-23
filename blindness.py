import numpy as np
from numpy.random import normal
def Blindness_vector(age,hbA1c,heart_rate,SBP,WBC,CHF_HIST,IHD_HIST,diabetes_years):
	vector=-11.607+age*0.047+hbA1c*0.171+heart_rate/10*0.080+0.068*SBP/10+WBC*0.052
	if CHF_HIST:
		vector+=0.841
	if IHD_HIST:
		vector+=0.610
	'''
	se_vector=Blindness_SE(age,hbA1c,heart_rate,SBP,WBC,CHF_HIST,IHD_HIST,diabetes_years)
	vector+=se_vector*normal(0,0.1,1)
	print("se_vector",normal(0,0.1,1),vector)
	'''
	return np.exp(vector)*diabetes_years
def Blindness(age1,age2,hbA1c,heart_rate,SBP,WBC,CHF_HIST,IHD_HIST,diabetes_years):
	v1=Blindness_vector(age1,hbA1c,heart_rate,SBP,WBC,CHF_HIST,IHD_HIST,diabetes_years)
	v2=Blindness_vector(age2,hbA1c,heart_rate,SBP,WBC,CHF_HIST,IHD_HIST,diabetes_years+age2-age1)
	print("v1","v2",v1,v2)
	return 1-np.exp(v1-v2)

def Blindness_SE(age,hbA1c,heart_rate,SBP,WBC,CHF_HIST,IHD_HIST,diabetes_years):
	vector=0.759+age*0.009+hbA1c*0.032+heart_rate/10*0.039+0.032*SBP/10+WBC*0.019
	if CHF_HIST:
		vector+=0.287
	if IHD_HIST:
		vector+=0.208
	return vector
age1=70 ##age of the patient unit: year 
age2=71 ##age of the patient unit: year 
hbA1c=6 ##Hemoglobin A1cv unit:%
heart_rate=80 ##Heart rate unit: times/min
SBP=100 ##Blood Pressure unit: mmHg
WBC=8   ##White Blood Cell count unit:10^6/ml
CHF_HIST=True ##History of CHF complication unit: Boolean
IHD_HIST=True ##History of IHD complication unit: Boolean
diabetes_years=20 ##History of Diabetes unit: year
## Reference:https://static-content.springer.com/esm/art%3A10.1007%2Fs00125-013-2940-y/MediaObjects/125_2013_2940_MOESM1_ESM.pdf
print("probability of a IHD/CHF hist patient gets blind between 70-71 years old:",Blindness(age1,age2,hbA1c,heart_rate,SBP,WBC,CHF_HIST,IHD_HIST,diabetes_years))



