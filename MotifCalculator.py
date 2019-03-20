import numpy as np
import matplotlib.pyplot as pylab
import random


def generateAverages(N, a, t, c, g, motif):
	times = 0
	for trial in range(N):
		simulation = createRandSequence(N, a, t, c, g)
		if str.find(motif, simulation[trial]) > 0:
			times += 1

	average = times/100
	#print(average)
	return average

def createRandSequence(length, a, t, c, g):
	sequenceList = ""
	for nucleotide in range(length):
		rand = random.random()
		if rand < a/100:
			sequenceList += "A"
		elif rand >= a/100 and rand < (a+t)/100:
			sequenceList += "T"
		elif rand >= (a+t)/100 and rand <(a+t+c)/100:
			sequenceList += "C"
		else:
			sequenceList += "G"

	return sequenceList



allowed = ['a','t','c','g', 'A', 'T', 'C', 'G']
prob = 1
probList = []

done = False
while done == False:
	motif = input("Enter a specific motif (a string of A, T, C, and G's.): ")
	badChars = [letter.lower() for letter in motif if letter.lower() not in allowed]
	motif.upper()
	if len(badChars) > 0:
		print("Invalid motif. Only A's, C's, T's, and G's! ")
	else:
		freqA = int(input("Enter the frequency for the nucleotide A: "))
		freqT = int(input("Enter the frequency for the nucleotide T: "))
		freqC = int(input("Enter the frequency for the nucleotide C: "))
		freqG = int(input("Enter the frequency for the nucleotide G: "))
		if (freqA + freqT + freqC + freqG) != 100:
			print("Your frequencies do not add up to 100.")
		else:
			done = True




for letter in range(len(motif)):
	if motif[letter] == 'a' or motif[letter] == 'A':
		prob *= freqA
	elif motif[letter] == 't' or motif[letter] == 'T':
		prob *= freqT
	elif motif[letter] == 'g' or motif[letter] == 'G':
		prob *= freqG
	elif motif[letter] == 'c' or motif[letter] == 'C':
		prob *= freqC

prob/= 100**len(motif)

print("Motif: ", motif)
print("Nucleotide ", "Frequency".ljust(5))
print("A".ljust(12), str(freqA), "%")
print("T".ljust(12), str(freqT), "%")
print("C".ljust(12), str(freqC), "%")
print("G".ljust(12), str(freqG), "%")
print("Probability of appearing in a sequence N = ", len(motif), "is ", prob, "or ", prob*100, "%.")


pylab.figure("User Probability of finding >= 1 Sequence from N to 5000")
#pylab.plot
pylab.axis(xmin=0, xmax = 5000, ymin = 0, ymax = 1)
pylab.xlabel('Sequence Length')
pylab.ylabel('Prob of finding at least one Motif')

for n in range (1, 5001):
	oneMotif = 1 - (1-prob)**n
	probList.append(oneMotif)

pylab.plot(probList)
pylab.show()

# sequence100 = createRandSequence(100, freqA, freqT, freqC, freqG)
# sequence1000 = createRandSequence(1000, freqA, freqT, freqC, freqG)
# sequence2000 = createRandSequence(2000, freqA, freqT, freqC, freqG)
# sequence5000 = createRandSequence(5000, freqA, freqT, freqC, freqG)
# sequence10000 = createRandSequence(10000, freqA, freqT, freqC, freqG)
#times = 0
#for trial in range(100):
#	simulation = createRandSequence(100, freqA, freqT, freqC, freqG)
#	if str.find(motif, simulation[trial]) > 0:
#		times += 1
#average = times/100

averageN100 = generateAverages(100, freqA, freqT, freqC, freqG, motif)
averageN1000 = generateAverages(1000, freqA, freqT, freqC, freqG, motif)
averageN2000 = generateAverages(2000, freqA, freqT, freqC, freqG, motif)
averageN5000 = generateAverages(5000, freqA, freqT, freqC, freqG, motif)
averageN10000 = generateAverages(10000, freqA, freqT, freqC, freqG, motif)

averages = np.array([averageN100, averageN1000, averageN2000, averageN5000, averageN10000])
intervals = np.array([100,1000,2000,5000,10000])


pylab.figure("Expected number of motifs in sequences of length N = 100, N = 1000, N = 2000, N = 5000, and N = 10000")
pylab.axis(xmin=0, xmax = 10000, ymin = 0, ymax = 50)
pylab.plot(intervals, averages, 'ro', markersize = 50)

pylab.show()