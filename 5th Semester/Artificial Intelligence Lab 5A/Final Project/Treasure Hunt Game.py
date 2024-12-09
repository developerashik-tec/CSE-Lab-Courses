import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 40

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TREASURE_COLOR = (255, 223, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Hunt Game")

# Player settings
player_x, player_y = 0, 0
player_color = BLUE

# Grid settings
cols, rows = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE


# Generate random obstacles and treasure
def generate_grid():
    obstacles = []
    for _ in range(20):  # Generate 20 random obstacles
        obstacles.append((random.randint(0, cols - 1), random.randint(0, rows - 1)))

    # Ensure treasure doesn't overlap with obstacles
    treasure = (random.randint(0, cols - 1), random.randint(0, rows - 1))
    while treasure in obstacles:
        treasure = (random.randint(0, cols - 1), random.randint(0, rows - 1))

    return obstacles, treasure


obstacles, treasure = generate_grid()

# Game loop variables
running = True
game_over = False
game_result = ""
clock = pygame.time.Clock()

# Font settings
font = pygame.font.SysFont("Arial", 36)


# Draw grid
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))


# Draw game elements
def draw_elements():
    # Draw obstacles
    for (x, y) in obstacles:
        pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw treasure
    pygame.draw.rect(screen, TREASURE_COLOR, (treasure[0] * GRID_SIZE, treasure[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw player
    pygame.draw.rect(screen, player_color, (player_x * GRID_SIZE, player_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Display game result
def display_message(text, color):
    message = font.render(text, True, color)
    text_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(message, text_rect)


# Main game loop
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_elements()

    if game_over:
        display_message(game_result, GREEN if game_result == "You found the treasure!" else RED)
        pygame.display.flip()
        pygame.time.wait(2000)
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 1
    if keys[pygame.K_DOWN] and player_y < rows - 1:
        player_y += 1
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and player_x < cols - 1:
        player_x += 1

    # Check for treasure collision
    if (player_x, player_y) == treasure:
        game_result = "You found the treasure!"
        game_over = True

    # Check for obstacle collision
    if (player_x, player_y) in obstacles:
        game_result = "You hit an obstacle! Game over."
        game_over = True

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
