'''
Filippo Aleotti
filippo.aleotti2@unibo.it

29 November 2019
I PROFESSIONAL MASTER'S PROGRAM, II LEVEL "SIMUR", Imola 2019

Create a Python function that, given a word as input, return True if that world is palindrome, False otherwise 
'''

def palindrome(word):
    # we have to check half the string, 
    is_palindrome = True
    length = len(word)-1
    for i in range(int(len(word)/2)):        
        if word[i] != word[length -i]:
            is_palindrome = False
    return is_palindrome

apple_call = palindrome('apple')
abba_call  = palindrome('abba')
abcba_call  = palindrome('abcba')


assert apple_call  == False
assert abba_call   == True 
assert abcba_call  == True