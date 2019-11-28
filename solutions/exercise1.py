'''
Filippo Aleotti
filippo.aleotti2@unibo.it

29 November 2019
I PROFESSIONAL MASTER'S PROGRAM, II LEVEL "SIMUR", Imola 2019

Create a Python function that, given three numbers as input A,B and C, return 
the sum of A and B if C is multiple of 9, otherwise the subtraction between
C and 3 times B, powered by A.  
'''

def crazy_func(A,B,C):
    remainder = C % 9
    result = None
    if remainder == 0:
         result = A+B 
    else: 
        result = (C-3*B)**A
    return result


first_call  = crazy_func(A=3, B=1, C=5)
second_call = crazy_func(A=2, B=1, C=18)

assert first_call  == 8
assert second_call == 3
