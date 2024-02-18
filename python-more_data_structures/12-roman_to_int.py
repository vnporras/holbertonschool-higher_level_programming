#!/usr/bin/python3

def units(units_string):
    match units_string:
        case "I":
            return 1
        case "II":
            return 2
        case "III":
            return 3
        case "IV":
            return 4
        case "V":
            return 5
        case "VI":
            return 6
        case "VII":
            return 7
        case "VIII":
            return 8
        case "IX":
            return 9
        case _:
            return 0
        
def tens(tens_string):
    match tens_string:
        case "X":
            return 10
        case "XX":
            return 20
        case "XXX":
            return 30
        case "XL":
            return 40
        case "L":
            return 50
        case "LX":
            return 60
        case "LXX":
            return 70
        case "LXXX":
            return 80
        case "XC":
            return 90
        case _:
            return 0
        
def hundreds(hundreds_string):
    match hundreds_string:
        case "C":
            return 100
        case "CC":
            return 200
        case "CCC":
            return 300
        case "CD":
            return 400
        case "D":
            return 500
        case "DC":
            return 600
        case "DCC":
            return 700
        case "DCCC":
            return 800
        case "CM":
            return 900
        case _:
            return 0
        
def thousands(thousands_string):
    match thousands_string:
        case "M":
            return 1000
        case "MM":
            return 2000
        case "MMM":
            return 3000
        case _:
            return 0


def roman_to_int(roman_string): # XIX
    if type(roman_number) != str or roman_number == None:
        return 0
    
    thousandsString = ""
    hundredsString = ""
    tensString = ""
    unitsString = ""

    for index, value in enumerate(roman_string):
        if roman_string[index] == "M":
            thousandsString += value
        
        if roman_string[index] == "C" or roman_string[index] == "D":
            hundredsString += value

        if (roman_string[index] == "X" and roman_string[index - 1] != "I") or roman_string[index] == "L":
            tensString += value

        if roman_string[index] == "I" or roman_string[index] == "V" or (roman_string[index] == "X" and roman_string[index - 1] == "I"):
            unitsString += value

    romanInteger = 0
    romanInteger += thousands(thousandsString)
    romanInteger += hundreds(hundredsString)
    romanInteger += tens(tensString)
    romanInteger += units(unitsString)

    return romanInteger