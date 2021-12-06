from pathlib import Path

def get_input():
    input = Path(__file__).with_name('input.txt')
    return list(map(int, input.open('r').readlines()))

input_data = get_input()
count = 0
for i in range(1, len(input_data)):
   if input_data[i] > input_data[i-1]:
    count += 1
    
print('How many measurements are larger than the previous measurement?')
print(count)

# ANSWER: 1832
