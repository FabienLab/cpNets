from src.learnCPnet import *

modeForDatasetGeneration = 2 # 1 = read a file, 2 = generate a synthetic database
nameOfFile = "databases/sushi_30Users_10000Comparisons.data"
numberOfComparisons = 1500000 # -1 = all of the comparisons in file
percentageOfNoise = [0,10,20,30,40,50,60,70,80,90,100] # between 0 and 50
numberOfVariables = 12 # -1 = automatically choose from the number of comparisons
numberOfEdgesLambda = -1 # -1 = infinity
numberOfParentsForTargetCPNet = -1 # -1 = infinity
numberOfParentsForLearnedCPNet = -1 # -1 = infinity
numberOfRoundsForFileGeneration = 1
numberOfRoundsForLearningProcedure = 10 # = percentage taken in the dataset for the cross validation

decisionThresholdBis = 0.1 # delta for decisionMode = 1
epsilonThreshold = 0.05 # threshold for epsilon

convergence = False

online = True
offline = False
autorizedCycle = False

# 1 = McDiarmid for conditioned variable, 2 = McDiarmid for conditioned AND conditional variables
decisionMode = 2



averageCycleSize2,aOnline,aOnlineLog,sdAOnline,sdAOnlineLog,aOffline,aOfflineLog,sdAOffline,sdAOfflineLog,tOnline,sdTOnline,meanIT,sdIT,tOffline,sdTOffline,meanAccNoiseOnline,meanAccNoiseOnlineLog,sdANoiseOnline,sdANoiseOnlineLog,meanAccNoiseOffline,meanAccNoiseOfflineLog,sdANoiseOffline,sdANoiseOfflineLog,lenOfFold,numberOfAttributes,meanConvergenceAccuracyOnline,meanConvergenceAccuracyOnlineLog,sdConvergenceAccuracyOnline,sdConvergenceAccuracyOnlineLog,meanConvergenceAccuracyOffline,meanConvergenceAccuracyOfflineLog,sdConvergenceAccuracyOffline,sdConvergenceAccuracyOfflineLog = generalProcedure(modeForDatasetGeneration,nameOfFile,numberOfComparisons,percentageOfNoise,numberOfVariables,numberOfEdgesLambda,numberOfParentsForTargetCPNet,numberOfParentsForLearnedCPNet,numberOfRoundsForFileGeneration,numberOfRoundsForLearningProcedure,decisionThresholdBis,epsilonThreshold,convergence,online,offline,decisionMode,None,autorizedCycle)
print(displayParameters(modeForDatasetGeneration,nameOfFile,numberOfComparisons,percentageOfNoise,numberOfVariables,numberOfEdgesLambda,numberOfParentsForTargetCPNet,numberOfParentsForLearnedCPNet,numberOfRoundsForFileGeneration,numberOfRoundsForLearningProcedure,decisionThresholdBis,lenOfFold,numberOfAttributes,online) + "\n" + displayResults(modeForDatasetGeneration,averageCycleSize2,percentageOfNoise,aOnline,aOnlineLog,sdAOnline,sdAOnlineLog,aOffline,aOfflineLog,sdAOffline,sdAOfflineLog,tOnline,sdTOnline,meanIT,sdIT,tOffline,sdTOffline,meanAccNoiseOnline,meanAccNoiseOnlineLog,meanAccNoiseOffline,meanAccNoiseOfflineLog,lenOfFold,online,offline,""))
convfileTestOnline = open("test-results/test_noise_resist_Online.dat","w")
tab1 = []
tab2 = []
tab3 = []
tab4 = []
for key in meanAccNoiseOnline.keys():
	tab1.append([key,meanAccNoiseOnline[key]])
	tab2.append([key,sdANoiseOnline[key]])
	tab3.append([key,meanAccNoiseOnlineLog[key]])
	tab4.append([key,sdANoiseOnlineLog[key]])
tab1.sort()
tab2.sort()
tab3.sort()
tab4.sort()
convfileTestOnline.write("0 0.0 0.0 0.0 0.0\n")
for i in range(1,len(tab1)):
	convfileTestOnline.write(str(tab1[i][0]) + " " + str(100 - tab1[i][1]) + " " + str(tab2[i][1]) + " " + str(abs(tab3[i][1])) + " " + str(tab4[i][1]) + "\n")
convfileTestOnline.close()
