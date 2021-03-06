CURRENT = [[" \t"," \t", " \t\n"],[" \t"," \t", " \t\n"],[" \t"," \t", " \t\n"]]
EMPYTY_POSITION = [(i, j) for i in range(1,4) for j in range(1, 4)]


def draw_symbol(position, user):
    x, y = position
    if user == 1:
        CURRENT[x-1][y-1]=CURRENT[x-1][y-1].replace(" ", "⭕")
    else:
        CURRENT[x-1][y-1]=CURRENT[x-1][y-1].replace(" ", "❌")

def draw_board():
    for i,x_item in enumerate(CURRENT):
        for y_item in x_item:
            print(y_item, end="")
            if y_item[-1] == "\t":
                print("|\t", end="")
        if i<2:
            print("-\t-\t-\t-\t-\t\n", end="")

def check_input():
    [x, y] = [i for i in (input("Please input the position you want to please(x,y):").split(","))]

    # tell the number type
    if x.isdigit() and y.isdigit():
        x, y = [int(x), int(y)]
    else:
        print("please input number(x ~ [1, 2, 3] y ~ [1, 2, 3]")
        return False

    if x > 0 and x < 3 and y > 0 and y < 3:
        return (x, y)
    else: 
        print("please input the correct value(x ~ [1, 2, 3] y ~ [1, 2, 3]")
        return False

def tell_win():
    pass

def manipulate(position, user):
    # input ture and has empty position 
    if position and position in EMPYTY_POSITION:
        draw_symbol(position, user)
        draw_board()
        EMPYTY_POSITION.remove(position)
        return True
        # tell the win condition
        #tell_win()

    # no empty postion
    elif position:
        print("The expected position has placed! Please choose another position!")
        return False

    # input error
    else:
        return False

def main():
    # Print the current board
    draw_board()

    for i in range(0,9):
        print("User 1 round: ")
        position  = check_input()

        if not manipulate(position, 1):
            continue

        print("User 2 round: ")
        position  = check_input()

        if not manipulate(position, 2):
            continue
main()

#question:
#1. 2如果输到已经有的位置，会直接跳过2 让 1 输入；
#2. 胜负逻辑没写



