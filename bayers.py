# import collections
# array = []
# with open("D:\Fall 2017\Big Data\comp7970\Dataset\CA-GrQc.txt", 'r') as searchfile:
#     for line in searchfile:
#         ew_array = np.array((array.float(i) for i in line.split(' ')))
#         arrays.append(new_array)
import random
dictionary = {}
prevVal = ""
with open("D:\Fall 2017\Big Data\comp7970\Dataset\CA-GrQc.txt") as f:
    j = 0
    for line in f:
        val, trash = line.split()
        if(val != prevVal):
            dictionary[j] = int(val)
            prevVal = val
            j = j + 1
    big = dictionary[0]
    small = dictionary[0]
    for i in range(0, 5242):
        if(dictionary[i] > big):
            big = dictionary[i]
        if(dictionary[i] < small):
            small = dictionary[i]
    print big
    print small


# def splitDataset(dataset, splitRatio):
#     trainSize = int(len(dataset) * splitRatio)
# 	trainSet = []
# 	copy = list(dataset)
# 	while len(trainSet) < trainSize:
# 		index = random.randrange(len(copy))
# 		trainSet.append(copy.pop(index))
# 	return [trainSet, copy]