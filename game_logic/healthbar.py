import pygame
from sound import Sound

sound1=Sound()

# Colors these colors for modify the color of health bar
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE=(255, 165, 0)

# in Player class you must add 
'''
        self.health = 100 # the player's current health
        self.game_over = False  #to create game over instance  a flag indicating whether the game is over or not
        self.health_bar = None
  def decrease_health(self, amount): 
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            sound1.play_loss(.3)
            self.game_over = True

        if self.health_bar:
            self.health_bar.update_health_color()

    def is_game_over(self): 
        return self.game_over

    def set_health_bar(self, health_bar):
        self.health_bar = health_bar
        self.health_bar.update_health_color()
    
'''

# HealthBar class
class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, player):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.player = player
        self.health_color = GREEN

    def update_health_color(self):
            if self.player.sprite.health >= 50:
                self.health_color = GREEN
            elif self.player.sprite.health < 50 and self.player.sprite.health < 20:
                self.health_color = ORANGE
            else:
                self.health_color = RED
        
      

        

    def draw_health(self, surface):
        # Calculate the width of the health bar based on player's health
        health_ratio = self.player.health / 100
        health_width = int(self.width * health_ratio)

        # Draw the background bar (green)
        pygame.draw.rect(surface, GREEN, (self.x, self.y, self.width, self.height))

        # # Calculate the width of the filled portion (red)
        filled_width = int(self.width * (1 - health_ratio))

        # Draw the filled portion (ORANGE)
        pygame.draw.rect(surface, ORANGE, (self.x + health_width, self.y, filled_width, self.height))

        # Draw the remaining portion (green)
        pygame.draw.rect(surface, self.health_color, (self.x, self.y, health_width, self.height))



# put it in main class or game running
'''
 # Detect collisions between player and enemies
    collisions = pygame.sprite.spritecollide(player, enemies, True)
    if collisions:
        player.decrease_health(50)  # Decrease player's health by 40 when player touches an enemy

 if player.is_game_over():
        game_over_text = pygame.font.Font(None, 50).render("Game Over", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)

        # Display "Press ESC to Quit" message
        quit_text = pygame.font.Font(None, 30).render("Press ESC to Quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(quit_text, quit_rect)

        pygame.display.update()
         # Wait for user input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            if not running:
                break
'''