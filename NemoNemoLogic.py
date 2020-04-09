# 네모네모 로직
# 프로그래밍 기초 수업 팀플


import random
class Input_Err(Exception): pass
class Char_Err(Exception): pass


def close_game():
    while True:
        try:
            play = input("게임을 종료하시겠습니까?(y/n) : ")
            if play != 'y' and play != 'n':
                raise Input_Err
        except Input_Err:
            print("'y'와 'n'중에 선택해주세요.")
        except:
            pass
        else:
            if play == 'y':
                return True
            else:
                return False


def select_Mode():
    while True:
        try:
            x = input("난이도를 선택해주세요(상,중,하) : ")
            if not(x == '상' or x == '중' or x == '하'):
                raise Input_Err
        except Input_Err:
            print("'상', '중', '하' 중에 하나를 골라주세요.")
        except:
           if close_game() == True:
               return -1
        else:
            if x == '상':
                return 1
            elif x == '중':
                return 2
            else:
                return 3

def make_ans_board(mode):
    picture = []

    if mode == 3:
        len_line = 3
        flower = [[' ','*','*','*',' '],['*','*',' ','*','*'],['*',' ','*',' ','*'],
               ['*','*',' ','*','*'],[' ','*','*','*',' ']]
        picture.append(flower)

        heart=[[' ','*',' ','*',' '],['*','*','*','*','*'],['*','*','*','*','*'],
               [' ','*','*','*',' '],[' ',' ','*',' ',' ']]

        picture.append(heart)

    elif mode == 2:
        len_line = 4
        smile = [[' ']*10 for x in range(10)]
        for x in range(1,9):
            smile[0][x] = '*'
            smile[9][x] = '*'
        smile[1][0],smile[1][1],smile[1][8],smile[1][9]='*','*','*','*'
        smile[8] = smile[1]
        for x in range(2,5):
            smile[x]=['*',' ','*','*',' ',' ','*','*',' ','*']
        smile[5][0],smile[5][9] = '*','*'
        smile[6][0],smile[6][9] ='*','*'
        smile[7] = smile[6]
        for x in range(2,8):
            smile[6][x] = '*'

        picture.append(smile)

        dog = [['*','*','*',' ',' ',' ',' ','*','*','*'],['*',' ','*','*','*','*','*','*',' ','*'],[' ',' ','*','*','*','*','*','*',' ',' '],[' ',' ','*',' ','*','*',' ','*',' ',' '],[' ',' ','*','*','*','*','*','*',' ',' '],[' ',' ','*','*',' ','*','*','*',' ',' '],[' ',' ','*','*','*','*','*','*','*',' '],
               [' ',' ',' ','*','*','*','*',' ','*','*'],[' ',' ',' ',' ','*',' ',' ','*','*','*'],[' ',' ',' ',' ','*','*','*','*','*','*']]

        picture.append(dog)

    else:
        len_line = 5
        cow = [[' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
        [' ',' ',' ','*','*',' ',' ',' ',' ',' ','*','*',' ',' ',' '],
        [' ',' ',' ','*','*','*','*','*','*','*','*','*',' ',' ',' '],
        [' ','*','*','*',' ',' ',' ',' ',' ','*','*','*','*','*','*'],
        ['*',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*'],
        ['*','*','*',' ',' ',' ',' ',' ','*','*','*','*','*','*','*'],
        [' ',' ','*',' ',' ','*',' ','*','*',' ','*','*','*',' ',' '],
        [' ',' ','*','*',' ',' ',' ','*','*','*','*','*','*',' ',' '],
        [' ',' ','*','*','*',' ',' ',' ','*','*','*','*','*',' ',' '],
        [' ',' ','*','*','*','*',' ',' ',' ',' ',' ','*','*',' ',' '],
        [' ',' ','*','*','*',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
        [' ',' ','*','*','*','*','*','*','*','*','*','*',' ',' ',' '],
        [' ',' ',' ','*','*',' ','*','*','*',' ','*','*',' ',' ',' '],
        [' ',' ',' ',' ','*','*','*','*','*','*','*',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ','*','*','*','*','*',' ',' ',' ',' ',' '],
        ]
        picture.append(cow)

        penguin=[[' ',' ',' ',' ',' ',' ','*','*','*','*','*',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ','*','*','*','*','*','*','*',' ',' ',' '],
                [' ',' ',' ',' ',' ','*','*','*',' ','*',' ','*',' ',' ',' '],
                [' ',' ',' ',' ','*','*','*','*','*','*','*','*',' ','*',' '],
                [' ',' ',' ','*','*','*','*',' ',' ',' ',' ','*','*','*',' '],
                [' ',' ',' ','*','*','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
                [' ',' ','*','*','*','*',' ',' ',' ',' ',' ','*','*',' ',' '],
                [' ','*','*','*','*',' ',' ',' ',' ',' ',' ',' ','*','*',' '],
                ['*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ','*','*','*'],
                ['*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ','*','*','*'],
                ['*',' ','*','*',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' '],
                [' ',' ','*','*',' ',' ',' ',' ',' ','*',' ',' ','*',' ',' '],
                [' ',' ','*','*','*','*','*','*','*',' ','*','*','*','*',' '],
                ['*','*','*',' ',' ',' ','*','*','*','*',' ','*','*','*',' ']]
        picture.append(penguin)

    return (picture[random.randrange(0,len(picture))],len_line)

def make_ans_row(board,size):
    length = size + len(board)
    ans_row = ans_row = [[' ']*length for x in range(size)]
    for y in range(len(board)):
        cnt = 0
        lv = size-1
        for x in range(len(board)-1,-1,-1):
            if board[x][y] == '*':
                cnt += 1
            else:
                if cnt > 0:
                    ans_row[lv][size+y] = str(cnt)
                    lv -= 1
                    cnt = 0
        if cnt > 0:
            ans_row[lv][size+y] = str(cnt)
    return ans_row



def make_ans_col(board,size):
    ans_col = [[' ']*size for x in range(len(board))]
    for y in range(len(board)):
        cnt = 0
        lv = size-1
        for x in range(len(board)-1,-1,-1):
            if board[y][x] == '*':
                cnt += 1
            else:
                if cnt > 0:
                    ans_col[y][lv] = str(cnt)
                    lv -= 1
                    cnt = 0
        if cnt > 0:
            ans_col[y][lv] = str(cnt)
    return ans_col



def show_board(board,ans_row,ans_col):
    print()
    for x in range(len(ans_row)):
            line = len(ans_row[0]) - len(board)

            for y in range(len(ans_row[0])):
                if y >= line:
                    print('|',end='')
                elif y<line-1:
                    print(' ',end='')
                if ans_row[x][y] != ' ' and int(ans_row[x][y]) >= 10:
                    print(ans_row[x][y],end='')
                else:
                    print(ans_row[x][y],end=' ')
            print('|')

    print('-'*(3*len(ans_row[0])))

    for x in range(len(board)):
            for y in range(len(ans_col[0])-1):
                if ans_col[x][y] != ' ' and int(ans_col[x][y]) >= 10:
                    print(ans_col[x][y]+' ',end='')
                else:
                    print(ans_col[x][y]+' ',end=' ')
            if int(ans_col[x][len(ans_col[0])-1]) < 10:
                print(ans_col[x][len(ans_col[0])-1],end=' ')
            else:
                print(ans_col[x][len(ans_col[0])-1],end='')
            for y in range(len(board)):
                print('|'+board[x][y],end = ' ')
            print('|')
    print()



def game(mode):
    (ans,len_line) = make_ans_board(mode)
    ans_row = make_ans_row(ans,len_line)
    ans_col = make_ans_col(ans,len_line)

    size = len(ans)

    coordi_ans = []
    cnt = 0
    for x in range(len(ans)):
        for y in range(len(ans[0])):
            if ans[x][y] == '*':
                coordi_ans.append((x,y))
                cnt += 1

    board = [[' ']* size for x in range(size)]
    show_board(board,ans_row,ans_col)

    while cnt > 0:

        while True:
            try :
                i = int(input("행을 입력해주세요(1~"+str(size)+") : "))
                if i < 1 or i > size:
                        raise Input_Err
                j = int(input("열을 입력해주세요(1~"+str(size)+") : "))
                if j < 1 or j > size:
                        raise Input_Err
                c = input("정답이면 '*', 아니라면 'X'를 입력하세요 : ")
                if c != '*' and c != 'X':
                    raise Char_Err

            except ValueError:
                    print("정수를 입력해주세요.")
            except Input_Err:
                    print("범위를 벗어났습니다.")
            except Char_Err:
                    print("'*'과 'X'중에 선택하세요.")
            except:
                if close_game() == 1:
                    return -1
            else:
                i -= 1
                j -= 1

                if c == 'X':
                        if board[i][j] == ' ':
                             board[i][j] = 'X'
                        else:
                            board[i][j] = ' '
                        Show_board(board,ans_row,ans_col)

                elif (i,j) in coordi_ans:
                        if board[i][j] == '*':
                            print("이미 선택되어 있습니다.")
                        else:
                            cnt -= 1
                            board[i][j] = '*'
                            Show_board(board,ans_row,ans_col)
                            break
                else:
                    print("다시 생각해보세요...")

    print()
    for x in range(len(ans)):
        for y in range(len(ans[0])):
            print(ans[x][y],end=' ')
        print()
    print("그림이 완성되었습니다.")
    print("축하합니다!\n")


def main():
    print("환영합니다!")
    play = True

    while play:
        mode = select_Mode()

        if mode == -1:
            print("안녕히 가세요!")
            break

        else:
            play = game(mode)

        if play == -1:
            return 0

        if close_game() == True:
                print("안녕히 가세요!")
                return 0


main()


