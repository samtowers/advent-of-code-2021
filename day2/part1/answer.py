from pathlib import Path

def get_input(type=str):
    input = Path(__file__).with_name('input.txt')
    return list(map(type, input.open('r').readlines()))

def parse_coord_delta(str):
    direction, amount = str.split(' ')
    match direction:
        case 'forward':
            return [int(amount), 0]
        case 'up':
            return [0, -int(amount)]
        case 'down':
            return [0, int(amount)]
    
# todo types & docs
def add_elementwise(a,b):
    return list(map(lambda x,y: x+y, a,b))

coords_x_y = [0,0]
for str in get_input():
    coords_x_y = add_elementwise(coords_x_y, parse_coord_delta(str))
    
result = coords_x_y[0] * coords_x_y[1]
print('What do you get if you multiply your final horizontal position by your final depth?')
print(result)
# Result: 1694130
