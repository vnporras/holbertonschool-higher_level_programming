#!/usr/bin/python3
def multiple_returns(sentence):
    firstChar = ""
    sentenceSize = len(sentence)

    if sentenceSize == 0:
        firstChar = None
    else:
        firstChar = sentence[0]

    return (sentenceSize, firstChar)
