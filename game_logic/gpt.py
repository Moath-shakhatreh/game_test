import pygame
import random

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define monster class
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Load monster image
        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)

        # Set initial position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set movement variables
        self.direction = random.choice([-1, 1])  # -1 for left, 1 for right
        self.distance = random.randint(50, 200)  # Distance to move

    def update(self):
        # Move the monster
        self.rect.x += self.direction

        # Check if the monster reaches the boundaries
        if self.rect.x <= 0 or self.rect.x >= screen_width - self.rect.width:
            self.direction *= -1  # Reverse the direction
            self.rect.y += 50  # Move down

# Create a game screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Monster Movement")

# Create a monster sprite group
all_sprites = pygame.sprite.Group()

# Create multiple monsters
for _ in range(5):
    monster = Monster(random.randint(0, screen_width - 50), random.randint(0, screen_height - 50))
    all_sprites.add(monster)

# Set initial scroll amount
scroll_amount = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Scroll the map
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                scroll_amount += 10
            elif event.button == 5:  # Scroll down
                scroll_amount -= 10

    # Update all sprites
    all_sprites.update()

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw all sprites on the screen with scroll amount applied
    for sprite in all_sprites:
        screen.blit(sprite.image, (sprite.rect.x + scroll_amount, sprite.rect.y))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
