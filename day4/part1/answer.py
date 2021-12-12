from functools import reduce
from pathlib import Path

def get_input(type=str, strip_newlines=True):
    input = Path(__file__).with_name('input.txt')
    for line in input.open('r').readlines():
        if strip_newlines:
            line = line.strip('\n')
        yield line
        
def explode(str, delimiter=',', type=str):
    return list(map(type, str.split(delimiter)))

def parse_callnums_and_carddata():
    input = list(get_input())
    callnums = explode(input[0], type=int)
    # Parse bingo cards:
    idx = 1
    curr_card = []
    cards = [curr_card]
    while idx < len(input):
        row_str = input[idx].strip()
        if row_str == '':
            # Begin parsing new card:
            curr_card = []
            cards.append(curr_card)
        else:
            curr_card.append(explode(input[idx], None, int))
        idx += 1    
    return callnums, cards
    
class BingoCard:
    def __init__(self, card_rows):
        self.rows = card_rows.copy()
        # Transpose 2D array:
        self.cols = [list(cols) for cols in zip(*card_rows)]
            
    def mark_num(self, num):
        # Get item in 2D list if val is contained within item:
        matched_row_set = [r for r in self.rows if num in r]
        matched_col_set = [c for c in self.cols if num in c]
        # Number not on this card:
        if not matched_row_set or not matched_col_set:
            return False
        row = matched_row_set[0]
        col = matched_col_set[0]
        row.remove(num)
        col.remove(num)
        # if len(row) < 3 or len(col) < 3:
        #     exit('YEEEEEEEE')
        # Bingo- if either are empty:
        return not row or not col
    
    def sum_remaining_nums(self):
        # Sum numbers in 2d list:
        return sum(map(sum, self.rows)) 

def get_winning_card(callnums, cards):
    """
    Return winning bingo card & optionally last called number.
    """
    for num in callnums:
        for c in cards:
            if c.mark_num(num): # Has Bingo.
                return c, num
    return None, None

callnums, carddata = parse_callnums_and_carddata()

winner, num = get_winning_card(callnums, list(map(BingoCard, carddata)))
print('Result: Sum of remaining numbers on board * Last called number:')
print(winner.sum_remaining_nums() * num)
# Output: 58374