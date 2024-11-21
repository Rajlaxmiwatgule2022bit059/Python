def sum(a, b, c):
    return a + b + c

def board(xstate, zstate):
    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
    two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
    three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
    four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
    five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
    six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
    eight = 'X' if xstate[8] else ('O' if zstate[8] else 8)
    
    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")

def check_win(xstate, zstate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print("X wins the match!")
            return 1
        if sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3:
            print("O wins the match!")
            return 0
	
    return -1

xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1

while True:
    board(xstate, zstate)
    
    if turn == 1:
        print("X's turn")
        value = int(input("Please enter a value between 0 and 8: "))
        if xstate[value] == 0 and zstate[value] == 0:
            xstate[value] = 1
        else:
            print("Invalid move. Try again.")
            continue
    else:
        print("O's turn")
        value = int(input("Please enter a value between 0 and 8: "))
        if xstate[value] == 0 and zstate[value] == 0:
            zstate[value] = 1
        else:
            print("Invalid move. Try again.")
            continue

    cwin = check_win(xstate, zstate)
    if cwin != -1:
        board(xstate, zstate)
        break
    
    turn = 1 - turn

