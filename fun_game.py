# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Samuel Ramos
#               Angel Lopez
#               Cindy Villasana
#               Ezekiel Rivera
# Section:      ENGR 102 M01
# Assignment:   Lab 13 team
# Date:         11/22/22
print("\nWelcome to Connect 4\nPlayer 1's token is the number 1\nPlayer 2's token is the number 2\n")
import numpy as np
grid = np.full((6, 7), 0)
print(grid, end='\n\n')
col_want = 0

def add_chip(col_want, turn):
    """Adds chips to the board (1 for p1 and 2 for p2)"""
    for i in range(5, -1, -1):
        if grid[i, col_want] == 0:
            if turn:
                grid[i, col_want] = 1
            else:
                grid[i, col_want] = 2
            break
    else:
        print('***COLUMN FULL, PLEASE SELECT ANOTHER COLUMN AND TRY AGAIN***')
        next(alt)

def main():
    """Running this runs the whole program"""
    n = True
    while n:
        turn = next(alt)
        if turn:
            add_chip(p1(), turn)
            print()
            print(grid, end='\n\n')
            if check_win(1):
                print(f'\nPlayer 1 wins!\n\n')
                draw_win()
                n = False
        else:
            add_chip(p2(), turn)
            print()
            print(grid, end='\n\n')
            if check_win(2):
                print(f'\nPlayer 2 wins!\n\n')
                draw_win()
                n = False

def p1():
        """player 1 input"""
        print("Type 'End' to end game")
        while True:
            inp = input('P1 Please enter a column number 1 - 7: ')
            try:
                inp = int(inp) - 1
                if 0 <= inp <= 6:
                    break
            except:
                if inp == 'END':
                    print(f'\n\nThanks for Playing\n\n')
                    exit()
                pass
        return inp

def p2():
        """player 2 input"""
        print("Type 'End' to end game")
        while True:
            inp = input('P2 Please enter a column number 1 - 7: ')
            try:
                inp = int(inp) - 1
                if 0 <= inp <= 6:
                    break
            except:
                if inp == 'END':
                    print(f'\n\nThanks for Playing\n\n')
                    exit()
                pass
        return inp

def alter():
    while True:
        yield True
        yield False

alt = alter()

def check_win(n):
    # for vertical
    for i in range(-1, -4, -1):
        for j in range(7):
            if win_vert(i, j, n):
                return True
    # for horizontal
    for i in range(-1, -7, -1):
        for j in range(4):
            if win_hori(i, j, n):
                return True
    # for diagonally right
    for i in range(-1, -4, -1):
        for j in range(4):
            if win_diag_right(i, j, n):
                return True
    # for diagonally left
    for i in range(-1, -4, -1):
        for j in range(-1, -5, -1):
            if win_diag_left(i, j, n):
                return True

def win_vert(y, x, n):
    return grid[y, x] == grid[y - 1, x] == grid[y - 2, x] == grid[y - 3, x] == n

def win_hori(y, x, n):
    return grid[y, x] == grid[y, x + 1] == grid[y, x + 2] == grid[y, x + 3] == n

def win_diag_right(y, x, n):
    return grid[y, x] == grid[y - 1, x + 1] == grid[y - 2, x + 2] == grid[y - 3, x + 3] == n

def win_diag_left(y, x, n):
    return grid[y, x] == grid[y - 1, x - 1] == grid[y - 2, x - 2] == grid[y - 3, x - 3] == n

def draw_win():
    import turtle as t
    n = 25
    w = 18.5 * n
    l = 25 * n
    board = t.Turtle()
    t.speed(0)
    t.color('blue')
    t.pensize(20)
    t.penup()
    t.goto(-(12.5 * n), (9.25 * n))
    t.pendown()
    # Square
    t.forward(l)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(w)
    # square
    for i in range(3):
        t.right(90)
        t.forward((25 * n) / 7)
        t.right(90)
        t.forward(18.5 * n)
        t.penup()
        t.left(90)
        t.forward((25 * n) / 7)
        t.left(90)
        t.pendown()
        t.forward(18.5 * n)
    t.right(90)
    t.forward((25 * n) / 7)
    t.right(90)
    for i in range(3):
        t.forward((18.5 * n) / 6)
        t.right(90)
        t.forward(25 * n)
        t.left(90)
        t.forward((18.5 * n) / 6)
        t.left(90)
        t.forward(25 * n)
        t.right(90)
    t.penup()
    t.right(180)
    t.forward(w / 6)
    t.left(90)
    t.forward(l / 14)
    t.pendown()
    for i in range(5):
        for j in range(6):
            t.circle(w / 12)
            t.forward(l / 7)
            t.circle(w / 12)
        t.penup()
        t.right(90)
        t.forward(w / 6)
        t.right(270)
        t.pendown()
        for i in range(6):
            t.circle(w / 12)
            t.back(l / 7)
            t.circle(w / 12)
    t.penup()
    x, y = l/7, w/6
    for i in range(6):
        for j in range(7):
            t.goto(-l/7*3 + x*j,-w/12*5 + y*i)
            if grid[5-i,j] == 1:
                t.color('yellow')
                t.dot(w/8)
                t.penup()
            elif grid[5-i,j] == 2:
                t.color('red')
                t.dot(w/8)
                t.penup()
    return t.done()
if __name__ == main():
    main()