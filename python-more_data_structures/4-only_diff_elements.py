#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
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
        if resultDictionary[i] == 1:
            resultList.append(i)

    return resultList

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))