#program to calculate to 5 decimal places the probability of getting heads vs. tails printing
#frequency and probability along the way in 20k increments.
from random import randint

#setting values
heads = 0
probability = 0.0
finding = '.50000'
freq = 0

while str(probability).find(finding) < 1:
	
	#assign 0 or 1
	heads += randint(0,1)
	
	#determine freq 1 to avoid dividing by zero
	freq += 1
	
	#P(H) = 1 - P(T)
	#	P(T) = #Tails / (P(T)+P(H))
	# 	AKA: number results of one divided by total results.
	probability = float(heads) / freq

	#printing every 20k results
	if freq % 20000 == 0:
		print 'freq: %d \t probability: %f' % (freq, float(probability))

print 'freq: %d \t probability: %f' % (freq,float(probability))

	
	
	



