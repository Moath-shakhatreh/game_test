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

# images
ground_image = pygame.image.load("assets\Parallax\dark_ground_04.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 11):
  bg_image = pygame.image.load(f"assets\Parallax/{i}.png").convert_alpha()
  bg_image = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()




def draw_bg():
  for x in range(11):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.1

def update_bg(scroll):
	
	#get keypresses
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
		scroll += 5
	if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
		scroll -= 5
 

def image(direction):
	if direction == "left":
		image = pygame.image.load("assets\character animation\idel\idel1.png").convert_alpha()
		image = pygame.transform.scale2x(image)
		image = pygame.transform.flip(image,True,False) 
	elif direction == "right":
		image = pygame.image.load("assets\character animation\idel\idel1.png").convert_alpha()
		image = pygame.transform.scale2x(image)
	elif direction == "tree":
		image = pygame.image.load("assets\Parallax\Tree_2_256b.png").convert_alpha()
		image = pygame.transform.scale2x(image)
	elif direction == "jump" :
		image = pygame.image.load("assets\character animation\jump\jump5.png").convert_alpha()
		image = pygame.transform.scale2x(image)
	elif direction == "land" :
		image = pygame.image.load("assets\Parallax\dark_ground_04.png").convert_alpha()
	elif direction == 'door': 
		image = pygame.image.load("assets\Parallax\door_02-modified.png").convert_alpha()
	return image
	
      
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = image("right")
		self.rect = self.image.get_rect(midbottom=(100, SCREEN_HEIGHT - (ground_height)))
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
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 1200:
			self.rect.x -= 5

class Objects_to_draw(pygame.sprite.Sprite):
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
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 1200:
			self.rect.x -= 5
		
               
						
def collide():
	for i in range(len(objects.sprites())):
		if objects.sprites()[i].rect.colliderect(player.sprite.rect): 
			if player.sprite.x_velocity < 0  and player.sprite.on_ground == False:
				# player.sprite.rect.left = objects.sprites()[1].rect.right
				player.sprite.x_velocity = 0

			if player.sprite.x_velocity > 0 and player.sprite.on_ground == False:
				# player.sprite.rect.right = objects.sprites()[1].rect.left
				player.sprite.x_velocity = 0


			if player.sprite.y_velocity > 0 : 
				player.sprite.rect.bottom = objects.sprites()[i].rect.top 
				player.sprite.y_velocity = 0 
				player.sprite.on_ground = True

			if player.sprite.y_velocity < 0 : 
				player.sprite.rect.top = objects.sprites()[i].rect.bottom 
				player.sprite.y_velocity = 0
				player.sprite.on_ground = True

	    
   
# groups         these groups should be in the level class 

# player
player = pygame.sprite.GroupSingle()
player.add(Player())

# objects that the player collides with
objects = pygame.sprite.Group()
for i in range(3):
	objects.add(Obstacle('land',(ground_width * i), SCREEN_HEIGHT))
objects.add(Obstacle('land',1300, SCREEN_HEIGHT-150))
objects.add(Obstacle('land',1820, SCREEN_HEIGHT-320))
for i in range(6,20):
	objects.add(Obstacle('land',(ground_width * i), SCREEN_HEIGHT))

# objects just to be drown
objects_d = pygame.sprite.Group()
objects_d.add(Objects_to_draw('tree',250,SCREEN_HEIGHT+25))
objects_d.add(Objects_to_draw('door',4000,SCREEN_HEIGHT - ground_height))


		

#game loop
run = True
while run:

	clock.tick(FPS)

	#draw world
	draw_bg()

	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
		scroll -= 2
	if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 1200:
		scroll += 2

	# draw_trees() 
	objects_d.update()  
	objects_d.draw(screen) 
	objects.update()  
	objects.draw(screen) 
	player.update() 
	player.draw(screen) 
	collide()
	# print(player.sprite.rect.right)

	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()


pygame.quit()