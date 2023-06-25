import pygame
from player import Player, move_player

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("assets\Parallax")

#define game variables
scroll = 0

ground_image = pygame.image.load("assets\Parallax\long-platforms_4.png").convert_alpha()
# ground_image = pygame.transform.scale2x(ground_image)
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

tree = pygame.image.load("assets\Parallax\Tree_2_256b.png").convert_alpha()
# ground_image = pygame.transform.scale2x(tree)





bg_images = []
for i in range(1, 11):
  bg_image = pygame.image.load(f"assets\Parallax/{i}.png").convert_alpha()
  
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
  for x in range(11):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll , 0))
      speed += 0.01

def draw_ground():
  for x in range(15):
    screen.blit(ground_image, ((x * ground_width) - scroll * 1, SCREEN_HEIGHT - ground_height))

def draw_trees():
  tree = pygame.image.load('assets\Parallax\Tree_2_256b.png').convert_alpha()
  screen.blit(tree,(100 - scroll ,150))


def redrawGameWindow():
     
    # win.blit(bg,(0,0))
    player_one.draw(screen)
    # player_two.draw(screen)
    # first_enemy.draw(win)
    # sec_enemy.draw(win)
    # for bullet in bullets:
    #     bullet.draw(win)
    # pygame.display.update()
    
    
player_one = Player(200, SCREEN_HEIGHT - ground_height, 64,64,'player_one')
player_two=Player(200, SCREEN_HEIGHT - ground_height, 64,64,'player_two')



#game loop
run = True
while run:

  clock.tick(FPS)

  #draw world
  draw_bg()
  draw_trees()
  draw_ground()
  redrawGameWindow()
#   screen.blit(tree,(100,100))

  #get keypresses
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT] and scroll > 0:
    scroll -= 5
  if key[pygame.K_RIGHT] and scroll < 3000:
    scroll += 5

  move_player(player_one)
  move_player(player_two)     

  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()


pygame.quit()