import csv
import random
import math

def loadFile(fn):
    lines = csv.reader(open(fn,"r"))
    dataset = list(lines)
    return dataset

def convert(dataset):
    data = {}
    for row in dataset:
        for item in row:
            if item not in data:
               data[item] = 0
    for row in dataset:
        for item in row:
            data[item]+= 1
    for row in range(len(dataset)):
        for col in range(len(dataset[row])):
            dataset[row][col] = float(data[dataset[row][col]])
    return dataset


def splitData(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet= []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return trainSet, copy

def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if vector[len(vector)-1] not in separated:
            separated[vector[len(vector) -1]] = []
        separated[vector[len(vector) - 1]].append(vector)
    print (separated)
    return separated

def mean(numbers):
    sum1 = 0
    for x in range(len(numbers)-2) :
        sum1 += float(numbers[x])
    return sum1/float(len(numbers))

def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

def summarize(dataset):
    summaries =[(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries

def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries

def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev)) * exponent

def classProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities

def predict(summaries, inputVector):
    probabilities = classProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel

def getPredictions(summaries,testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions

def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(testSet))) * 100

def main():
    fn = '/Users/parth/PycharmProjects/MachineLearningHW1/mushroom.csv'
    splitRatio = 0.68
    dataset = loadFile(fn)
    dataset = convert(dataset)
    trainingSet, testSet = splitData(dataset, splitRatio)
    print ('Split %d rows into train = %d and test = %d' %(len(dataset), len(trainingSet), len(testSet)))
    # Train
    summaries = summarizeByClass(trainingSet)
    # test
    predictions = getPredictions(summaries, testSet)
    accuracy = getAccuracy(testSet, predictions)
    print (accuracy)

main()





