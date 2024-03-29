#!/usr/bin/python3

def common_elements(set_1, set_2):
    resultDictionary = {}
    resultList = []

    for i in set_1:
        valueDictionary = resultDictionary.get(i)
        if valueDictionary is None:
            resultDictionary[i] = 1
        else:
            resultDictionary[i] = valueDictionary + 1

    for i in set_2:
        valueDictionary = resultDictionary.get(i)
        if valueDictionary is None:
            resultDictionary[i] = 1
        else:
            resultDictionary[i] = valueDictionary + 1

    for i in resultDictionary:
        if resultDictionary[i] >= 2:
            resultList.append(i)

    return resultList
