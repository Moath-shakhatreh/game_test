import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("assets\Parallax")

#define game variables
scroll = 0

ground_image = pygame.image.load("assets\Parallax\long-platforms_4.png").convert_alpha()
# ground_image = pygame.transform.scale2x(ground_image)
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()




bg_images = []
for i in range(1, 11):
  bg_image = pygame.image.load(f"assets\Parallax/{i}.png").convert_alpha()
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()


def draw_bg():
  for x in range(11):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.1
 
def draw_ground():
	for x in range(2):
		screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))
	for x in range(4,20):
		screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))


def image(direction):
    if direction == "left":
      image = pygame.image.load("assets\character animation\idel\idel1.png")
      image = pygame.transform.scale2x(image)
      image = pygame.transform.flip(image,True,False) 
    elif direction == "right":
      image = pygame.image.load("assets\character animation\idel\idel1.png")
      image = pygame.transform.scale2x(image)
    elif direction == "tree":
        image = pygame.image.load("assets\Parallax\Tree_2_256b.png").convert_alpha()
        image = pygame.transform.scale2x(image)
    elif direction == "jump" :
        image = pygame.image.load("assets\character animation\jump\jump5.png").convert_alpha()
        image = pygame.transform.scale2x(image)
    elif direction == "land" :
        image = pygame.image.load("assets\Parallax\long-platforms_4.png").convert_alpha()
    return image
      

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image("right")
        self.rect = self.image.get_rect(midbottom=(300, SCREEN_HEIGHT - (ground_height // 2)))
        self.x_velocity = 0
        self.y_velocity = 0
        self.on_ground = True

    def update(self):
        self.x_velocity = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x_velocity = -5
            self.image = image("left")
            
            
            
        if keys[pygame.K_RIGHT]:
            self.x_velocity = 5
            self.image = image("right")
            

        # Jumping
        if keys[pygame.K_SPACE] and self.on_ground:
            self.y_velocity = -18
            self.on_ground = False
            # self.image = image("jump")

        # Apply gravity
        self.y_velocity += 0.8

        # Limit the vertical speed
        if self.y_velocity > 10:
            self.y_velocity = 10

        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        if self.rect.bottom >= SCREEN_HEIGHT - (ground_height // 2):
            self.rect.bottom = SCREEN_HEIGHT - (ground_height // 2)
            self.y_velocity = 0
            self.on_ground = True
            
        # fdsfsdf 
        if self.rect.left < 200 :
            self.rect.left = 200
		# dsfsdf 
        if self.rect.right > 1000 : 
            self.rect.right = 1000
		
class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type,x_pos,y_pos):
		super().__init__()
		
		
		material = image(type)
		self.frames = [material]
		self.y_pos = y_pos
		self.x_pos = x_pos
                        
		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (self.x_pos,self.y_pos))
                
	def update(self):
           #get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
			self.rect.x += 7.8
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 7.8
			
		
# def colloide():
#     if pygame.sprite.spritecollide(player.sprite,objects,True):
#         print('true')
#         if player.sprite.rect.bottom == objects.sprites.rect.top :
#             player.sprite.y_velocity = 0
#             player.sprite.on_ground = True
            
            

# groups
player = pygame.sprite.GroupSingle()
player.add(Player())

objects = pygame.sprite.Group()
objects.add(Obstacle('tree',250,SCREEN_HEIGHT+25))

for i in range(1):
	objects.add(Obstacle('land',1140 + (i*ground_width), SCREEN_HEIGHT-100))



#game loop
run = True
while run:

  clock.tick(FPS)

  #draw world
  draw_bg()
  objects.update()
  objects.draw(screen)
  draw_ground()
  player.update()
  player.draw(screen)
#   for sprite in objects.sprites() :
#       sprite.rect.x += 1


  #get keypresses
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
    scroll -= 3
    
  if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
    scroll += 3
    
  
  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()


pygame.quit()