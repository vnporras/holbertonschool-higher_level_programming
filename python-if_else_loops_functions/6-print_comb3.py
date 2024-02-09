#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(num1+1, 10):
        print("{}{}{}".format(num1, num2, '\n' if num1 == 8 and num2 == 9 else ', '), end='')
