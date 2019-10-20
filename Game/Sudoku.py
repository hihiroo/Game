#스도쿠
#프로그래밍 기초 수업 과제

import random


def create_board():
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)
    ans=[]
    ans += [seed]
    ans += [[seed[3]]+[seed[4]]+[seed[5]]+[seed[0]]+[seed[1]]+[seed[2]]]
    ans += [[seed[2]]+[seed[0]]+[seed[1]]+[seed[5]]+[seed[3]]+[seed[4]]]
    ans += [[seed[5]]+[seed[3]]+[seed[4]]+[seed[2]]+[seed[0]]+[seed[1]]]
    ans += [[seed[1]]+[seed[2]]+[seed[0]]+[seed[4]]+[seed[5]]+[seed[3]]]
    ans += [[seed[4]]+[seed[5]]+[seed[3]]+[seed[1]]+[seed[2]]+[seed[0]]]
    return ans

def copy_board(board):
    board_clone = []
    for row in board :
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone


def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")

    if level == '하':
        return 6
    elif level == '중':
        return 8
    elif level =='상':
        return 10



def make_holes(board,no_of_holes):
    holeset = []
    for x in range(no_of_holes):
        i = random.randrange(0,6)
        j = random.randrange(0,6)
        while board[i][j] == 0:
            i = random.randrange(0,6)
            j = random.randrange(0,6)
        board[i][j] = 0;
        holeset.append((i,j))
    return (board, holeset)



def show_board(board):
    print()
    print('S','|','1','2','3','4','5','6')
    print('-','+','-','-','-','-','-','-')
    i = 1
    for row in board:
        print(str(i)+' |',end=' ')
        i += 1
        for x in row:
            if x == 0:
                print('.',end=' ')
            else:
                print(x,end=' ')
        print()



def get_integer(message,i,j):
    number = input(message)
    while (not (number.isdigit()) or int(number) < i or int(number) > j): # 괄호 안에 조건식을 채운다.
        number = input(message)
    return int(number)



def main():
    solution = create_board()
    holes = get_level()
    puzzle = copy_board(solution)
    (puzzle, hole_set) = make_holes(puzzle, holes)
    show_board(puzzle)

    while holes:
        j = get_integer("가로줄 번호(1~6):",1,6) - 1
        i = get_integer("세로줄 번호(1~6):",1,6) - 1
        if (i,j) not in hole_set:
            print("빈칸이 아닙니다.")
            continue

        n = get_integer("숫자(1~6):",1,6)
        ans = solution[i][j]
        if ans == n:
            puzzle[i][j] = ans
            show_board(puzzle)
            hole_set.remove((i,j))
            holes -=1

        else:
            print(n,"가 아닙니다. 다시 해보세요.")
    print("잘 하셨습니다. 또 들려주세요.")

main()

