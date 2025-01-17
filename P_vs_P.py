#Liangyz
#2022/5/2  18:25

import pygame
import main
import time
import menu
# make move by mouse
def pvsp():
    # background
    main.surface.blit(main.gameboard,(375,50))

    #set new board and put pawn on board
    board = main.restnewboard()
    info = []
    for x in range(1,9):
        for y in range(1,9):
            if [x,y] not in [[4,4],[4,5],[5,4],[5,5]]:
                info.append([x,y])


    flag_d = False
    flag_u = False
    flag_gameover = [1,1]

    gameover = False
    gameover_show = True
    turn = 'black'

    running = True
    while running:
        for event in pygame.event.get():
            # quit
            if event.type==pygame.QUIT:
                main.exit_game()
            # retry
            if event.type==pygame.MOUSEBUTTONDOWN and \
                    event.pos[0] in range(1095,1172) and\
                        event.pos[1] in range(50,125):
                return pvsp()
            # return to main_menu
            if event.type==pygame.MOUSEBUTTONDOWN and \
                    event.pos[0] in range(1095,1176) and\
                        event.pos[1] in range(770,851):
                main.number_of_win_black=0
                main.number_of_win_white=0
                main.Draw=0
                # menu.main_menu()
                return

            # make move--------------------------------------------------------------------------------
            gameover = main.gameover(board,info)

            if not gameover:
                #show whose turn
                if turn == 'black':
                    main.surface.blit(main.gamepawn_black,(385,60))
                elif turn == 'white':
                    main.surface.blit(main.gamepawn_white,(385,60))

                #for black
                if turn == 'black' and \
                        event.type == pygame.MOUSEBUTTONDOWN and \
                        event.button == 1 and \
                        not gameover:
                    pos = event.pos
                    for [x,y] in info:
                        if pos[0] in range(375+y*80, 375+y*80+80) and \
                                pos[1] in range(50+x*80, 50+x*80+80):
                            if main.legal_move(board,'black',x,y):
                                board[x][y] = 1
                                info.remove([x,y])
                                for i, j in main.flip_pawn(board,'black',x,y):
                                    board[i][j] = 1
                                turn = 'white'
                                break
                #for white
                elif turn == 'white' and \
                        event.type == pygame.MOUSEBUTTONDOWN and \
                        event.button == 1 and \
                        not gameover:
                    pos = event.pos
                    for [x,y] in info:
                        if pos[0] in range(375+y*80, 375+y*80+80) and \
                                pos[1] in range(50+x*80, 50+x*80+80):
                            if main.legal_move(board,'white',x,y):
                                board[x][y] = 2
                                info.remove([x,y])
                                for i, j in main.flip_pawn(board,'white',x,y):
                                    board[i][j] = 2
                                turn = 'black'
                                break

                #check is there any legal move for both player
                if turn == 'black':
                    if not main.check_is_any_legal_move(board,info,'black'):
                        turn = 'white'
                elif turn == 'white':
                    if not main.check_is_any_legal_move(board,info,'white'):
                        turn = 'black'


            else:
                if gameover_show:
                    main.show_score(main.socreboard,board)
                    black,white=main.score(board)
                    if black>white:
                        main.number_of_win_black+=1
                    elif black<white:
                        main.number_of_win_white+=1
                    elif black==white:
                        main.Draw+=1

                    main.Scoreboard(main.number_of_win_black,
                                    main.number_of_win_white,
                                    main.Draw)
                    gameover_show = False

        if not gameover:
            # update board
            for x in range(1,9):
                for y in range(1,9):
                    if board[x][y]==1:
                        main.surface.blit(main.gamepawn_black,
                                          (y*main.cell_size[0]+main.space_size[0]+375,
                                           x*main.cell_size[1]+main.space_size[1]+50))
                    elif board[x][y]==2:
                        main.surface.blit(main.gamepawn_white,
                                          (y*main.cell_size[0]+main.space_size[0]+375,
                                           x*main.cell_size[1]+main.space_size[1]+50))

        pygame.display.update()
        main.Runingclock.tick(main.fps)
