#!/usr/bin/env python 

import os
import glob
path = r"C:\Users\Yateslab\Dropbox\ethancode\Leg_Automation\Static_Histograms" #Directory we want to search. Need to put an r in front to avoid unicode escape
os.chdir(path)
file_names = glob.glob('*.*.txt') 
print(file_names) 

import csv
import itertools
for histogram in file_names:
	with open(histogram,'rt') as tsvin, open(str(histogram)+"_MidA.tsv",'w') as MidA, open(str(histogram)+"_ME.tsv",'w') as ME, open(str(histogram)+"_ext.tsv",'w') as ext, open(str(histogram)+"_EM.tsv",'w') as EM, open(str(histogram)+"_MidB.tsv",'w') as MidB, open(str(histogram)+"_MF.tsv",'w') as MF, open(str(histogram)+"_flex.tsv",'w') as flex, open(str(histogram)+"_FM.tsv",'w') as FM, open(histogram + "_1col",'w') as tsvout:
		tsvin = csv.reader(tsvin, delimiter='\t')
		MidA = csv.writer(MidA, delimiter='\t')
		ME = csv.writer(ME, delimiter='\t')
		ext = csv.writer(ext, delimiter='\t')
		EM = csv.writer(EM, delimiter='\t')
		MidB = csv.writer(MidB, delimiter='\t')
		MF = csv.writer(MF, delimiter='\t')
		flex = csv.writer(flex, delimiter='\t')
		FM = csv.writer(FM, delimiter='\t')
		tsvout = csv.writer(tsvout, delimiter='\t')
		for row in tsvin:
			tsvout.writerows(row[1])
		for row in itertools.islice(tsvout,1,61):
			#print(row)
			MidA.writerow(row)
		for row in itertools.islice(tsvout,62,71):
			ME.writerow(row)
		for row in itertools.islice(tsvin,72,131):
			ext.writerow(row)
		for row in itertools.islice(tsvout,132,141):
			EM.writerow(row)
		for row in itertools.islice(tsvout,142,201):
			MidB.writerow(row)
		for row in itertools.islice(tsvout,201,211):
			MF.writerow(row)
		for row in itertools.islice(tsvout,212,271):
			flex.writerow(row)
		for row in itertools.islice(tsvout,272,281):
			FM.writerow(row)	
#with open(')