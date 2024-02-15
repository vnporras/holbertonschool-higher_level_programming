#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    listA = list(tuple_a)
    listB = list(tuple_b)

    if len(listA) == 1:
        listA.append(0)

    if len(listA) == 0:
        listA.append(0)
        listA.append(0)

    if len(listB) == 1:
        listB.append(0)

    if len(listB) == 0:
        listB.append(0)
        listB.append(0)

    tA = tuple(listA)
    tB = tuple(listB)

    return (tA[0] + tB[0], tA[1] + tB[1])
