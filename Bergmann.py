import matplotlib.pyplot as pyplot

def Bergmann(params,deltaT,steps,G,I,X):
	t=deltaT
	Gb=params['Gb']['val']
	n=params['n']['val']
	h=params['h']['val']
	Ib=params['Ib']['val']
	gamma=params['gamma']['val']
	gamma*=400
	p1,p2,p3=(params['p1']['val'],params['p2']['val'],params['p3']['val'])
	diffI=-n*max((I-Ib),0)+max(gamma*(G-h)*t,0)+Ib
	print("zero",gamma*(G-h)*t)
	diffX=p2*X+p3*max((I-Ib),0)

	diffG=(p1-X)*G-p1*Gb
	## G will converge at k1Gb, Gb is the base Glucose level, k1 and k2 are constants
	## X will converge at -p3*I/p2
	## I will converge at k2Ib
	## TODO: Add a variable represent 
	## Ib: basic Insuline level
	return diffI,diffG,diffX

params={'gamma':{'val':5.36*10**(-3),'unit':'uU/mgmin^2'},'p1':{'val':-2.96/100,'unit':'1/min'},'p2':{'val':-0.86/100,'unit':'1/min'},'p3':{'val':6.51/1000000,'unit':'ml/uUmin^2'},'p4':{'val':0.098,'unit':'1/ml'},'n':{'val':0.142,'unit':'1/min'},'I0':{'val':25,'unit':'uU/ml'},'h':{'val':90.9,'unit':'mg/dL'},'n':{'val':0.23,'unit':'min-1'},'G0':{'val':126,'unit':'mg/dL'}}
params['Gb']={'val':120,'unit':'dL'}
params['Ib']={'val':5,'unit':'uU/mL'}
def update(params,deltaT,steps):
	results=list()
	G,I,X=(params['G0']['val'],params['I0']['val'],0)
	results.append([G,I,X])
	for i in range(1,steps-1):			
		diffI,diffG,diffX=Bergmann(params,deltaT,i,G,I,X)
		G+=deltaT*diffG
		I+=deltaT*diffI
		## Diet event, suppose the patient takes a diet after 200 mins
		## TODO: Dirac Delta function should be a better choice than +=60
		'''
		if i==int(steps/2):
			G+=60
		'''
		X+=deltaT*diffX
		results.append([G,I,X])
	return results

def plot(results,deltaT,steps,mode='Glucose'):
	g=list()
	for i in range(len(results)):
		print(results[i],results[i][0])
		if mode=='Glucose':
			g.append(results[i][0])
		else:
			g.append(results[i][1])
	t=list(range(0,len(g)))
	plt=pyplot.plot(t,g)
	pyplot.show()

results=update(params,1,400)
plot(results,1,200,mode='Insulin')


