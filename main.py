##'Bergman minimal Model'
import numpy as np
import pandas as pd
parameters=pd.read_csv('parameters.csv')
events=['Stroke','InsulinResistance','Retinopathy','RetinalDetachment','Diet']
class Pancreas():
	def __init__(self,BetaCellCount):
		self.BetaCellCount=BetaCellCount
class Blood():
	def __init__(self,GlucoseLevel,InsulinLevel,OxygenLevel,LipidLevel,ImmuneCells)
		self.GlucoseLevel=GlucoseLevel
		self.InsulinLevel=InsulinLevel
		self.OxygenLevel=OxygenLevel
		self.LipidLevel=LipidLevel
		self.ImmuneCells=ImmuneCells
class edge():
	def __init__(leftnode,rightnode,weight,operation):
		self.leftnode=leftnode
		self.rightnode=rightnode
		self.simulator=simulator
		self.operation=operation
		## Weight of an edge is the computation matrix between 2 variables

	def update(self,deltaT):
		self.simulator.update()
class simulator():
	def __init__(mode,method,params,leftnode,rightnode):
		self.mode=mode
		self.method=method
		self.params=params
		self.check_valid()
		## params should be a map such as {'initial probabilities','transition matrix'} in case of discrete markov model

	def check_valid(self):
		available_modes=['LinearODE']
		if self.mode not in available_modes:
			raise ValueError('Unknown model! Please pick another one or check the documentation for correct syntax!')
		elif self.mode=='LinearODE':
			if self.params.values[0].size!=(len(leftnode),len(rightnode)):
				raise ValueError('Incorrect Dimensionality!')

	def update(self,dT):
		if self.method=='EulerMethod':
			self.rightnode+=dT*np.dot(params,self.leftnode.transpose())

class model():
	def __init__(self,time,nodes,edges):
		self.time=time
		self.nodes=nodes
		self.edges=edges
	def update(self):
		for edge in self.edges:
			edge.update()

def Init():
	blood=Blood(GlucoseLevel,InsulinLevel,OxygenLevel,LipidLevel,ImmuneCells)
	pancreas=Pancreas(BetaCellCount)
