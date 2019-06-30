import re
strings='..XOOOX..'
win_x= [
            r'X..X..X..',
            r'.X..X..X.',
            r'..X..X..X',
            r'XXX......',
            r'...XXX...',
            r'......XXX',
            r'X...X...X',
            r'..X.X.X..',
        ]

win_o= [
            r'O..O..O..',
            r'.O..O..O.',
            r'..O..O..O',
            r'OOO......',
            r'...OOO...',
            r'......OOO',
            r'O...O...O',
            r'..O.O.O..',
        ]

for item in win_x:
    if re.search(item,strings):
        print("X win!!!")

for item1 in win_o:
    if re.search(item1,strings):
        print("O win!!!")





