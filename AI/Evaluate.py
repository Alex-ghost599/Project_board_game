#Liangyz
#2022/5/3  3:53

import main
import random
import numpy as np

# evaluation = [
#     [120,2,20,10,10,20,2,120],
#     [2,1,3,3,3,3,1,2],
#     [20,3,15,5,5,15,3,20],
#     [10,3,5,5,5,5,3,10],
#     [10,3,5,5,5,5,3,10],
#     [20,3,15,5,5,15,3,20],
#     [2,1,3,3,3,3,1,2],
#     [120,2,20,10,10,20,2,120]
# ]
evaluation=[
        [5,1,3,3,3,3,1,5],
        [1,1,2,2,2,2,1,1],
        [3,2,3,4,4,3,2,3],
        [3,2,4,5,5,4,2,3],
        [3,2,4,5,5,4,2,3],
        [3,2,3,4,4,3,2,3],
        [1,1,2,2,2,2,1,2],
        [5,1,3,3,3,3,1,5],
    ]
# evaluation=[
#         [5,1,3,3,3,3,1,5],
#         [1,1,2,2,2,2,1,1],
#         [3,2,4,4,4,4,2,3],
#         [3,2,4,6,6,4,2,3],
#         [3,2,4,6,6,4,2,3],
#         [3,2,4,4,4,4,2,3],
#         [1,1,2,2,2,2,1,2],
#         [5,1,3,3,3,3,1,5],
#     ]
evaluation=np.array(evaluation)


def move_eva(board,player,info,eva=evaluation):
    possible_moves = main.get_possible_moves(board,player,info)
    random.shuffle(possible_moves)
    result0 = 0
    move = [None,None]
    if len(possible_moves) != 0:
        for [x0,y0] in possible_moves:
            x = x0 - 1
            y = y0 - 1
            result0 = max(result0,eva[x][y])
            if result0 == eva[x][y]:
                move = [x0,y0]
            else:
                move = move
        return move
    else:
        return None,None



