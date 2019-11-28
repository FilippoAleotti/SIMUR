'''
Filippo Aleotti
filippo.aleotti2@unibo.it

29 November 2019
I PROFESSIONAL MASTER'S PROGRAM, II LEVEL "SIMUR", Imola 2019

Given a list of integer, store the frequency of each value in a dict, where the key is the value. 
'''

def are_equals(dict1, dict2):
    ''' check if two dict are equal.
        Both the dicts have str keys and integer values
    '''
    for k,v in dict1.items():
        if k not in dict2.keys():
            return False
        if dict2[k] !=  v:
            return False
    return True


def frequency_extractor(input_list):
    output_dict = {}
    for element in input_list:
        if str(element) not in output_dict.keys():
            output_dict[str(element)] = 1
        else:
            output_dict[str(element)] += 1
    return output_dict

frequency_1  = frequency_extractor([0,1,0,2,2,1,2,1,0,0,2,1,1])
frequency_2  = frequency_extractor([1,2,2,2,0,5,3])

assert are_equals(frequency_1, {'0':4,'1':5,'2':4})
assert are_equals(frequency_2, {'0':1,'1':1,'2':3,'3':1,'5':1})
