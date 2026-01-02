import pygame
import sys
from pygame.locals import *
import asyncio

async def main():
    pygame.init()

    #desktop sizes
    desktops_sizes=pygame.display.get_desktop_sizes()
    desktop1_sizes=list(desktops_sizes[0])
    desktop1_sizes[0]*=0.75
    desktop1_sizes[1]*=0.75
    desktop1_width=desktop1_sizes[0]
    desktop1_height=desktop1_sizes[1]
    desktop1_center_x=desktop1_width//2
    desktop1_center_y=desktop1_height//2

    #colours
    light_grey=(128,128,128) #grey
    red=(220,20,60) #crimson
    green=(50,205,50) #lime green
    blue=(30,144,255) #dodger blue
    black=(0,0,0) #black
    white=(255,255,255) #white
    dark_grey=(105,105,105) #dimgrey
    gold=(207,181,59) #old gold


    #window stuff
    window=pygame.display.set_mode(desktop1_sizes,pygame.RESIZABLE)

    #music
    pygame.mixer.music.load("lofi-instrumental-409202.mp3")
    volume=0.5
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

    #clock
    clock=pygame.time.Clock()

    #tic tac toe text
    name_font=pygame.font.SysFont("freesanbold.ttf",200,bold=True)
    name_text=name_font.render("Tic tac toe",True,blue)
    name_text_x,name_text_y=name_font.size("Tic tac toe")

    #menu text
    menu_title_font=pygame.font.SysFont("freesanbold.ttf", 100)
    menu_title_text=menu_title_font.render("Main menu", True, red)
    menu_title_text_x,menu_title_text_y=menu_title_font.size("Main menu")

    #player draw text
    end_draw_font=pygame.font.SysFont("freesanbold.ttf",100)
    end_draw_text=end_draw_font.render("It's a draw!",True,gold)
    end_draw_text_x,end_draw_text_y=end_draw_font.size("It's a draw!")

    #player win text
    end_win_font=pygame.font.SysFont("freesanbold.ttf",100)
    def win_text(winner):
        end_win_text=end_win_font.render(f"Congratulations, player {winner} has won!",True,gold)
        end_win_text_x,end_win_text_y=end_win_font.size(f"Congratulations, player {winner} has won!")
        return end_win_text,end_win_text_x,end_win_text_y

    #settings text
    settings_font=pygame.font.SysFont("freesanbold",100)
    settings_text=settings_font.render("Settings",True,red)
    settings_text_x,settings_text_y=settings_font.size("Settings")

    #mute button
    mute_button_font=pygame.font.SysFont("freesanbold.ttf", 50)
    mute_button_text1=mute_button_font.render("Muted",True,black)
    mute_button_text2=mute_button_font.render("Unmuted",True,black)
    mute_button_text_x,mute_button_text_y=mute_button_font.size("Unmute")

    #play button
    play_button_font=pygame.font.SysFont("freesanbold.ttf", 66)
    play_button_text=play_button_font.render("Play", True, black)
    play_button_text_x,play_button_text_y=play_button_font.size("Play")

    #quit button
    quit_button_font=pygame.font.SysFont("freesanbold.ttf", 50)
    quit_button_text=quit_button_font.render("Quit", True, black)
    quit_button_text_x,quit_button_text_y=quit_button_font.size("Quit")

    #settings button
    settings_button_font=pygame.font.SysFont("freesanbold.ttf", 66)
    settings_button_text=settings_button_font.render("Settings",True,black)
    settings_button_text_x,settings_button_text_y=settings_button_font.size("Settings")

    #back to menu button
    menu_button_font=pygame.font.SysFont("freesanbold.ttf", 50)
    menu_button_text=menu_button_font.render("Menu", True, black)
    menu_button_text_x,menu_button_text_y=menu_button_font.size("Menu")

    #play again button
    again_button_font=pygame.font.SysFont("freesanbold.ttf", 50)
    again_button_text=again_button_font.render("Play again", True, black)
    again_button_text_x,again_button_text_y=again_button_font.size("Play again")

    #shapes
    #circle
    o_surface=pygame.Surface([160, 160], pygame.SRCALPHA)
    pygame.draw.circle(o_surface, blue, (80, 80), 50, 15)
    #cross
    x_surface=pygame.Surface([160, 160], pygame.SRCALPHA)
    offset=15
    start_pos1=(offset+25,offset+25)
    end_pos1=(110-offset+25,110-offset+25)
    pygame.draw.line(x_surface, red, start_pos1, end_pos1,25)
    start_pos2=(110-offset+25,offset+25)
    end_pos2=(offset+25,110-offset+25)
    pygame.draw.line(x_surface, red, start_pos2, end_pos2,25)


    if_menu=True
    if_game=False
    if_settings=False
    if_game_ending=False

    music_on=True

    def vertical(x):
        if board[0]==board[3]==board[6]==x:
            start=board_rects[0].midtop
            end=board_rects[6].midbottom
            pygame.draw.line(window,gold,start,end,10)
            return x
        if board[1]==board[4]==board[7]==x:
            start = board_rects[1].midtop
            end = board_rects[7].midbottom
            pygame.draw.line(window, gold, start, end, 10)
            return x
        if board[2]==board[5]==board[8]==x:
            start = board_rects[2].midtop
            end = board_rects[8].midbottom
            pygame.draw.line(window, gold, start, end, 10)
            return x
    def horizontal(x):
        if board[0]==board[1]==board[2]==x:
            start=board_rects[0].midleft
            end=board_rects[2].midright
            pygame.draw.line(window,gold,start,end,10)
            return x
        if board[3]==board[4]==board[5]==x:
            start=board_rects[3].midleft
            end=board_rects[5].midright
            pygame.draw.line(window, gold, start, end, 10)
            return x
        if board[6]==board[7]==board[8]==x:
            start=board_rects[6].midleft
            end=board_rects[8].midright
            pygame.draw.line(window, gold, start, end, 10)
            return x
    def diagonal(x):
        if board[0]==board[4]==board[8]==x:
            start=board_rects[0].topleft
            end=board_rects[8].bottomright
            pygame.draw.line(window,gold,start,end,10)
            return x
        if board[2]==board[4]==board[6]==x:
            start=board_rects[2].topright
            end=board_rects[6].bottomleft
            pygame.draw.line(window,gold,start,end,10)
            return x

    def if_win():
        if vertical(1) != None or horizontal(1) != None or diagonal(1) != None:
            return "1"
        elif vertical(2) != None or horizontal(2) != None or diagonal(2) != None:
            return "2"
        else:
            return "n"

    #window sizes
    window_size=pygame.display.get_window_size()
    window_width,window_height=window_size[0],window_size[1]
    window_center_x,window_center_y=window_width//2,window_height//2

    #mouse
    o_surface_cursor=pygame.transform.scale_by(o_surface,0.5)
    o_cursor=pygame.cursors.Cursor([40,40],o_surface_cursor)
    x_surface_cursor=pygame.transform.scale_by(x_surface,0.5)
    x_cursor=pygame.cursors.Cursor([40,40],x_surface_cursor)



    #back to menu button
    menu_rect_box=pygame.Rect(window_width * 0.85, 25, menu_button_text_x * 1.5, menu_button_text_y * 1.5)

    mute_rect_box=pygame.Rect(window_center_x-100,window_center_y*0.75,200,100)

    while True:
        if music_on:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

        mouse_pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #menu controls
                    if if_menu:
                        #quit button
                        if quit_rect_box.collidepoint(mouse_pos):
                            pygame.quit()
                            sys.exit()
                        #play button
                        if play_rect_box.collidepoint(mouse_pos):
                            if_menu=False
                            if_game=True
                            player = 0
                            board = [0] * 9
                        #settings
                        if settings_rect_box.collidepoint(mouse_pos):
                            if_menu=False
                            if_settings=True
                    #game controls
                    if if_game:
                        #back to main menu button
                        if menu_rect_box.collidepoint(mouse_pos):
                            if_game=False
                            if_menu=True
                        #board buttons
                        for n in range(9):
                            if board_rects[n].collidepoint(mouse_pos):
                                if board[n]==0:
                                    board[n]=player
                                    if_chosen=True
                                else:
                                    print("chose a different slot")
                    #game end controls
                    if if_game_ending:
                        #menu button
                        if menu_rect_box.collidepoint(mouse_pos):
                            if_game_ending=False
                            if_menu=True
                        #play again button
                        if again_rect_box.collidepoint(mouse_pos):
                            if_game_ending=False
                            if_game=True
                            player = 0
                            board = [0] * 9
                    #settings controls
                    if if_settings:
                        #menu button
                        if menu_rect_box.collidepoint(mouse_pos):
                            if_settings=False
                            if_menu=True
                        #mute button
                        if mute_rect_box.collidepoint(mouse_pos):
                            if music_on:
                                music_on=False
                            else:
                                music_on=True

        #window sizes
        window_size=pygame.display.get_window_size()
        window_width,window_height=window_size[0],window_size[1]
        window_center_x,window_center_y=window_width//2,window_height//2

        #game board
        #move board
        move_x,move_y=10,10
        #board squares
        board_rects=[]
        for rect_y in range(0,320,160-10):
            for rect_x in range(0,320,160-10):
                board_rect=pygame.Rect(window_center_x-240+rect_x+move_x,window_center_y-240+rect_y+move_y,160,160)
                board_rects.append(board_rect)

        # background
        window.fill(light_grey)
        # game name
        name_rect = pygame.Rect(window_center_x - name_text_x // 2, window_center_y * 0.1, name_text_x, name_text_y)
        window.blit(name_text, name_rect)

        #center of window
        #pygame.draw.circle(window,red,[window_center_x,window_center_y],5)


        #main menu screen
        if if_menu:
            pygame.mouse.set_cursor(0)
            # menu text
            menu_rect = pygame.Rect(window_center_x - menu_title_text_x // 2, window_center_y * 0.75, menu_title_text_x, menu_title_text_y)
            window.blit(menu_title_text, menu_rect)
            # quit button
            quit_rect_box = pygame.Rect(window_center_x - quit_button_text_x // 2, window_center_y * 1.5,quit_button_text_x * 1.5, quit_button_text_y * 1.5)
            pygame.draw.rect(window,red,quit_rect_box)
            quit_rect_text=quit_rect_box.move(12.5,5)
            window.blit(quit_button_text, quit_rect_text)
            #play button
            play_rect_box=pygame.Rect(window_center_x - play_button_text_x // 2 + 150, window_center_y * 1.15, play_button_text_x * 1.5, play_button_text_y * 1.5)
            pygame.draw.rect(window,green,play_rect_box)
            play_rect_text=play_rect_box.move(20,10)
            window.blit(play_button_text, play_rect_text)
            #settings button
            settings_rect_box=pygame.Rect(window_center_x-settings_button_text_x//2-150,window_center_y*1.15,settings_button_text_x*1.5,settings_button_text_y*1.5)
            pygame.draw.rect(window,dark_grey,settings_rect_box)
            settings_rect_text=settings_rect_box.move(45,10)
            window.blit(settings_button_text,settings_rect_text)

        #game screen
        if if_game:
            #back to menu button
            menu_rect_box=pygame.Rect(window_width * 0.85, 25, menu_button_text_x * 1.5, menu_button_text_y * 1.5)
            pygame.draw.rect(window,red,menu_rect_box)
            menu_rect_text=menu_rect_box.move(15,7.5)
            window.blit(menu_button_text, menu_rect_text)
            #game board
            for game_rect in board_rects:
                pygame.draw.rect(window,white,game_rect,10)
            for n in range(9):
                if board[n]==1:
                    # pygame.draw.circle(window,blue,board_rects[n].center,board_rects[n].width//2,20)
                    window.blit(o_surface,board_rects[n])
                if board[n]==2:
                    # pygame.draw.circle(window,red,board_rects[n].center, board_rects[n].width // 2, 20)
                    window.blit(x_surface,board_rects[n])
            #game logic
            if if_chosen:
                if player==1:
                    player=2
                    pygame.mouse.set_cursor(*x_cursor)
                else:
                    player=1
                    pygame.mouse.set_cursor(*o_cursor)
                win=if_win()
                if win!="n":
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    if win=="1":
                        winner=1
                        if_game=False
                        if_game_ending=True
                    elif win=="2":
                        winner=2
                        if_game=False
                        if_game_ending=True
                elif 0 not in board:
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    winner = 0
                    if_game = False
                    if_game_ending = True
                if_chosen=False

        #game end screen
        if if_game_ending:
            pygame.mouse.set_cursor(0)
            #when it's a draw
            if winner==0:
                end_draw_rect=pygame.Rect(window_center_x - end_draw_text_x // 2, window_center_y * 0.75, end_draw_text_x, end_draw_text_y)
                window.blit(end_draw_text,end_draw_rect)
            #when there is a winner
            else:
                end_win_text,end_win_text_x,end_win_text_y= win_text(winner)
                end_win_rect=pygame.Rect(window_center_x-end_win_text_x//2,window_center_y*0.75,end_win_text_x,end_win_text_y)
                window.blit(end_win_text,end_win_rect)
            #buttons
            # back to menu button
            menu_rect_box = pygame.Rect(window_center_x*0.75,window_center_y*1.15,menu_button_text_x*1.5,menu_button_text_y*1.5)
            pygame.draw.rect(window, red, menu_rect_box)
            menu_rect_text = menu_rect_box.move(15, 7.5)
            window.blit(menu_button_text, menu_rect_text)
            #play again button
            again_rect_box=pygame.Rect(window_center_x*1.1,window_center_y*1.15,again_button_text_x*1.25,again_button_text_y*1.5)
            pygame.draw.rect(window,green,again_rect_box)
            again_rect_text=again_rect_box.move(20,7.5)
            window.blit(again_button_text,again_rect_text)

        #settings
        if if_settings:
            pygame.mouse.set_cursor(0)
            #settings text
            settings_rect=pygame.Rect(window_center_x-settings_text_x//2,window_center_y*0.5,settings_text_x,settings_text_y)
            window.blit(settings_text,settings_rect)
            #buttons
            # back to menu button
            menu_rect_box = pygame.Rect(window_center_x-menu_button_text_x//2 , window_center_y * 1.5, menu_button_text_x * 1.5,menu_button_text_y * 1.5)
            pygame.draw.rect(window, red, menu_rect_box)
            menu_rect_text = menu_rect_box.move(15, 7.5)
            window.blit(menu_button_text, menu_rect_text)
            #mute/unmute
            mute_rect_box=pygame.Rect(window_center_x-mute_button_text_x//2*1.5,window_center_y*0.75,mute_button_text_x*1.5,mute_button_text_y*1.5)
            if not music_on:
                pygame.draw.rect(window,red,mute_rect_box)
                mute_rect_text=mute_rect_box.move(40,7.5)
                window.blit(mute_button_text1,mute_rect_text)
            else:
                pygame.draw.rect(window, green, mute_rect_box)
                mute_rect_text = mute_rect_box.move(20, 7.5)
                window.blit(mute_button_text2, mute_rect_text)

        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())