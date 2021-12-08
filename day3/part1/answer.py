from functools import reduce
from pathlib import Path

def get_input(type=str, strip_newlines=True):
    input = Path(__file__).with_name('input.txt')
    for line in input.open('r').readlines():
        if strip_newlines:
            line = line.strip('\n')
        yield line

# todo Convert rows to decimal and calculate?

def str_to_int_list(str):
    return list(map(int, list(str)))

def add_element_wise(a,b):
    return list(map(lambda x,y: x+y, a,b))

def implode(list):
    return reduce(lambda x,y: str(x) + str(y), list, '')

# todo Set dynamically 
sum = [0,0,0,0,0,0,0,0,0,0,0,0]
input = list(get_input())
for str in input:
    sum = add_element_wise(sum, str_to_int_list(str))

# Binary string formed from most common.    
bin_most_common = ''
bin_least_common = ''

half_length = len(input) / 2
for summed_bit in sum:
    if summed_bit >= half_length: # Prefer 1 if counts are same
        bin_most_common += '1'
        bin_least_common += '0'
    else:
        bin_most_common += '0'
        bin_least_common += '1'

dec_most_common = int(bin_most_common, 2)
dec_least_common = int(bin_least_common, 2)

result = dec_most_common * dec_least_common
print('What is the power consumption of the submarine?')
print(result)
# Result: 1997414
