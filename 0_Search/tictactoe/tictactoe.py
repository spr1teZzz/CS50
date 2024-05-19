"""
Tic Tac Toe Player
"""

import math
import copy
import functools
#表示棋盘的可能移动
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    返回下一次的player
    """
    #遍历board 对每一个单元格进行统计,比较 “X” 和 “O”的数量（X先移动
    count_X = 0
    count_O = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == X:
                count_X+=1
            if board[i][j] == O:
                count_O+=1
    
    #比较数量
    if count_X > count_O:
        #player 为O
        return O
    else:
        return X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    返回棋盘所有可能的action
    """
    #当输入的棋盘状态为 结束状态
    if terminal(board) is True:
        return None
    set_actions = set()

    #添加棋盘的所有可能action 到 set_actions中
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                set_actions.add((i,j))
    # print(set_actions)
    return set_actions

    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    返回执行move(i,j)后的board
    """
    if terminal(board) == True:
        return board
    
    #move(i,j)操作异常
    i = action[0]
    j = action[1]
    if i<0 or i >2 or j<0 or j>2 or board[i][j] != EMPTY:
        raise NameError('result action')
    #进行深拷贝
    new_board = copy.deepcopy(board)
    #判断player
    p = player(board)
    #move(i,j)并返回
    new_board[i][j] = p
    return new_board


def win_judge(a,b,c):
    """
    根据a,b,c是否相等来判断该行、列、斜对角是否形成连线(True/False)
    """ 
    if a == EMPTY:
        return False
    if a == b:
        if a == c:
            return True    
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    如果有赢家,则返回赢家
    """
    #横、纵、斜 三者相连则为赢家 八种情形
    if win_judge(board[0][0],board[0][1],board[0][2]):
        return board[0][0]
    if win_judge(board[1][0],board[1][1],board[1][2]):
        return board[1][0]
    if win_judge(board[2][0],board[2][1],board[2][2]):
        return board[2][0]
    if win_judge(board[0][0],board[1][0],board[2][0]):
        return board[0][0]
    if win_judge(board[0][1],board[1][1],board[2][1]):
        return board[0][1]
    if win_judge(board[0][2],board[1][2],board[2][2]):
        return board[0][2]
    if win_judge(board[0][0],board[1][1],board[2][2]):
        return board[0][0]
    if win_judge(board[0][2],board[1][1],board[2][0]):
        return board[0][2]   
    
    # 没有赢家
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #1.有人赢游戏 2.单元格被填满且没有赢家 True

    win = winner(board)
    if win is not None:
        #有赢家则直接返回True
        return True
    
    #没有赢家，则需要判断board 是否单元格已满
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                #单元格未满 返回False
                return False
    
    #单元格已满 返回True
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    返回当前的效用 X赢:1 | 平局:0 | O赢:-1 
    """
    win = winner(board)
    p = player(board)
    print("win:%s,p:%s"%(win,p))
    # if  p == win :
    #     return 1
    # elif p == None:
    #     return 0
    # else : 
    #     return -1
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def optimize(board,step,score):
    if terminal(board) == True:
        return 
    #获取当前board 可执行的action
    actions_set = actions(board)
    step += 1 #step 增加
    for ac in actions_set:
        #执行ac操作
        b = result(board,ac)
        if terminal(b)  == True:
            #若执行完之后 结束
            score.append((utility(b),step,ac))
        else:
            #执行完后 未结束
            optimize(b,step,score)

# 获取列表的第一个元素
def comp(a,b):
    if a[0] == b[0]:
        if a[1] == b[1]:
            return 0
        elif a[1] > b[1]:
            return 1
        else:
            return -1
    elif a[0]>b[0]:
        return -1
    else:
        return 1   

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    返回当前玩家的最优 action
    """
    if terminal(board) == True:
        #若当前棋盘状态为结束则返回None
        return None
    step = 0 #表示游戏结束的步数
    score = []
    optimize(board,step,score)
    score.sort(key= functools.cmp_to_key(comp))
    # print(score)
    return score[0][2]
