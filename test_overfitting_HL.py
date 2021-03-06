from src.learnCPnet import *

modeForDatasetGeneration = 2 # 1 = read a file, 2 = generate a synthetic database
nameOfFile = "databases/sushi_30Users_10000Comparisons.data"
numberOfComparisons = [5000,50000,200000] # -1 = all of the comparisons in file
percentageOfNoise = [0,10] # between 0 and 50
numberOfVariables = 12 # -1 = automatically choose from the number of comparisons
numberOfEdgesLambda = -1 # -1 = infinity
numberOfParentsForTargetCPNet = -1 # -1 = infinity
numberOfParentsForLearnedCPNet = -1 # -1 = infinity
numberOfRoundsForFileGeneration = 10
numberOfRoundsForLearningProcedure = 1 # = percentage taken in the dataset for the cross validation

decisionThresholdBis = 0.1 # delta for decisionMode = 1
epsilonThreshold = 0.05 # threshold for epsilon

convergence = False

online = False
offline = True
autorizedCycle = False

# 1 = McDiarmid for conditioned variable, 2 = McDiarmid for conditioned AND conditional variables
decisionMode = 2



for numberOfComparisons in [5000,50000,200000]:
	fileTestHL = {}
	for i in percentageOfNoise:
		fileTestHL[i] = open("test-results/test_overfitting_" + str(i) + "_noise_" + str(numberOfComparisons) + "_Offline.dat","w")
	for numberOfParentsForLearnedCPNet in [0,1,2,4,6,8,11]:
		averageCycleSize2,aOnline,aOnlineLog,sdAOnline,sdAOnlineLog,aOffline,aOfflineLog,sdAOffline,sdAOfflineLog,tOnline,sdTOnline,meanIT,sdIT,tOffline,sdTOffline,meanAccNoiseOnline,meanAccNoiseOnlineLog,sdANoiseOnline,sdANoiseOnlineLog,meanAccNoiseOffline,meanAccNoiseOfflineLog,sdANoiseOffline,sdANoiseOfflineLog,lenOfFold,numberOfAttributes,meanConvergenceAccuracyOnline,meanConvergenceAccuracyOnlineLog,sdConvergenceAccuracyOnline,sdConvergenceAccuracyOnlineLog,meanConvergenceAccuracyOffline,meanConvergenceAccuracyOfflineLog,sdConvergenceAccuracyOffline,sdConvergenceAccuracyOfflineLog = generalProcedure(modeForDatasetGeneration,nameOfFile,numberOfComparisons,percentageOfNoise,numberOfVariables,numberOfEdgesLambda,numberOfParentsForTargetCPNet,numberOfParentsForLearnedCPNet,numberOfRoundsForFileGeneration,numberOfRoundsForLearningProcedure,decisionThresholdBis,epsilonThreshold,convergence,online,offline,decisionMode,None,autorizedCycle)
		for i in percentageOfNoise:
			fileTestHL[i].write(str(numberOfParentsForLearnedCPNet) + " " + str(aOffline[i]) + " " + str(sdAOffline[i]) + " " + str(aOfflineLog[i]) + " " + str(sdAOfflineLog[i]) + " " + str(meanAccNoiseOffline[i]) + " " + str(sdANoiseOffline[i]) + " " + str(meanAccNoiseOfflineLog[i]) + " " + str(sdANoiseOfflineLog[i]) + "\n")
	for i in percentageOfNoise:
		fileTestHL[i].close()
