import pygame
from sound import *
from healthbar import *
from game_menu import StartGameMenu,PauseGameMenu

pygame.init()
clock = pygame.time.Clock()
FPS = 60
#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("assets\Parallax")


pygame.mixer.set_num_channels(10)

#define game variables
scroll = 0


# images
ground_image = pygame.image.load("assets\Parallax\\aliens_ground_04-modified.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 4):
#   bg_image = pygame.image.load(f"assets\Parallax/{i}.png").convert_alpha()
  bg_image = pygame.image.load(f"assets\Parallax\sky_{i}.png").convert_alpha()
  bg_image = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()




def draw_bg():
  for x in range(11):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.1

		
 

def image(direction,flip = False):
	if direction == "idel":
		image = []
		for i in range(1,7):
			image_ = pygame.image.load(f"assets\\character_animation\\blue\\idle\\idle{i}.png").convert_alpha()
			image_ = pygame.transform.flip(image_,flip,False)
			image.append(pygame.transform.scale2x(image_))
	elif direction == "running":
		image = []
		for i in range(1,9):
			image_ = pygame.image.load(f"assets\\character_animation\\blue\\run\\run{i}.png").convert_alpha()
			image_ = pygame.transform.flip(image_,flip,False)
			image.append(pygame.transform.scale2x(image_))
	elif direction == "attack":
		image = []
		for i in range(1,9):
			image_ = pygame.image.load(f"assets\\character_animation\\blue\\attack\\attack{i}.png").convert_alpha()
			image_ = pygame.transform.flip(image_,flip,False)
			image.append(pygame.transform.scale2x(image_))
	elif direction == "tree":
		image = []
		image.append(pygame.image.load("assets\Parallax\Alien_tileset_tree_06.png").convert_alpha())
	elif direction == "jump" :
		image = []
		for i in range(1,17):
			image_ = pygame.image.load(f"assets\\character_animation\\blue\\jump_up\\jump_up{i}.png").convert_alpha()
			image.append(pygame.transform.scale2x(image_))
	elif direction == "damage":
		image = []
		for i in range(1,5):
			image_ = pygame.image.load(f"assets\\character_animation\\blue\\damage\\damage{i}.png").convert_alpha()
			image.append(pygame.transform.scale2x(image_))
	elif direction == 'healthbar':
		image = []
		for i in range(1,6):
			image_ = pygame.image.load(f"assets\Parallax\health_{i}-modified.png").convert_alpha()
			image.append(image_)
	elif direction == "land" :
		image = pygame.image.load("assets\Parallax\\aliens_ground_04-modified.png").convert_alpha()
	elif direction == 'door': 
		image = []
		image.append(pygame.image.load("assets\Parallax\door_02-modified.png").convert_alpha())
	elif direction == "big_land" :
		image = pygame.image.load("assets\Parallax\\aliens_big_ground_7-modified.png").convert_alpha()
	elif direction == "land_2" :
		image = pygame.image.load("assets\Parallax\land_type2_1.png").convert_alpha()
	elif direction == "land_3" :
		image = pygame.image.load("assets\Parallax\land_type3_1.png").convert_alpha()
	elif direction == "eater":
		image = []
		for i in range(1,5):
			image.append(pygame.image.load(f"assets\Parallax\eater_{i}-modified.png").convert_alpha())
	elif direction == "eater_damage":
		image = []
		for i in range(1,8):
			image.append(pygame.image.load(f"assets\Parallax\eater_damage_{i}-modified.png").convert_alpha())
	elif direction == "flying":
		image = []
		for i in range(1,5):
			image.append(pygame.image.load(f"assets\Parallax\\flying_bot_{i}-modified.png").convert_alpha())
	elif direction == "slime":
		image = []
		for i in range(1,5):
			image.append(pygame.image.load(f"assets\Parallax\slime_{i}-modified.png").convert_alpha())
	elif direction == "coin":
		image = []
		for i in range(1,11):
			image.append(pygame.image.load(f"assets\Parallax\Gold_{i}.png").convert_alpha())
	elif direction == "key":
		image = []
		for i in range(0,24):
			image.append(pygame.image.load(f"assets\Parallax\key_32x32_24f ({i}).png").convert_alpha())
	elif direction == 'wall':
		image = []
		image.append(pygame.image.load(f"assets\Parallax\Wall_5.png").convert_alpha())
	elif direction == 'ground':
		image = pygame.image.load(f"assets\Parallax\ground_4.png").convert_alpha()
	elif direction == 'up_ground':
		image = pygame.image.load(f"assets\Parallax\ground_4.png").convert_alpha()
		image = pygame.transform.flip(image,False,True)
	elif direction == 'f_ground':
		image = pygame.image.load(f"assets\Parallax\ground__1-modified.png").convert_alpha()
	elif direction == "s_ground":
		image = pygame.image.load(f"assets\Parallax\ground__4-modified.png").convert_alpha()
	elif direction == "torch":
		image = []
		for i in range(1,6):
			image_ = pygame.image.load(f"assets\Parallax\\torch__{i}-modified.png").convert_alpha()
			image.append(image_)
	elif direction == "cell" :
		image = []	
		for i in range(1,11):
			image_ = pygame.image.load(f"assets\Parallax\cell__{i}-modified.png").convert_alpha()
			image.append(image_)
	elif direction == "Door" :
		image = []	
		image_ = pygame.image.load(f"assets\Parallax\Door.png").convert_alpha()
		image.append(image_)
	elif direction == "black_box" :
		image = pygame.image.load(f"assets\Parallax\\black_box_1.png").convert_alpha()
	elif direction == "floating_land":
		image = pygame.image.load(f"assets\Parallax\\floating_land_1-modified.png").convert_alpha()
	elif direction == "last_wall":
		image = pygame.image.load(f"assets\Parallax\last_wall-modified.png").convert_alpha()
	elif direction == "chess":
		image = []
		for i in range(1,2):
			image_ = pygame.image.load(f"assets\Parallax\chess_{i}-modified.png").convert_alpha()
			image.append(image_)
	return image

ground_2 = pygame.image.load(f"assets\Parallax\ground_4.png").convert_alpha()
ground_2_width = ground_2.get_width()
     
class Player(pygame.sprite.Sprite):
	def __init__(self,name):
		super().__init__()
		self.type = image("idel")
		self.index = 0
		self.image = self.type[int(self.index)]
		self.rect = self.image.get_rect(midbottom=(300, 300))
		self.x_velocity = 0
		self.y_velocity = 0
		self.on_ground = True
		self.flip = False
		self.state = True
		self.name = name
		self.last_update = pygame.time.get_ticks()
		self.hit_cooldown = 1500
		self.sound = Sound()

		

		# sounds
		self.jump_sound  = pygame.mixer.Sound("assets\\audio\jump_c_02-102843.mp3")
		self.jump_sound.set_volume(0.3)
		self.attack_sound = pygame.mixer.Sound('assets\\audio\sword-hit-7160.mp3')
		self.attack_sound.set_volume(0.3)
		self.damage  = pygame.mixer.Sound("assets\\audio\hurt_c_08-102842.mp3")
		self.damage.set_volume(0.5)
		self.back_ground = pygame.mixer.Sound("assets\\audio\\b_Level1.ogg")
		self.back_ground.set_volume(0.1)
		

	def update(self):
		self.x_velocity = 0
		keys = pygame.key.get_pressed()
		self.index += 0.1
		if self.index > len(self.type)-1:
			self.index = 0
		self.image = self.type[int(self.index)]
		if self.on_ground :
			self.type = image("idel",self.flip)

		if self.name == "player_1":

			if keys[pygame.K_LEFT] :
				self.x_velocity = -5
				self.type = image("running",self.flip)
				self.flip = True
				
			if keys[pygame.K_RIGHT] :
				self.x_velocity = 5
				self.type = image("running")
				self.flip = False
				
			# Jumping
			if keys[pygame.K_UP] and self.on_ground :
				
				self.y_velocity = -18
				self.on_ground = False
				self.type = image('jump')
				pygame.mixer.Channel(0).play(self.jump_sound) 

			for i in range(len(monsters.sprites())):
				if self.rect.colliderect(monsters.sprites()[i].rect):
					self.type = image('damage')

			if keys[pygame.K_RSHIFT]:
				self.type = image('attack',self.flip)
				x = 0
				if x == 0 :
					# self.attack_sound.play()
					pygame.mixer.Channel(7).play(self.attack_sound)
				x += 1
				if x == len(self.type) - 1:
					x = 0
		

		if self.name == "player_2":

			if keys[pygame.K_a] :
				self.x_velocity = -5
				self.type = image("running",self.flip)
				self.flip = True
				
			if keys[pygame.K_d] :
				self.x_velocity = 5
				self.type = image("running")
				self.flip = False
				
			# Jumping
			if keys[pygame.K_w] and self.on_ground:
				self.y_velocity = -18
				self.on_ground = False
				self.type = image('jump')
				pygame.mixer.Channel(1).play(self.jump_sound) 
			

			for i in range(len(monsters.sprites())):
				if self.rect.colliderect(monsters.sprites()[i].rect):
					self.type = image('damage')
			
			if keys[pygame.K_f]:
				self.type = image('attack',self.flip)
				

		if self.name == "player_level_2":          # 555555555555555555

			if keys[pygame.K_LEFT] :
				self.x_velocity = -5
				self.type = image("running",self.flip)
				self.flip = True
				
			if keys[pygame.K_RIGHT] :
				self.x_velocity = 5
				self.type = image("running")
				self.flip = False
				
			# Jumping
			if keys[pygame.K_UP] and self.on_ground:
				self.y_velocity = -18
				self.on_ground = False
				self.type = image('jump')
				# pygame.mixer.Channel(1).play(self.jump_sound) 
			

			# for i in range(len(monsters.sprites())):
			# 	if self.rect.colliderect(monsters.sprites()[i].rect):
			# 		self.type = image('damage')
			
			if keys[pygame.K_m]:
				self.type = image('attack',self.flip)
				
        
				
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


class Health(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		self.type= image(type)
		self.index = 0
		self.image = self.type[self.index]
		self.rect = self.image.get_rect(topleft = (50,50))
		self.last_update = pygame.time.get_ticks()
		self.hit_cooldown = 1500
		0
		
	def update(self):
		self.image = self.type[self.index]


		if self.index > 4 :
			self.index = 0

		
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
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5
 
		if key[pygame.K_LEFT] and player_level_2.sprite.rect.left < 201 and scroll > 0:           # 555555555555555555
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player_level_2.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5


class Objects_to_draw(pygame.sprite.Sprite):
	def __init__(self,type,x_pos,y_pos):
		super().__init__()
		
		
		self.type = image(type)
		# self.frames = [self.type]
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.animation_index = 0
		self.image = self.type[int(self.animation_index)]
		self.rect = self.image.get_rect(midbottom = (self.x_pos,self.y_pos))

                
	def update(self):
           #get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5

		if key[pygame.K_LEFT] and player_level_2.sprite.rect.left < 201 and scroll > 0:      # 555555555555555555
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player_level_2.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5

		self.animation_index += 0.1
		self.image = self.type[int(self.animation_index)]        # 5555555555
		if self.animation_index > len(self.type)-1 :
			self.animation_index = 0


class Monsters(pygame.sprite.Sprite):
	def __init__(self,type,x_pos,y_pos,distance,speed,start_point):
		super().__init__()
		
		self.type = image(type)
		self.x_pos = x_pos           
		self.y_pos = y_pos
		self.start_point = start_point
		self.animation_index = 0
		self.state = False
		self.speed = speed
		self.distance = distance
		self.image = self.type[int(self.animation_index)]
		self.rect = self.image.get_rect(bottomleft = (self.x_pos,self.y_pos))
		self.death = False
		self.death_count = 0
		self.t = type

		self.death_sound  = pygame.mixer.Sound("assets\\audio\mixkit-exclamation-of-pain-from-a-zombie-2207.wav")
		self.death_sound.set_volume(0.2)
		
                
	def update(self):
           #get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5

		if key[pygame.K_LEFT] and player_level_2.sprite.rect.left < 201 and scroll > 0:          # 555555555555555555
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player_level_2.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5
		
        

		self.animation_index += 0.1
		self.image = self.type[int(self.animation_index)]
		if self.animation_index > len(self.type)-1 :
			self.animation_index = 0
		
		self.rect.x += self.speed
		
		
		# if self.rect.x <= objects.sprites()[self.start_point].rect.x or self.rect.x >= objects.sprites()[self.start_point].rect.x + self.distance:
		# 	self.speed *= -1  # Reverse the direction
		# 	self.state = not(self.state)

		if self.rect.x <= objects_level_2.sprites()[self.start_point].rect.x or self.rect.x >= objects_level_2.sprites()[self.start_point].rect.x + self.distance:
			self.speed *= -1  # Reverse the direction             # 555555555555555555
			self.state = not(self.state)
				
		if self.state :
			self.image = pygame.transform.flip(self.image, True,False)

		current_time = pygame.time.get_ticks()
		if key[pygame.K_RSHIFT] and player.sprite.rect.colliderect(self.rect) and  current_time - player.sprite.last_update >= player.sprite.hit_cooldown:
			if self.t == "eater" :
				self.type = image('eater_damage')
				pygame.mixer.Channel(8).play(self.death_sound)
				self.death = True

		if key[pygame.K_RSHIFT] and player_level_2.sprite.rect.colliderect(self.rect) and  current_time - player_level_2.sprite.last_update >= player_level_2.sprite.hit_cooldown:
			if self.t == "eater" :
				self.type = image('eater_damage')        # 555555555555555555
				# pygame.mixer.Channel(8).play(self.death_sound)
				self.death = True


			# pygame.time.wait(100)
			# self.kill()
		if self.death == True:
			self.death_count += 1
			if self.death_count == 50:
				self.kill()
	

class coins(pygame.sprite.Sprite):
	def __init__(self,type,x_pos,y_pos):
		super().__init__()
		
		self.type = image(type)
		self.x_pos = x_pos          
		self.y_pos = y_pos
		self.animation_index = 0
		self.state = False
		self.current_coins = 0
		self.image = self.type[int(self.animation_index)]
		self.rect = self.image.get_rect(bottomleft = (self.x_pos,self.y_pos))

		# sound 
		self.get_damage = pygame.mixer.Sound("assets\\audio\coins.mp3")
		self.get_damage.set_volume(0.5)
                
	def update(self):
           #get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5

		
		if key[pygame.K_LEFT] and player_level_2.sprite.rect.left < 201 and scroll > 0:       # 555555555555555555
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player_level_2.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5
		

		self.animation_index += 0.1
		self.image = self.type[int(self.animation_index)-1]
		if self.animation_index > len(self.type) :
			self.animation_index = 0
		
		global coil_count 
		if player.sprite.rect.colliderect(self.rect):
			pygame.mixer.Channel(2).play(self.get_damage)
			self.kill()
			coil_count += 1

		if player_2.sprite.rect.colliderect(self.rect):      
			pygame.mixer.Channel(3).play(self.get_damage)
			self.kill()
			coil_count += 1 

		if player_level_2.sprite.rect.colliderect(self.rect):    #5555555     
			# pygame.mixer.Channel(3).play(self.get_damage)
			self.kill()
			coil_count += 1 

class key(pygame.sprite.Sprite):
	def __init__(self,type,x_pos,y_pos):
		super().__init__()
		
		self.type = image(type)
		self.x_pos = x_pos          
		self.y_pos = y_pos
		self.animation_index = 0
		self.state = False
		self.image = self.type[int(self.animation_index)]
		self.rect = self.image.get_rect(bottomleft = (self.x_pos,self.y_pos))


		# sound 
		self.get_damage = pygame.mixer.Sound("assets\\audio\coins.mp3")
		self.get_damage.set_volume(0.3)
                
	def update(self):
           #get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5
		

		self.animation_index += 0.1
		self.image = self.type[int(self.animation_index)-1]
		if self.animation_index > len(self.type) :
			self.animation_index = 0
		
		global not_having_key
		if player.sprite.rect.colliderect(self.rect):
			not_having_key = False
			self.kill()
			

		if player_2.sprite.rect.colliderect(self.rect):
			not_having_key = False
			self.kill()
				
def collide():
	
	for i in range(len(objects.sprites())):
		if objects.sprites()[i].rect.colliderect(player.sprite.rect): 
			if player.sprite.x_velocity < 0  and player.sprite.on_ground == False:
				# player.sprite.rect.left = objects.sprites()[i].rect.right
				player.sprite.x_velocity = 0

			if player.sprite.x_velocity > 0 and player.sprite.on_ground == False:
				# player.sprite.rect.right = objects.sprites()[i].rect.left
				player.sprite.x_velocity = 0


			if player.sprite.y_velocity > 0 : 
				player.sprite.rect.bottom = objects.sprites()[i].rect.top 
				player.sprite.y_velocity = 0 
				player.sprite.on_ground = True

			if player.sprite.y_velocity < 0 : 
				player.sprite.rect.top = objects.sprites()[i].rect.bottom 
				player.sprite.y_velocity = 0
				player.sprite.on_ground = False

		if objects.sprites()[i].rect.colliderect(player_2.sprite.rect): 
			if player_2.sprite.x_velocity < 0  and player_2.sprite.on_ground == False:
				# player.sprite.rect.left = objects.sprites()[i].rect.right
				player_2.sprite.x_velocity = 0

			if player_2.sprite.x_velocity > 0 and player_2.sprite.on_ground == False:
				# player.sprite.rect.right = objects.sprites()[i].rect.left
				player_2.sprite.x_velocity = 0


			if player_2.sprite.y_velocity > 0 :
				player_2.sprite.rect.bottom = objects.sprites()[i].rect.top
				player_2.sprite.y_velocity = 0 
				player_2.sprite.on_ground = True

			if player_2.sprite.y_velocity < 0 : 
				player_2.sprite.rect.top = objects.sprites()[i].rect.bottom 
				player_2.sprite.y_velocity = 0
				player_2.sprite.on_ground = False

	for i in range(len(objects_level_2.sprites())):	                              #5555555555
		if objects_level_2.sprites()[i].rect.colliderect(player_level_2.sprite.rect): 
			if player_level_2.sprite.x_velocity < 0  and player_level_2.sprite.on_ground == False:
				# player.sprite.rect.left = objects.sprites()[i].rect.right
				player_level_2.sprite.x_velocity = 0

			if player_level_2.sprite.x_velocity > 0 and player_level_2.sprite.on_ground == False:
				# player.sprite.rect.right = objects.sprites()[i].rect.left
				player_level_2.sprite.x_velocity = 0


			if player_level_2.sprite.y_velocity > 0 : 
				player_level_2.sprite.rect.bottom = objects_level_2.sprites()[i].rect.top 
				player_level_2.sprite.y_velocity = 0 
				player_level_2.sprite.on_ground = True

			if player_level_2.sprite.y_velocity < 0 : 
				player_level_2.sprite.rect.top = objects_level_2.sprites()[i].rect.bottom 
				player_level_2.sprite.y_velocity = 0
				player_level_2.sprite.on_ground = False

		
				
		

	current_time = pygame.time.get_ticks()
	for i in range(len(monsters.sprites())):
		if monsters.sprites()[i].rect.colliderect(player.sprite.rect) and not(key[pygame.K_RSHIFT]) and current_time - player.sprite.last_update >= player.sprite.hit_cooldown:
			player.sprite.last_update = current_time
			health.sprite.index += 1
			pygame.mixer.Channel(4).play(player.sprite.damage)
			

	global key_count
	key_sound  = pygame.mixer.Sound("assets\\audio\Key.wav")
	key_sound.set_volume(0.5)
	if not_having_key :
		image__ = pygame.image.load((f"assets\Parallax\\not_having_key-modified.png")).convert_alpha()
		screen.blit(image__,(300,50))
				
	if not_having_key == False and key_count == 1:
		image__ = pygame.image.load((f"assets\Parallax\having_key-modified.png")).convert_alpha()
		screen.blit(image__,(300,50))
		pygame.mixer.Channel(5).play(key_sound)
		key_count += 1
		

	
			
			
def quit_game():
    pygame.quit()
    exit()	
	
	

	    
start_game_menu = StartGameMenu(SCREEN_WIDTH, SCREEN_HEIGHT)
pause_menu = PauseGameMenu(SCREEN_WIDTH, SCREEN_HEIGHT)
game_state = "start_game"
pause_or_not = False

   
# groups         these groups should be in the level class 

# player
player = pygame.sprite.GroupSingle()
player.add(Player('player_1'))

player_2 = pygame.sprite.GroupSingle()
player_2.add(Player('player_2'))

# for level two
player_level_2 = pygame.sprite.GroupSingle()
player_level_2.add(Player('player_level_2'))

coil_count = 0

# objects that the player collides with
objects = pygame.sprite.Group()
for i in range(3):
	objects.add(Obstacle('land',(ground_width * i), SCREEN_HEIGHT+20))
objects.add(Obstacle('land',1300, SCREEN_HEIGHT-150))
objects.add(Obstacle('land',1820, SCREEN_HEIGHT-320))
objects.add(Obstacle("big_land",2730,SCREEN_HEIGHT+600))
objects.add(Obstacle('land',(ground_width * 10)+20, SCREEN_HEIGHT-220))
for i in range(11,13):
	objects.add(Obstacle('land',(ground_width * i), SCREEN_HEIGHT+20))
objects.add(Obstacle('land',(ground_width * 13)+70, SCREEN_HEIGHT-150))
objects.add(Obstacle('land',(ground_width * 15)-50, SCREEN_HEIGHT-150))
for i in range(16,20):
	objects.add(Obstacle('land',(ground_width * i), SCREEN_HEIGHT+20))
objects.add(Obstacle('land',(ground_width * 2)+50, SCREEN_HEIGHT-340))
objects.add(Obstacle('land_2',(ground_width * 16)+100, SCREEN_HEIGHT-350))
objects.add(Obstacle('land_2',(ground_width * 17)+100, SCREEN_HEIGHT-350))
objects.add(Obstacle('land_2',(ground_width * 18)+100, SCREEN_HEIGHT-350))
objects.add(Obstacle('land_3',(ground_width * 18)+500, SCREEN_HEIGHT-300))
objects.add(Obstacle('land_3',(ground_width * 18)+800, SCREEN_HEIGHT-450))
objects.add(Obstacle('land_3',(ground_width * 18)+1100, SCREEN_HEIGHT-450))


# for level two
objects_level_2 = pygame.sprite.Group()
objects_level_2.add(Obstacle('f_ground',90,SCREEN_HEIGHT+100))
for i in range(1,6):
	objects_level_2.add(Obstacle('ground',ground_2_width/2 + (i * ground_2_width),SCREEN_HEIGHT))
for i in range(6,9):
	objects_level_2.add(Obstacle('ground',ground_2_width/2 + (i * ground_2_width),SCREEN_HEIGHT-80))
for i in range(9,12):
	objects_level_2.add(Obstacle('ground',ground_2_width/2 + (i * ground_2_width),SCREEN_HEIGHT))
# for i in range(12,15):
# 	objects_level_2.add(Obstacle('ground',ground_2_width/2 + (i * ground_2_width),SCREEN_HEIGHT+50))
# for i in range(15,17):
# 	objects_level_2.add(Obstacle('ground',ground_2_width/2 + (i * ground_2_width),SCREEN_HEIGHT))
objects_level_2.add(Obstacle('s_ground',ground_2_width/2 + (18 * ground_2_width),SCREEN_HEIGHT+120))
for i in range(0,23):
	objects_level_2.add(Obstacle('up_ground',ground_2_width/2 + (i * ground_2_width),55))
for i in range(6,9):
	objects_level_2.add(Obstacle('black_box',300/2 + (i * 300),SCREEN_HEIGHT))
# objects_level_2.add(Obstacle('black_box',300/2 + (16 * 300)+120,SCREEN_HEIGHT+65))
objects_level_2.add(Obstacle('black_box',150,SCREEN_HEIGHT+60))
objects_level_2.add(Obstacle('floating_land',ground_2_width/2 + (5 * ground_2_width) - 130,SCREEN_HEIGHT-350))
objects_level_2.add(Obstacle('floating_land',ground_2_width/2 + (5 * ground_2_width) - 550,SCREEN_HEIGHT-400))
objects_level_2.add(Obstacle('floating_land',ground_2_width/2 + (13 * ground_2_width) - 170,SCREEN_HEIGHT-200))
objects_level_2.add(Obstacle('floating_land',ground_2_width/2 + (13 * ground_2_width) +300,SCREEN_HEIGHT-280))
objects_level_2.add(Obstacle('floating_land',ground_2_width/2 + (13 * ground_2_width) +850,SCREEN_HEIGHT-350))
objects_level_2.add(Obstacle('last_wall',ground_2_width/2 + (19 * ground_2_width)+200,SCREEN_HEIGHT))
objects_level_2.add(Obstacle('black_box',ground_2_width/2 + (19 * ground_2_width)+100,SCREEN_HEIGHT))
objects_level_2.add(Obstacle('black_box',ground_2_width/2 + (19 * ground_2_width)+100,SCREEN_HEIGHT-80))
# objects_level_2.add(Obstacle('black_box',ground_2_width/2 + (19 * ground_2_width)+100,SCREEN_HEIGHT-140))


# monsters 
monsters = pygame.sprite.Group()
monsters.add(Monsters('eater',objects.sprites()[2].rect.x,objects.sprites()[2].rect.top,300,3,2))
monsters.add(Monsters('eater',objects.sprites()[3].rect.x,objects.sprites()[3].rect.top,300,4,3))
monsters.add(Monsters('eater',objects.sprites()[4].rect.x,objects.sprites()[4].rect.top,300,4,4))
monsters.add(Monsters('flying',objects.sprites()[5].rect.x,objects.sprites()[5].rect.top,1000,2,5))
monsters.add(Monsters('slime',objects.sprites()[5].rect.x,objects.sprites()[5].rect.top,1000,4,5))
monsters.add(Monsters('eater',objects.sprites()[5].rect.x,objects.sprites()[5].rect.top,1000,3,5))
monsters.add(Monsters('eater',objects.sprites()[6].rect.x,objects.sprites()[6].rect.top,300,3,6))
monsters.add(Monsters('flying',objects.sprites()[7].rect.x,objects.sprites()[7].rect.top,620,2,7))
monsters.add(Monsters('slime',objects.sprites()[7].rect.x,objects.sprites()[7].rect.top,620,4,7))
monsters.add(Monsters('slime',objects.sprites()[9].rect.x,objects.sprites()[9].rect.top,300,4,9))
monsters.add(Monsters('eater',objects.sprites()[10].rect.x,objects.sprites()[10].rect.top,300,3,10))
monsters.add(Monsters('flying',objects.sprites()[11].rect.x,objects.sprites()[11].rect.top,650,2,11))
monsters.add(Monsters('slime',objects.sprites()[11].rect.x,objects.sprites()[11].rect.top,650,5,11))
monsters.add(Monsters('flying',objects.sprites()[13].rect.x,objects.sprites()[13].rect.top,500,2,13))
monsters.add(Monsters('slime',objects.sprites()[13].rect.x,objects.sprites()[13].rect.top,500,5,13))
monsters.add(Monsters('slime',objects.sprites()[15].rect.x,objects.sprites()[15].rect.top,300,4,15))

# for level two
monsters_level_2 = pygame.sprite.Group()
monsters_level_2.add(Monsters('eater',objects_level_2.sprites()[2].rect.x,objects_level_2.sprites()[2].rect.top,1000,4,2))
monsters_level_2.add(Monsters('slime',objects_level_2.sprites()[2].rect.x + 900,objects_level_2.sprites()[2].rect.top,1000,5,2))
monsters_level_2.add(Monsters('flying',objects_level_2.sprites()[6].rect.x  ,objects_level_2.sprites()[6].rect.top ,800,3,6))
monsters_level_2.add(Monsters('eater',objects_level_2.sprites()[9].rect.x  ,objects_level_2.sprites()[9].rect.top ,800,3,9))
monsters_level_2.add(Monsters('slime',objects_level_2.sprites()[42].rect.x ,objects_level_2.sprites()[42].rect.top,220,4,42))
monsters_level_2.add(Monsters('slime',objects_level_2.sprites()[43].rect.x ,objects_level_2.sprites()[43].rect.top,220,4,43))
monsters_level_2.add(Monsters('slime',objects_level_2.sprites()[44].rect.x ,objects_level_2.sprites()[44].rect.top,220,4,44))



coin = pygame.sprite.Group()
coin.add(coins('coin',objects.sprites()[15].rect.x +20 ,objects.sprites()[15].rect.y - 40))
coin.add(coins('coin',objects.sprites()[15].rect.x + 170 ,objects.sprites()[15].rect.y - 40))
coin.add(coins('coin',objects.sprites()[15].rect.x + 300 ,objects.sprites()[15].rect.y - 40))
coin.add(coins('coin',objects.sprites()[3].rect.x + 400 ,objects.sprites()[3].rect.y - 80))
coin.add(coins('coin',objects.sprites()[4].rect.x + 410 ,objects.sprites()[4].rect.y - 80))
coin.add(coins('coin',objects.sprites()[5].rect.x + 180 ,objects.sprites()[5].rect.y - 150))
coin.add(coins('coin',objects.sprites()[5].rect.x + 380 ,objects.sprites()[5].rect.y - 20))
coin.add(coins('coin',objects.sprites()[5].rect.x + 580 ,objects.sprites()[5].rect.y - 150))
coin.add(coins('coin',objects.sprites()[5].rect.x + 780 ,objects.sprites()[5].rect.y - 20))
coin.add(coins('coin',objects.sprites()[5].rect.x + 980 ,objects.sprites()[5].rect.y - 150))
coin.add(coins('coin',objects.sprites()[6].rect.x + 160 ,objects.sprites()[6].rect.y - 40))
coin.add(coins('coin',objects.sprites()[7].rect.x + 50 ,objects.sprites()[7].rect.y - 40))
coin.add(coins('coin',objects.sprites()[7].rect.x + 350 ,objects.sprites()[7].rect.y - 40))
coin.add(coins('coin',objects.sprites()[7].rect.x + 600 ,objects.sprites()[7].rect.y - 40))
coin.add(coins('coin',objects.sprites()[9].rect.x + 160 ,objects.sprites()[9].rect.y - 40))
coin.add(coins('coin',objects.sprites()[9].rect.x + 450 ,objects.sprites()[9].rect.y - 150))
coin.add(coins('coin',objects.sprites()[10].rect.x + 160 ,objects.sprites()[10].rect.y - 40))
coin.add(coins('coin',objects.sprites()[11].rect.x + 160 ,objects.sprites()[11].rect.y - 40))
coin.add(coins('coin',objects.sprites()[12].rect.x + 160 ,objects.sprites()[12].rect.y - 40))
coin.add(coins('coin',objects.sprites()[13].rect.x + 160 ,objects.sprites()[13].rect.y - 40))
coin.add(coins('coin',objects.sprites()[14].rect.x + 160 ,objects.sprites()[14].rect.y - 40))
coin.add(coins('coin',objects.sprites()[16].rect.x + 20 ,objects.sprites()[16].rect.y - 40))
coin.add(coins('coin',objects.sprites()[17].rect.x + 20 ,objects.sprites()[17].rect.y - 40))
coin.add(coins('coin',objects.sprites()[18].rect.x + 20 ,objects.sprites()[18].rect.y - 40))
coin.add(coins('coin',objects.sprites()[21].rect.x + 1000 ,objects.sprites()[21].rect.y - 20))

# for level 2
coin_level_2 = pygame.sprite.Group()
coin_level_2.add(coins('coin',objects_level_2.sprites()[1].rect.x +100 ,objects_level_2.sprites()[2].rect.y -10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[2].rect.x +180 ,objects_level_2.sprites()[2].rect.y -10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[3].rect.x +180,objects_level_2.sprites()[2].rect.y -10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[3].rect.x +120,objects_level_2.sprites()[2].rect.y -350))
coin_level_2.add(coins('coin',objects_level_2.sprites()[4].rect.x +180,objects_level_2.sprites()[2].rect.y -10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[40].rect.x+ 140,objects_level_2.sprites()[40].rect.y -10))



coin_level_2.add(coins('coin',objects_level_2.sprites()[6].rect.x +20,objects_level_2.sprites()[6].rect.y-10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[6].rect.x +120,objects_level_2.sprites()[6].rect.y-150))
coin_level_2.add(coins('coin',objects_level_2.sprites()[6].rect.x +240,objects_level_2.sprites()[6].rect.y-10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[6].rect.x +340,objects_level_2.sprites()[6].rect.y-150))
coin_level_2.add(coins('coin',objects_level_2.sprites()[6].rect.x +460,objects_level_2.sprites()[6].rect.y-10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[6].rect.x +560,objects_level_2.sprites()[6].rect.y-150))
coin_level_2.add(coins('coin',objects_level_2.sprites()[6].rect.x +680,objects_level_2.sprites()[6].rect.y-10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[6].rect.x +780,objects_level_2.sprites()[6].rect.y-150))
coin_level_2.add(coins('coin',objects_level_2.sprites()[42].rect.x +120 ,objects_level_2.sprites()[42].rect.y -20))
coin_level_2.add(coins('coin',objects_level_2.sprites()[43].rect.x +120 ,objects_level_2.sprites()[43].rect.y -20))
coin_level_2.add(coins('coin',objects_level_2.sprites()[44].rect.x +120 ,objects_level_2.sprites()[44].rect.y -20))
coin_level_2.add(coins('coin',objects_level_2.sprites()[9].rect.x +20 ,objects_level_2.sprites()[9].rect.y -10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[9].rect.x +320 ,objects_level_2.sprites()[9].rect.y -10))
coin_level_2.add(coins('coin',objects_level_2.sprites()[9].rect.x +620 ,objects_level_2.sprites()[9].rect.y -10))

keys = pygame.sprite.GroupSingle()
keys.add(key('key',objects.sprites()[21].rect.x + 5 ,objects.sprites()[21].rect.y - 20))





# objects just to be drown
objects_d = pygame.sprite.Group()
objects_d.add(Objects_to_draw('tree',250,SCREEN_HEIGHT-ground_height+20))
objects_d.add(Objects_to_draw('door',(ground_width * 19)+130,SCREEN_HEIGHT - ground_height+20))

# for level two
objects_d_level_2 = pygame.sprite.Group()
for i in range(2):
	objects_d_level_2.add(Objects_to_draw('wall',6000 * i ,750))
objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[2].rect.x -200,objects.sprites()[2].rect.y - 180))
objects_d_level_2.add(Objects_to_draw('cell',objects_level_2.sprites()[2].rect.x +10,objects.sprites()[2].rect.y-70))
objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[2].rect.x +220,objects.sprites()[2].rect.y - 180))
objects_d_level_2.add(Objects_to_draw('cell',objects_level_2.sprites()[2].rect.x +430,objects.sprites()[2].rect.y-70))
objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[2].rect.x +640,objects.sprites()[2].rect.y - 180))
objects_d_level_2.add(Objects_to_draw('cell',objects_level_2.sprites()[2].rect.x +850,objects.sprites()[2].rect.y-70))
objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[2].rect.x +1060,objects.sprites()[2].rect.y - 180))

objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[7].rect.x - 10,objects.sprites()[7].rect.y -230))
objects_d_level_2.add(Objects_to_draw('Door',objects_level_2.sprites()[7].rect.x +150,objects.sprites()[7].rect.y-160))
objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[7].rect.x +310,objects.sprites()[7].rect.y -230))

objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[10].rect.x ,objects.sprites()[10].rect.y ))
objects_d_level_2.add(Objects_to_draw('cell',objects_level_2.sprites()[10].rect.x +210,objects.sprites()[10].rect.y + 100))
objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[10].rect.x +440,objects.sprites()[10].rect.y))

objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[43].rect.x -380 ,objects_level_2.sprites()[43].rect.y -100))
objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[43].rect.x +120 ,objects_level_2.sprites()[43].rect.y -100))
objects_d_level_2.add(Objects_to_draw('torch',objects_level_2.sprites()[43].rect.x +620 ,objects_level_2.sprites()[43].rect.y -100))

objects_d_level_2.add(Objects_to_draw('chess',objects_level_2.sprites()[12].rect.x + 500 ,objects_level_2.sprites()[12].rect.y))









health = pygame.sprite.GroupSingle()
health.add(Health("healthbar"))
		

back_ground_ = pygame.mixer.Sound("assets\\audio\Kim Lightyear - The Final.mp3")
back_ground_.set_volume(0.1)

not_having_key = True
key_count = 1

#game loop
run = True
while run:
	frame_rate = clock.get_fps()
	# print(frame_rate)
	clock.tick(FPS)

	if game_state == "start_game":
			screen.fill((0, 0, 0))
			start_game_menu.start_game_draw(screen)
		
	elif game_state == "playing":
		# this line here is to fill the screen with black
		# screen.fill((0, 0, 0))
		draw_bg()
		
		if pause_or_not:
			pause_menu.resume_button.hover()
			pause_menu.quit_button.hover()
			pause_menu.pause_game_draw(screen)
		else:
			key = pygame.key.get_pressed()
			if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
				scroll -= 2
			elif key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
				scroll += 2

			if key[pygame.K_LEFT] and player_level_2.sprite.rect.left < 201 and scroll > 0:
				scroll -= 2
			elif key[pygame.K_RIGHT] and player_level_2.sprite.rect.right > 999 and scroll < 3000:
				scroll += 2
			
			# player.sprite.back_ground.play()
			# pygame.mixer.Channel(6).play(back_ground_)
			# back_ground_.play()
			font = pygame.font.Font("assets\\fonts\game_over.ttf", 90)
			text = font.render(f'Coins : {coil_count}/24', True, "#F5F5F5")
			text_rect = text.get_rect(center=(SCREEN_WIDTH/2,50))
				
				
			
			screen.blit(text,text_rect)
			# objects_d.update()  
			# objects_d.draw(screen) 
			objects_d_level_2.update()
			objects_d_level_2.draw(screen)
			# objects.update()  
			# objects.draw(screen) 
			objects_level_2.update()
			objects_level_2.draw(screen)
			# monsters.update()
			# monsters.draw(screen)
			monsters_level_2.update()
			monsters_level_2.draw(screen)
			# coin.update()
			# coin.draw(screen)
			coin_level_2.update()
			coin_level_2.draw(screen)
			# keys.update()
			# keys.draw(screen)
			# player.update() 
			# player.draw(screen) 
			player_level_2.update() 
			player_level_2.draw(screen)
			# player_2.update() 
			# player_2.draw(screen) 
			# health.update()
			# health.draw(screen)
			collide()
			# print(len(objects_level_2.sprites()))
			

	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		
		if game_state == "start_game":
			start_game_menu.play_button.hover()
			start_game_menu.quit_button.hover()
			if start_game_menu.play_button.button_clicked(event):
				game_state = "playing"
			if start_game_menu.quit_button.button_clicked(event):
				quit_game()
		elif game_state == "playing":
			# puase menu events handler
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or  health.sprite.index == 4:       #  i edited this lineeeeeeeeeee
					pause_or_not = True
				if  player.sprite.rect.y > SCREEN_HEIGHT + 100:            #  i edited this lineeeeeeeeeee
					pause_or_not = True                              #  i edited this lineeeeeeeeeee
			if pause_menu.resume_button.button_clicked(event):
				pause_or_not = False
			if pause_menu.quit_button.button_clicked(event):
				pause_or_not = False
				game_state = "start_game"

	pygame.display.update()


pygame.quit()