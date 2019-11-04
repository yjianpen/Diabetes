import matplotlib.pyplot as pyplot
def Bergmann(params,deltaT,steps,G,I,X):
	t=deltaT
	Gb=params['Gb']['val']
	n=params['n']['val']
	h=params['h']['val']
	gamma=params['gamma']['val']
	p1,p2,p3=(params['p1']['val'],params['p2']['val'],params['p3']['val'])
	diffI=-n*I+max(gamma*(G-h)*t,0)
	print("zero",gamma*(G-h)*t)
	diffX=p2*X+p3*I
	diffG=(p1-X)*G-p1*Gb
	return diffI,diffG,diffX

params={'gamma':{'val':5.36*10**(-3),'unit':'uU/mgmin^2'},'p1':{'val':-2.96/100,'unit':'1/min'},'p2':{'val':-1.86/100,'unit':'1/min'},'p3':{'val':6.51/1000000,'unit':'ml/uUmin^2'},'p4':{'val':0.098,'unit':'1/ml'},'n':{'val':0.142,'unit':'1/min'},'I0':{'val':200,'unit':'uU/mgmin^2'},'h':{'val':90.9,'unit':'mg/dL'},'n':{'val':0.23,'unit':'min-1'},'G0':{'val':298,'unit':'mg/dL'},'I0':{'val':300,'unit':'uU/mL'}}
params['Gb']={'val':92.6,'unit':'dL'}
def update(params,deltaT,steps):
	results=list()
	G,I,X=(params['G0']['val'],params['I0']['val'],0)
	results.append([G,I,X])
	for i in range(1,steps-1):			
		diffI,diffG,diffX=Bergmann(params,deltaT,i,G,I,X)
		G+=deltaT*diffG
		I+=deltaT*diffI
		X+=deltaT*diffX
		results.append([G,I,X])
	return results

def plot(results,deltaT,steps):
	g=list()
	for i in range(len(results)):
		print(results[i],results[i][0])
		g.append(results[i][0])
	t=list(range(0,len(g)))
	plt=pyplot.plot(t,g)
	pyplot.show()

results=update(params,1,200)
plot(results,1,200)


