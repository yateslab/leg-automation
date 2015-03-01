#!/usr/bin/env python 

import os
import glob
path = r"C:\Users\Yateslab\Dropbox\ethancode\Leg_Automation\Static_Histograms" #Directory we want to search. Need to put an r in front to avoid unicode escape
os.chdir(path)
file_names = glob.glob('*.*.txt') 
print(file_names) 

import itertools

for histogram in file_names:
	with open(str(histogram)+"_MidA.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 1, 61):
				print(line.rstrip().split('\t')[1], file=ostr)
	with open(str(histogram)+"_ME.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 61, 71):
				print(line.rstrip().split('\t')[1], file=ostr)
							
	with open(str(histogram)+"_ext.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 71, 131):
				print(line.rstrip().split('\t')[1], file=ostr)	
				
	with open(str(histogram)+"_EM.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 131, 141):
				print(line.rstrip().split('\t')[1], file=ostr)
	
	with open(str(histogram)+"_MidB.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 141, 201):
				print(line.rstrip().split('\t')[1], file=ostr)
				
	with open(str(histogram)+"_MF.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 201, 211):
				print(line.rstrip().split('\t')[1], file=ostr)
	
	with open(str(histogram)+"_flex.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 211, 271):
				print(line.rstrip().split('\t')[1], file=ostr)
	
	with open(str(histogram)+"_FM.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 271, 281):
				print(line.rstrip().split('\t')[1], file=ostr)
	
	with open(str(histogram)+"_ME2.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 56, 71):
				print(line.rstrip().split('\t')[1], file=ostr)
	
	with open(str(histogram)+"_ME3.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 56, 76):
				print(line.rstrip().split('\t')[1], file=ostr)
	
	with open(str(histogram)+"_EM2.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 126, 141):
				print(line.rstrip().split('\t')[1], file=ostr)
	
	with open(str(histogram)+"_EM3.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 126, 146):
				print(line.rstrip().split('\t')[1], file=ostr)
	
	with open(str(histogram)+"_FM2.csv",'w') as ostr:
		with open(histogram) as file:
			for line in itertools.islice(file, 266, 280):
				print(line.rstrip().split('\t')[1], file=ostr)
	