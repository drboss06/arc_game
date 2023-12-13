import unittest
from gamep import check_collision
import pygame

class TestCollision(unittest.TestCase):
    def test_check_collision(self):
        # Создаем прямоугольник блока
        block_rect = pygame.Rect(100, 100, 50, 50)

        # Создаем прямоугольник шарика
        ball_rect = pygame.Rect(120, 120, 20, 20)

        # Проверяем, что функция check_collision возвращает 1 для коллизии
        self.assertEqual(check_collision([block_rect], ball_rect), 1)

        # # Изменяем позицию шарика, чтобы он не пересекался с блоком
        # ball_rect.x = 200
        # ball_rect.y = 200

        # # Проверяем, что функция check_collision возвращает 0 для отсутствия коллизии
        # self.assertEqual(check_collision([block_rect], ball_rect), 0)

if __name__ == '__main__':
    unittest.main()