input_data = [
    199, 200, 208, 210, 200, 
    207, 240, 269, 260, 263,
]

count = 0
for i in range(1, len(input_data)):
   if input_data[i] > input_data[i-1]:
    count += 1
    
print('How many measurements are larger than the previous measurement?')
print(count)

