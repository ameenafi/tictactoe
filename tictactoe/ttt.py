import random
import time
import os
board=[[' ',' ',' '],[' ',' ',' ',],[' ',' ','  ']]
print('ALL THE BEST LETS START THE GAME')
print('COMPUTER STARTS THE GAME')
print('COMPUTER CHOOSES X')

while(1):
    while(2):
        rowchoice=[0,1,2]
        columnchoice=[0,1,2]
        row=random.choice(rowchoice)
        column=random.choice(columnchoice)
        if ((board[row][column]=='X') or (board[row][column]=='O')):
            print()
        else:    
            board[row][column]='X'
            break
    time.sleep(2)
    os.system('cls')
    print('\t\t|\t\t|')
    print('\t'+board[0][0]+'\t|\t'+board[0][1]+'\t|\t'+board[0][2]+'')
    print('\t---------------------------------')
    print('\t\t|\t\t|')
    print('\t'+board[1][0]+'\t|\t'+board[1][1]+'\t|\t'+board[1][2]+'')
    print('\t---------------------------------')
    print('\t\t|\t\t|')
    print('\t'+board[2][0]+'\t|\t'+board[2][1]+'\t|\t'+board[2][2]+'')

    if((board[0][0]=='X' and  board[0][1]=='X' and  board[0][2]=='X') or
       (board[0][0]=='X' and  board[1][0]=='X' and  board[2][0]=='X') or
       (board[0][0]=='X' and  board[1][1]=='X' and  board[2][2]=='X') or
       (board[0][1]=='X' and  board[1][1]=='X' and  board[2][1]=='X') or
       (board[0][2]=='X' and  board[1][2]=='X' and  board[2][2]=='X') or
       (board[0][2]=='X' and  board[1][1]=='X' and  board[2][0]=='X') or
       (board[1][0]=='X' and  board[1][1]=='X' and  board[1][2]=='X') or 
       (board[2][0]=='X' and  board[2][1]=='X' and board[2][2]=='X') ):
         print('COMPUTER WINS')
         break
    if(((board[0][0]!=' ' and board[0][1]!=' ' and board[0][2]!=' ' and
         board[1][0]!=' ' and board[1][1]!=' ' and board[1][2]!=' ' and
         board[2][0]!=' ' and board[2][1]!=' ' and board[2][2]!=' '))):
        print('ITS A TIE')
        break
    while(3):
        print('ITS YOUR TURN')
        row=int(input('enter the value of the row:'))
        column=int(input('enter the value of the column:'))
        if ((board[row][column]=='X') or (board[row][column]=='O')):
            print('try again')
        else:    
            board[row][column]='O'
            break
    os.system('cls')    
    print('\t\t|\t\t|')
    print('\t'+board[0][0]+'\t|\t'+board[0][1]+'\t|\t'+board[0][2]+'')
    print('\t---------------------------------')
    print('\t\t|\t\t|')
    print('\t'+board[1][0]+'\t|\t'+board[1][1]+'\t|\t'+board[1][2]+'')
    print('\t---------------------------------')
    print('\t\t|\t\t|')
    print('\t'+board[2][0]+'\t|\t'+board[2][1]+'\t|\t'+board[2][2]+'')
    if((board[0][0]=='O' and  board[0][1]=='O' and board[0][2]=='O') or
       (board[0][0]=='O' and  board[1][0]=='O' and board[2][0]=='O') or
       (board[0][0]=='O' and  board[1][1]=='O' and  board[2][2]=='O') or
       (board[0][1]=='O' and  board[1][1]=='O' and  board[2][1]=='O') or
       (board[0][2]=='O' and  board[1][2]=='O' and  board[2][2]=='O') or
       (board[0][2]=='O' and  board[1][1]=='O' and board[2][0]=='O') or
       (board[1][0]=='O' and  board[1][1]=='O' and board[1][2]=='O') or 
       (board[2][0]=='O' and  board[2][1]=='O' and  board[2][2]=='O') ):
         print('CONGRATULATIONS YOU WIN')
         break
    if(((board[0][0]!=' ' and board[0][1]!=' ' and board[0][2]!=' ' and
         board[1][0]!=' ' and board[1][1]!=' ' and board[1][2]!=' ' and
         board[2][0]!=' ' and board[2][1]!=' ' and board[2][2]!=' '))):
        print('ITS A TIE')
        break
time.sleep(4)
