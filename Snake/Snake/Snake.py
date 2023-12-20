import pygame
import sys
import random

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20

BG_COLOR = (0, 0, 0)
HEAD_COLOR = (0, 200, 0)
SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Simple Snake Game')

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render('Game Over. Press "Press any key to continue"', True, (255, 255, 255))
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    WINDOW.blit(text, text_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

def main():
    while True:
        snake = [(5, 5)]
        snake_direction = RIGHT

        apple = (random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1), random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and snake_direction != DOWN:
                snake_direction = UP
            elif keys[pygame.K_DOWN] and snake_direction != UP:
                snake_direction = DOWN
            elif keys[pygame.K_LEFT] and snake_direction != RIGHT:
                snake_direction = LEFT
            elif keys[pygame.K_RIGHT] and snake_direction != LEFT:
                snake_direction = RIGHT

            x, y = snake[0]
            x += snake_direction[0]
            y += snake_direction[1]

            if x < 0 or x >= WINDOW_WIDTH // CELL_SIZE or y < 0 or y >= WINDOW_HEIGHT // CELL_SIZE:
                game_over()
                break

            if (x, y) in snake[1:]:
                game_over()
                break

            snake.insert(0, (x, y))

            if snake[0] == apple:
                apple = (random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1), random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1))
            else:
                snake.pop()

            WINDOW.fill(BG_COLOR)
            pygame.draw.rect(WINDOW, APPLE_COLOR, (apple[0] * CELL_SIZE, apple[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            for i, segment in enumerate(snake):
                color = HEAD_COLOR if i == 0 else SNAKE_COLOR
                rect_size = CELL_SIZE + 2 if i == 0 else CELL_SIZE
                pygame.draw.rect(WINDOW, color, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, rect_size, rect_size))

            pygame.display.flip()

            pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()
