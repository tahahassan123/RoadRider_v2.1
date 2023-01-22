import pygame
pygame.init()
pygame.font.init()
import sys
import time
import random
from pygame import mixer

WIDTH = 719
HEIGHT = 480
pygame.display.set_caption("RoadRider", "RR")
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
icon = random.choice(["images/icons/ferrari2.png", "images/icons/ferrari3.png", "images/icons/ferrari1.png", "images/icons/audi.png"])
randomicon = pygame.image.load(icon).convert_alpha()
pygame.display.set_icon(randomicon)
skyblue = (0, 128, 255)
lightgrey = (218, 208, 208)
nightblue = (0, 25, 51)
roadgrey = (64, 64, 64)
grassgreen = (0, 153, 0)
lightblue = (115, 202, 246)
white = (255, 255, 255)
transparent = (0 , 0, 0, 0)
black = (0, 0, 0)
button = pygame.image.load("images/button.png").convert_alpha()
arrow = pygame.image.load("images/arrow.png").convert_alpha()
arrowrotate = pygame.transform.rotate(arrow, 90)
arrowrotate2 = pygame.transform.rotate(arrow, 270)
arrow1 = pygame.transform.scale(arrowrotate, (45, 25))
arrow2 = pygame.transform.scale(arrowrotate2, (45, 25))
speedometer = pygame.image.load("images/speedometer.png").convert_alpha()
allracers = ["vehicles/bmw.png", "vehicles/mustang2.png", "vehicles/corvette.png", "vehicles/mustang.png","vehicles/camry.png", "vehicles/bmwback.png","vehicles/ferrari.png","vehicles/subaru.png", "vehicles/nissanjuke.png","vehicles/test.png" ]
racertext = ["BMW", "Mustang C", "Mustang", "Corvette", "Camry", "BMW GTR", "Ferrari", "Subaru", "Nissan J", "Test Mode"]
vehicle = ["vehicles/traffic6.png", "vehicles/traffic5.png" , "vehicles/traffic4.png","vehicles/traffic3.png", "vehicles/traffic2.png", "vehicles/traffic.png"]
racervehicle = "vehicles/bmw.png" #default racer
vehiclenum = 0
racersizex = 200
racersizey = 140
racer = pygame.image.load(racervehicle).convert_alpha()
racersize = pygame.transform.scale(racer, (racersizex, racersizey))
button1 = pygame.transform.scale(button, (350, 80))
button2 = pygame.transform.scale(button, (380, 110))
button3 = pygame.transform.scale(button, (450, 50))
fps = 20
menucolor = roadgrey
racerX = (WIDTH / 2) - (racersizex / 2)
racerY = HEIGHT - 150
velocity = 170
movingbackground = ["background/road1.png", "background/road2.png", "background/road3.png", "background/road4.png", "background/road5.png", "background/road6.png", "background/road7.png",
                        "background/road8.png", "background/road9.png", "background/road10.png", "background/road11.png", "background/road12.png", "background/road13.png", "background/road14.png",
                        "background/road15.png", "background/road16.png"]
font = pygame.font.Font('fonts/LemonMilkRegular.otf', 32)
font2 = pygame.font.Font("fonts/batman.ttf", 30)
fontsmall = pygame.font.Font("fonts/batman.ttf", 15)
font3 = pygame.font.Font("fonts/batman.ttf", 23)
digitalfont = pygame.font.Font('fonts/Digital.ttf',52)
digitalfont2 = pygame.font.Font('fonts/Digital.ttf',25)
end = pygame.font.SysFont("ubuntu", 98)
trafficsize = 0
background = ""
volume = [1, 1, 1, 1, 1, 1, 1, 1]
fileopen = open("settings.txt", "r")
vol = fileopen.readlines()
for i in range(len(volume)):
   volume[i] = float(vol[i])
playing = 0
crash = mixer.Sound("sound/crash.mp3")
crash.set_volume(volume[1])
acceleration = mixer.Sound("sound/acceleration.mp3")
acceleration.set_volume(volume[2])
constant = mixer.Sound("sound/acceleration2.mp3")
constant.set_volume(volume[2])
carpassing = mixer.Sound("sound/carpassing.mp3")
carpassing.set_volume(volume[3])
skid = mixer.Sound("sound/skid.mp3")
skid.set_volume(volume[4])
hover = mixer.Sound("sound/hover.mp3")
hover.set_volume(volume[5])
click = mixer.Sound("sound/click.mp3")
click.set_volume(volume[6])
click2 = mixer.Sound("sound/click2.mp3")
click2.set_volume(volume[6])
class Menus:
   def mainmenu(self):
    menu = True
    hoverplay = 0
    if playing == 0:
       mixer.music.load("sound/mainmenu.mp3")
       mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume[0])
    while menu:
        WINDOW.fill(black)
        mx, my = pygame.mouse.get_pos()
        play = font2.render("PLAY", True, menucolor)
        option = font2.render("OPTIONS", True, menucolor)
        quitmenu = font2.render("QUIT", True, menucolor)
        WINDOW.blit(button1, (180, 100))
        WINDOW.blit(button1, (180, 200))
        WINDOW.blit(button1, (180, 300))
        WINDOW.blit(play, (314, 118))
        WINDOW.blit(option, (280, 218))
        WINDOW.blit(quitmenu, (318, 318))
        if (510 > mx > 200) and (170 > my > 105):
            if hoverplay == 0:
                hoverplay = 1
                mixer.Sound.play(hover)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            WINDOW.blit(button2, (165, 88))
            WINDOW.blit(play, (314, 118))
        elif  (510 > mx > 200) and (270 > my > 205):
            if hoverplay == 0:
                hoverplay = 1
                mixer.Sound.play(hover)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            WINDOW.blit(button2, (165, 188))
            WINDOW.blit(option, (280, 218))
        elif (510 > mx > 200) and (370 > my > 305):
            if hoverplay == 0:
                hoverplay = 1
                mixer.Sound.play(hover)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            WINDOW.blit(button2, (165, 288))
            WINDOW.blit(quitmenu, (318, 318))
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            hoverplay = 0
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (510 > mx > 200) and (170 > my > 105):
                    mixer.music.stop()
                    mixer.Sound.play(click)
                    time.sleep(2)
                    runit.rungame(self)
                elif (510 > mx > 200) and (270 > my > 205):
                    mixer.Sound.play(click2)
                    time.sleep(0.5)
                    start.options(self)
                elif (510 > mx > 200) and (370 > my > 305):
                    mixer.music.stop()
                    mixer.Sound.play(click2)
                    time.sleep(1.5)
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
   def options(self):
    options = True
    hoverplay = 0
    global vehiclenum, playing
    playing = 1
    while options:
         fileopen = open("settingsV.txt", "r")
         vehiclenum = int(fileopen.read())
         fileopen.close()
         WINDOW.fill(black)
         mx, my = pygame.mouse.get_pos()
         sound = font2.render("SOUND", True, menucolor)
         racerchoose = font3.render("VEHICLE: " + racertext[vehiclenum], True, menucolor)
         back = font2.render("BACK", True, menucolor)
         WINDOW.blit(button1, (180, 100))
         WINDOW.blit(button1, (180, 200))
         WINDOW.blit(button1, (180, 300))
         WINDOW.blit(sound, (294, 118))
         WINDOW.blit(racerchoose, (210, 220))
         WINDOW.blit(back, (308, 318))
         if (510 > mx > 200) and (170 > my > 105):
             if hoverplay == 0:
                 hoverplay = 1
                 mixer.Sound.play(hover)
             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
             WINDOW.blit(button2, (165, 88))
             WINDOW.blit(sound, (294, 118))
         elif (510 > mx > 200) and (270 > my > 205):
             if hoverplay == 0:
                 hoverplay = 1
                 mixer.Sound.play(hover)
             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
             WINDOW.blit(button2, (165, 188))
             WINDOW.blit(racerchoose, (210, 220))
         elif (510 > mx > 200) and (370 > my > 305):
             if hoverplay == 0:
                 hoverplay = 1
                 mixer.Sound.play(hover)
             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
             WINDOW.blit(button2, (165, 288))
             WINDOW.blit(back, (308, 318))
         else:
             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
             hoverplay = 0
         pygame.display.update()
         for event in pygame.event.get():
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     if (510 > mx > 200) and (170 > my > 105):
                        mixer.Sound.play(click2)
                        time.sleep(0.5)
                        start.sound_racer(self)
                     elif (510 > mx > 200) and (270 > my > 205):
                         mixer.Sound.play(click2)
                         vehiclenum += 1
                         if vehiclenum == len(racertext):
                             vehiclenum = 0
                         fileopen = open("settingsV.txt", "w")
                         fileopen.writelines(str(vehiclenum))
                         fileopen.close()
                     elif (510 > mx > 200) and (370 > my > 305):
                         mixer.Sound.play(click2)
                         time.sleep(0.5)
                         start.mainmenu(self)
                 if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
   def sound_racer(self):
       sounds = True
       hoverplay = 0
       global playing
       playing = 1
       while sounds:
           WINDOW.fill(black)
           mx, my = pygame.mouse.get_pos()
           #testposition = font.render( str(mx) + " " + str(my), True, white) for finding mouse position
           musictext = font2.render("  MUSIC: " + str(int(volume[0]*100)) + "%", True, menucolor)
           crashtext = font2.render("  CRASH: " + str(int(volume[1]*100)) + "%", True, menucolor)
           engine = font2.render("  ENGINE: " + str(int(volume[2]*100)) + "%", True, menucolor)
           traffic = font2.render("  TRAFFIC: " + str(int(volume[3]*100)) + "%", True, menucolor)
           tire = font2.render("  TIRES: " + str(int(volume[4]*100)) + "%", True, menucolor)
           hovertext = font2.render("  HOVER: " + str(int(volume[5]*100)) + "%", True, menucolor)
           clicktext = font2.render("  CLICK: " + str(int(volume[6]*100)) + "%", True, menucolor)
           back = font2.render("BACK", True, menucolor)
           #WINDOW.blit(testposition, (30, 30))
           WINDOW.blit(button3, (130, 20)); WINDOW.blit(arrow1,(160, 30)); WINDOW.blit(arrow2,(500, 30))
           WINDOW.blit(button3, (130, 70)); WINDOW.blit(arrow1,(160, 80)); WINDOW.blit(arrow2,(500, 80))
           WINDOW.blit(button3, (130, 120)); WINDOW.blit(arrow1,(160, 130)); WINDOW.blit(arrow2,(500, 130))
           WINDOW.blit(button3, (130, 170)); WINDOW.blit(arrow1,(160, 180)); WINDOW.blit(arrow2,(500, 180))
           WINDOW.blit(button3, (130, 220)); WINDOW.blit(arrow1,(160, 230)); WINDOW.blit(arrow2,(500, 230))
           WINDOW.blit(button3, (130, 270)); WINDOW.blit(arrow1,(160, 280)); WINDOW.blit(arrow2,(500, 280))
           WINDOW.blit(button3, (130, 320)); WINDOW.blit(arrow1,(160, 330)); WINDOW.blit(arrow2,(500, 330))
           WINDOW.blit(button1, (180, 380))
           WINDOW.blit(musictext, (180, 30))
           WINDOW.blit(crashtext, (180, 80))
           WINDOW.blit(engine, (180, 130))
           WINDOW.blit(traffic, (180, 180))
           WINDOW.blit(tire, (180, 230))
           WINDOW.blit(hovertext, (180, 280))
           WINDOW.blit(clicktext, (180, 330))
           WINDOW.blit(back, (308, 402))
           if (515 > mx > 197) and (450 > my > 388):
               if hoverplay == 0:
                   hoverplay = 1
                   mixer.Sound.play(hover)
               pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
               WINDOW.blit(button2, (165, 368))
               WINDOW.blit(back, (308, 402))

           else:
               pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
               hoverplay = 0
           pygame.display.update()
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN:
                   if (204 > mx > 158) and (60 > my > 30) and volume[0] > 0:
                        mixer.Sound.play(hover)
                        volume[0] -= 0.05
                        pygame.mixer.music.set_volume(volume[0])
                   elif (204 > mx > 158) and (110 > my > 80) and volume[1] > 0:
                        mixer.Sound.play(hover)
                        volume[1] -= 0.05
                        crash.set_volume(volume[1])
                   elif (204 > mx > 158) and (160 > my > 130) and volume[2] > 0:
                        mixer.Sound.play(hover)
                        volume[2] -= 0.05
                        acceleration.set_volume(volume[2])
                        constant.set_volume(volume[2])
                   elif (204 > mx > 158) and (210 > my > 180) and volume[3] > 0:
                        mixer.Sound.play(hover)
                        volume[3] -= 0.05
                        carpassing.set_volume(volume[3])
                   elif (204 > mx > 158) and (260 > my > 230) and volume[4] > 0:
                        mixer.Sound.play(hover)
                        volume[4] -= 0.05
                        skid.set_volume(volume[4])
                   elif (204 > mx > 158) and (310 > my > 280) and volume[5] > 0:
                        mixer.Sound.play(hover)
                        volume[5] -= 0.05
                        hover.set_volume(volume[5])
                   elif (204 > mx > 158) and (360 > my > 330) and volume[6] > 0:
                        mixer.Sound.play(hover)
                        volume[6] -= 0.05
                        click.set_volume(volume[6])
                        click2.set_volume(volume[6])
                   elif (550 > mx > 520) and (60 > my > 30) and volume[0] < 1:
                       mixer.Sound.play(hover)
                       volume[0] += 0.05
                       pygame.mixer.music.set_volume(volume[0])
                   elif (550 > mx > 520) and (110 > my > 80) and volume[1] < 1:
                       mixer.Sound.play(hover)
                       volume[1] += 0.05
                       crash.set_volume(volume[1])
                   elif (550 > mx > 520) and (160 > my > 130) and volume[2] < 1:
                       mixer.Sound.play(hover)
                       volume[2] += 0.05
                       acceleration.set_volume(volume[2])
                       constant.set_volume(volume[2])
                   elif (550 > mx > 520) and (210 > my > 180) and volume[3] < 1:
                       mixer.Sound.play(hover)
                       volume[3] += 0.05
                       carpassing.set_volume(volume[3])
                   elif (550 > mx > 520) and (260 > my > 230) and volume[4] < 1:
                       mixer.Sound.play(hover)
                       volume[4] += 0.05
                       skid.set_volume(volume[4])
                   elif (550 > mx > 520) and (310 > my > 280) and volume[5] < 1:
                       mixer.Sound.play(hover)
                       volume[5] += 0.05
                       hover.set_volume(volume[5])
                   elif (550 > mx > 520) and (360 > my > 330) and volume[6] < 1:
                       mixer.Sound.play(hover)
                       volume[6] += 0.05
                       click.set_volume(volume[6])
                       click2.set_volume(volume[6])
                   elif (513 > mx > 200) and (450 > my > 388):
                       mixer.Sound.play(click2)
                       time.sleep(0.5)
                       start.options(self)
               fileopen = open("settings.txt", "w")
               for i in range(len(volume)):
                   fileopen.writelines(str(volume[i]) + "\n")
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
start = Menus

class GameScreens:
   def pause(self, trafficstartx, trafficstarty):
    pygame.mixer.Channel(2).pause()
    pygame.mixer.music.pause()
    constant.stop()
    pygame.mixer.Channel(1).pause()
    paused = True
    while paused:
        pauseoutline = end.render("PAUSED", True, black)
        pausetext = end.render("PAUSED", True, white)
        countinue = fontsmall.render("C: Continue", True, white)
        backmenu = fontsmall.render("M: Main Menu", True, white)
        quitgame = fontsmall.render("Q: Quit", True, white)
        countinueoutline = fontsmall.render("C: Continue", True, black)
        backmenuoutline = fontsmall.render("M: Main Menu", True, black)
        quitgameoutline = fontsmall.render("Q: Quit", True, black)
        WINDOW.blit(trafficsize, (trafficstartx, trafficstarty))
        WINDOW.blit(pauseoutline, (183, 157))
        WINDOW.blit(pausetext, (190, 150))
        WINDOW.blit(countinueoutline, (580, 400))
        WINDOW.blit(backmenuoutline, (580, 420))
        WINDOW.blit(quitgameoutline, (580, 440))
        WINDOW.blit(countinue, (583, 398))
        WINDOW.blit(backmenu, (583, 418))
        WINDOW.blit(quitgame, (583, 438))
        pygame.display.update()
        keypressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if keypressed[pygame.K_c]:
            paused = False
            pygame.mixer.music.unpause()
            pygame.mixer.Channel(1).unpause()
            pygame.mixer.Channel(2).unpause()
        elif keypressed[pygame.K_m]:
            start.mainmenu(self)
        elif keypressed[pygame.K_q]:
            pygame.quit()
            sys.exit()
   def endgame(self, score, trafficstartx, trafficstarty, trafficsize, racerposition):
    mixer.Sound.stop(carpassing)
    mixer.Sound.stop(acceleration)
    mixer.Sound.stop(constant)
    mixer.music.stop()
    crash.play()
    collision = pygame.image.load("images/collision.png")
    collisionsize = pygame.transform.scale(collision, (150, 150))
    gameover = end.render("GAME OVER", True, (white))
    gameoveroutline = end.render("GAME OVER", True, (black))
    final = score
    finalscore = font.render("Final Score: " + str(score), True, (white))
    finalscoreoutline = font.render("Final Score: " + str(score), True, (black))
    countinue = fontsmall.render("C: Continue", True, white)
    backmenu = fontsmall.render("M: Main Menu", True, white)
    quitgame = fontsmall.render("Q: Quit", True, white)
    countinueoutline = fontsmall.render("C: Continue", True, black)
    backmenuoutline = fontsmall.render("M: Main Menu", True, black)
    quitgameoutline = fontsmall.render("Q: Quit", True, black)
    WINDOW.blit(background, (0, 0))
    WINDOW.blit(trafficsize, (trafficstartx, trafficstarty))
    WINDOW.blit(racersize,racerposition)
    WINDOW.blit(collisionsize, (trafficstartx, trafficstarty))
    WINDOW.blit(gameoveroutline, (80, 87))
    WINDOW.blit(gameover, (85, 80))
    WINDOW.blit(finalscoreoutline, (225, 194))
    WINDOW.blit(finalscore, (227, 190))
    WINDOW.blit(countinueoutline, (580, 400))
    WINDOW.blit(backmenuoutline, (580, 420))
    WINDOW.blit(quitgameoutline, (580, 440))
    WINDOW.blit(countinue, (583, 398))
    WINDOW.blit(backmenu, (583, 418))
    WINDOW.blit(quitgame, (583, 438))
    pygame.display.update()

class Display:
   def windowsettings(self, racerposition, backgroundposition, racersize):
    global background
    WINDOW.fill(nightblue)
    background = pygame.image.load(movingbackground[backgroundposition]).convert_alpha()
    WINDOW.blit(background, (0, 0))
    WINDOW.blit(racersize, (racerposition))
   def traffic(self, trafficstartx, trafficstarty, trafficwidth, trafficheight):
    global trafficsize, vehicle, vehicle2
    if trafficstarty == 150:
           vehicle2 = random.choice(vehicle)
           pygame.mixer.Channel(2).play(carpassing)
    traffic = pygame.image.load(vehicle2)
    trafficsize = pygame.transform.scale(traffic, (trafficwidth, trafficheight))
    WINDOW.blit(trafficsize, (trafficstartx, trafficstarty))
    pygame.display.update()
    return vehicle

show = Display

class MainGame:
   def rungame(self):
    global racersize, fps , playing
    playing = 0
    fileopen = open("settingsV.txt", "r")
    vehiclenum = int(fileopen.read())
    fileopen.close()
    #racervehicle = allracers[vehiclenum] future feature
    racer = pygame.image.load(allracers[vehiclenum]).convert_alpha()
    racersize = pygame.transform.scale(racer, (racersizex, racersizey))
    mixer.Sound.stop(crash)
    mixer.music.load("sound/racemusic.mp3")
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume[0])
    pygame.mixer.Channel(1).play(acceleration)
    start = Menus
    gamescreens = GameScreens
    FPS = fps
    mph = 0
    score = 0
    left = 270
    right = 365
    play = 0
    playingaccelertion = 0
    trafficspeed = 5
    trafficstartx = random.choice([left, right])
    trafficstarty = 150
    trafficwidth = 100
    trafficheight = 55
    racerposition = pygame.Rect(racerX, racerY, racersizex, racersizey)
    clock = pygame.time.Clock()
    run = True
    backgroundposition = 0
    USEREVENT = 0
    pygame.time.set_timer(USEREVENT + 1, 500)
    while run:
        clock.tick(FPS)
        scoretext = font.render("Score: " + str(score), True, (white))
        mphtext = digitalfont2.render("MPH", True, (grassgreen))
        scoretextoutline = font.render("Score: " + str(score), True, (black))
        esc = fontsmall.render("ESC: Pause", True, (white))
        if mph <= 180:
            mph = int(FPS * 2.6)
        else:
            playingaccelertion = 1
        if playingaccelertion == 1:
            mixer.Sound.play(constant)
            playingaccelertion = 0
        test = font.render("FOR DEVELOPMENT PURPOSES" , True, (white))
        testoutline = font.render("FOR DEVELOPMENT PURPOSES", True, (black))
        speed = digitalfont.render(str(mph), True, (grassgreen))
        WINDOW.blit(scoretextoutline, (240, 24))
        WINDOW.blit(scoretext, (245, 20))
        WINDOW.blit(esc, (10, 9))
        if vehiclenum == len(allracers) - 1:
           WINDOW.blit(testoutline, (110, 63))
           WINDOW.blit(test, (112, 60))
        score += 1
        score = int(score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == USEREVENT + 1:
                FPS += 1
                trafficspeed += 1
        show.traffic(self, trafficstartx, trafficstarty, trafficwidth, trafficheight)
        trafficcollisionbox = pygame.Rect(trafficstartx, trafficstarty, trafficwidth, trafficheight)
        WINDOW.blit(speedometer, (550, 400))
        WINDOW.blit(speed, (590, 425))
        WINDOW.blit(mphtext, (655, 450))
        pygame.display.update()
        trafficstarty += trafficspeed
        if trafficheight <= 150 and trafficwidth <= 200:
            trafficwidth += trafficspeed
            trafficheight += trafficspeed
        if trafficstartx == right:
            trafficstartx += 1
            right += 1
        elif trafficstartx == left:
            trafficstartx -= 5.5
            left -= 5.5
        if trafficstarty > HEIGHT:
            left = 270
            right = 365
            trafficspeed = 5
            trafficstartx = random.choice([left, right])
            trafficstarty = 150
            trafficwidth = 100
            trafficheight = 50
        keypressed = pygame.key.get_pressed()
        show.windowsettings(self, racerposition, backgroundposition, racersize)
        if keypressed[pygame.K_LEFT] and racerposition.x - velocity > 0:
            racerposition.x -= velocity
            mixer.Sound.play(skid)
        elif keypressed[pygame.K_RIGHT] and racerposition.x + velocity < 480:
            racerposition.x += velocity
            mixer.Sound.play(skid)
        elif keypressed[pygame.K_ESCAPE]:
            gamescreens.pause(self, trafficstartx, trafficstarty)
        if backgroundposition < 14:
            backgroundposition += 1
        else:
            backgroundposition = 0
        if racerposition.colliderect(trafficcollisionbox) and vehiclenum != len(allracers) - 1:
            gamescreens.endgame(self, score, trafficstartx, trafficstarty, trafficsize, racerposition)
            while run:
                keypressed = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if keypressed[pygame.K_c]:
                    run = False
                    runit.rungame(self)
                if keypressed[pygame.K_m]:
                    run = False
                    start.mainmenu(self)
                elif keypressed[pygame.K_q]:
                    pygame.quit()
                    sys.exit()
    pygame.quit()

runit = MainGame
start.mainmenu("dummytext")

