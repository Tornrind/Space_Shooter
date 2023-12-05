import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_size = 50
player_speed = 5
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size

# Bullets
bullet_size = 5
bullet_speed = 7
bullets = []


# Small Asteroids
enemy_size = 50
enemy_speed = 3
enemies = []

# Big Asteroids

asteroids_groesser_size = 25
asteroids_groesser_speed = 6
asteroids_2 = []




# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astro Adventures")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_size // 2, player_y])

    # Move bullets
    bullets = [[bx, by - bullet_speed] for bx, by in bullets if by > 0]

    # Generate enemies
    if random.randint(0, 100) < 5:
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemies.append([enemy_x, 0])

    # Move enemies
    enemies = [[ex, ey + enemy_speed] for ex, ey in enemies if ey < HEIGHT]
    asteroids_2 = [[ex, ey + asteroids_groesser_speed] for ex, ey in asteroids_2 if ey< HEIGHT]


    # Check for collisions
    for bullet in bullets:
        for enemy in enemies:
            if (
                enemy[0] < bullet[0] < enemy[0] + enemy_size
                and enemy[1] < bullet[1] < enemy[1] + enemy_size
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Draw everything
    win.fill(WHITE)

    pygame.draw.rect(win, RED, (player_x, player_y, player_size, player_size))

    for bullet in bullets:
        pygame.draw.rect(win, RED, (bullet[0], bullet[1], bullet_size, bullet_size))

    for enemy in enemies:
        pygame.draw.rect(win, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    for asteroid in asteroids_2:
        pygame.draw.rect(win, RED, (asteroid[0], asteroid[1], asteroids_groesser_speed))

    pygame.display.flip()

    # Set the frames per second
    clock.tick(FPS)