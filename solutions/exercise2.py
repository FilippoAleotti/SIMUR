'''
Create a Python function that, given a word as input, return True if that world is palindrome, False otherwise 
'''

def palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

apple_call = palindrome('apple')
abba_call  = palindrome('abba')

assert apple_call  == False
assert abba_call   == True 