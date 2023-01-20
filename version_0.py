import pygame
pygame.font.init()
import random
WIDTH=1080
HEIGHT=480
pygame.display.set_caption("RoadRider","RR")
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
icon=random.choice(["ferrari2.png","ferrari3.png","ferrari4.png","audi.png"])
randomicon=pygame.image.load(icon)
pygame.display.set_icon(randomicon)
skyblue=(0,128,255)
nightblue=(0,25,51)
roadgrey=(64,64,64)
grassgreen=(0,153,0)
white=(255,255,255)
racer=pygame.image.load("bmwback.png")
racersizex=200
racersizey=140
racersize=pygame.transform.scale(racer,(racersizex,racersizey))
FPS=20
racerX=(WIDTH/2)-(racersizex/2)
racerY=HEIGHT-150
velocity=150
font=pygame.font.Font("freesansbold.ttf",32)
def endgame(score,trafficstartx,trafficstarty,font):
    pygame.font.init()
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
            if event.type == pygame.K_c:
                paused=False
        collision = pygame.image.load("collision.png")
        collisionsize = pygame.transform.scale(collision, (150, 150))

        gameover =font.render("GAME OVER", True, (white))
        Final = score
        Finalscore = font.render("Final Score: " + str(Final), True, (white))
        WINDOW.blit(collisionsize, (trafficstartx, trafficstarty))
        WINDOW.fill((0, 0, 0))
        WINDOW.blit(gameover, (200, 140))
        WINDOW.blit(Finalscore, (280, 250))
def windowsettings(racerposition,backgroundposition):
     WINDOW.fill(nightblue)
     movingbackground=["road1.png","road2.png","road3.png","road4.png","road5.png","road6.png","road7.png","road8.png","road9.png","road10.png","road11.png","road12.png","road13.png","road14.png","road15.png","road16.png"]
     background=pygame.image.load(movingbackground[backgroundposition])
     WINDOW.blit(background, (0,0))
     WINDOW.blit(racersize,(racerposition.x,racerposition.y))
def traffic(trafficstartx,trafficstarty,trafficwidth,trafficheight):
     traffic = pygame.image.load("bmwback.png")
     trafficsize = pygame.transform.scale(traffic, (trafficwidth,trafficheight))

     WINDOW.blit(trafficsize,(trafficstartx,trafficstarty))
def rungame(FPS):
  score=0
  left=270
  right=365
  trafficspeed=5
  trafficstartx=random.choice([left,right])
  trafficstarty=150
  trafficwidth=100
  trafficheight=50
  racerposition=pygame.Rect(racerX,racerY,racersizex,racersizey)
  clock=pygame.time.Clock()
  run=True
  backgroundposition=0
  USEREVENT=0
  pygame.time.set_timer(USEREVENT + 1, 500)
  while run==True:
       clock.tick(FPS)
       scoretext=font.render("Your Score: " + str(score),True,(white))
       WINDOW.blit(scoretext,(800,50))
       score+=1
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run=False
          if event.type == USEREVENT+1:
              FPS+=1
              trafficspeed+=1

       traffic(trafficstartx,trafficstarty,trafficwidth,trafficheight)
       trafficcollisionbox=pygame.Rect(trafficstartx,trafficstarty,trafficwidth,trafficheight)
       pygame.display.update()
       trafficstarty += trafficspeed
       if trafficheight<=150 and trafficwidth<=200:
        trafficwidth+=trafficspeed
        trafficheight+=trafficspeed
       if trafficstartx==right:
          trafficstartx+=1
          right+=1
       elif trafficstartx==left:
          trafficstartx-=5.5
          left-=5.5
       if trafficstarty>HEIGHT:
          left = 270
          right = 365
          trafficspeed = 5
          trafficstartx = random.choice([left, right])
          trafficstarty = 150
          trafficwidth = 100
          trafficheight = 50
       keypressed = pygame.key.get_pressed()
       windowsettings(racerposition,backgroundposition)
       if keypressed[pygame.K_LEFT] and racerposition.x - velocity > 0:
          racerposition.x -= velocity
       elif keypressed[pygame.K_RIGHT] and racerposition.x + velocity < 480:
          racerposition.x += velocity
       if backgroundposition < 14:
          backgroundposition += 1
       else:
          backgroundposition = 0
       if racerposition.colliderect(trafficcollisionbox):
           collision = pygame.image.load("collision.png")
           collisionsize = pygame.transform.scale(collision, (150, 150))
           end=pygame.font.Font("freesansbold.ttf",100)
           gameover = end.render("GAME OVER", True, (white))
           Final = score
           Finalscore = font.render("Final Score: " + str(Final), True, (white))
           WINDOW.blit(collisionsize, (trafficstartx, trafficstarty))
           WINDOW.fill((0, 0, 0))
           WINDOW.blit(gameover, (200, 140))
           WINDOW.blit(Finalscore, (280, 250))
           end=True
           while run==True:
             for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    run=False
                    pygame.quit()



  pygame.quit()
rungame(FPS)