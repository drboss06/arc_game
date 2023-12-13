import pygame
import sys
import yaml
from make_map import Map
import menu_test


# Определение констант
# SCREEN_SIZE = (800, 600)
# PADDLE_WIDTH, PADDLE_HEIGHT = 80, 15
# BALL_DIAMETER = 15
# FPS = 60
# BLOCK_W, BLOCK_H = 60, 20

with open("setings.yaml", "r") as f:
    setings = yaml.safe_load(f)

SCREEN_SIZE = (setings["screen_size"][0], setings["screen_size"][1])
PADDLE_WIDTH, PADDLE_HEIGHT = setings["PADDLE_WIDTH"], setings["PADDLE_HEIGHT"]
FPS = setings["fps"]
BALL_DIAMETER = setings["BALL_DIAMETER"]
BLOCK_W = setings["BLOCK_W"]
BLOCK_H = setings["BLOCK_H"]
SPEED_B = 1.3
SPEED_P = setings["SPEED_P"]

f.close()

Map = Map("levels.txt", BLOCK_W, BLOCK_H, SCREEN_SIZE)

def check_collision(blocks, ball):
    for block in blocks[:]:  # Итерируемся по копии списка
        if ball.colliderect(block):
            blocks.remove(block)
            #ball_dy *= -1  # Отражаем мяч
            #SPEED_B += 0.1
            return 1
            break

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    paddle_x = SCREEN_SIZE[0] // 2
    ball_x, ball_y = SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - PADDLE_HEIGHT - BALL_DIAMETER
    ball_dx, ball_dy = 3, -3

    # Создание блоков
    # blocks = [pygame.Rect(x, y, BLOCK_W, BLOCK_H) 
    #       for x in range(0, SCREEN_SIZE[0], BLOCK_W)
    #       for y in range(0, SCREEN_SIZE[1] // 4, BLOCK_H)]
    blocks = Map.make_map()
    counter = 0
    for i in blocks:
        counter += 1
        print(i)

    print(counter)
    # Создаём мяч
    ball = pygame.Rect(ball_x, ball_y, BALL_DIAMETER, BALL_DIAMETER)

    # Игровой цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Обновление позиции ракетки
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if paddle_x > 0:
                paddle_x -= 2 * SPEED_P
        if keys[pygame.K_RIGHT]:
            if paddle_x < SCREEN_SIZE[0] - PADDLE_WIDTH:
                paddle_x += 2 * SPEED_P

        # Обновление позиции мяча
        ball.x += ball_dx * 1.3
        ball.y += ball_dy * 1.3

        # Проверка столкновения с краями экрана
        if ball.left < 0 or ball.right > SCREEN_SIZE[0]:
            ball_dx *= -1
        if ball.top < 0:
            ball_dy *= -1
        elif ball.bottom > SCREEN_SIZE[1]:
            print("Game Over!")
            return
        elif (ball.bottom >= SCREEN_SIZE[1] - PADDLE_HEIGHT and
            paddle_x < ball.centerx < paddle_x + PADDLE_WIDTH):
            ball_dy *= -1

        # Проверка столкновения с блоками
        # for block in blocks[:]:  # Итерируемся по копии списка
        #     if ball.colliderect(block):
        #         blocks.remove(block)
        #         ball_dy *= -1  # Отражаем мяч
        #         #SPEED_B += 0.1
        #         break
        if check_collision(blocks, ball):
            ball_dy *= -1

        screen.fill((0, 0, 0))

        # Рисование ракетки и мяча
        pygame.draw.rect(screen, (255, 255, 255), 
                         pygame.Rect((paddle_x, SCREEN_SIZE[1] - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)))
        pygame.draw.circle(screen, pygame.Color("red"), ball.center, BALL_DIAMETER // 2)

        # Рисование блоков
        for block in blocks:
            pygame.draw.rect(screen, (255, 255, 255), block)

        pygame.display.flip()
        clock.tick(FPS)

main_menu = menu_test.Menu(SCREEN_SIZE[0], SCREEN_SIZE[1], main)

if __name__ == "__main__":
    main_menu.main_menu()