##'Bergman minimal Model'
import numpy as np
import pandas as pd
parameters=pd.read_csv('parameters.csv')
events=['Stroke','InsulinResistance','Retinopathy','RetinalDetachment']
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
