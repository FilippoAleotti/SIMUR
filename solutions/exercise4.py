'''
Filippo Aleotti
filippo.aleotti2@unibo.it

29 November 2019
I PROFESSIONAL MASTER'S PROGRAM, II LEVEL "SIMUR", Imola 2019

Modify the function realised in the previous exercise to return (inside the dict, using the key min) also the value with minimum frequency. 
If more values have the same minimum frequency, then return the lowest one
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
    min_value = None
    #NOTE: val are str, so we need an int cast to obtain integer values
    for val, freq in output_dict.items():
        if min_value == None:
            #NOTE: at first iteration, we will always enter here
            min_value = int(val)
        else:
            if freq < output_dict[str(min_value)]:
                # this frequency value is lower than the frequency of the current minimum,
                # so we have to update the current minimum
                min_value = int(val)
            elif freq ==  output_dict[str(min_value)] and min_value > int(val):
                # the frequency is equal to the frequency of minimum.
                # We have to update the minimum only if the current minimum
                # is greather than this value
                min_value = int(val)
    output_dict['min'] = min_value
    return output_dict

frequency_1  = frequency_extractor([0,1,0,2,2,1,2,1,0,0,2,1,1])
frequency_2  = frequency_extractor([1,2,2,2,1,5,3,1])

assert are_equals(frequency_1, {'0':4,'1':5,'2':4,'min':0}) == True
assert are_equals(frequency_2, {'1':3,'2':3,'3':1,'5':1, 'min':3}) == True
