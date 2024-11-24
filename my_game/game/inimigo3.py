import pygame
from enemy_laser import EnemyLaser
from math import sin

class StartupCEO(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        file_path = './graphics/green.png'
        original_image = pygame.image.load(file_path).convert_alpha()
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.amplitude = 50  # Amplitude do movimento senoidal
        self.frequency = 0.05  # Velocidade do movimento senoidal
        self.initial_y = y
        self.time = 0
        self.can_shoot = True
        self.shoot_cooldown = 1000  # Alterado para 1 segundo e meio
        self.last_shot_time = pygame.time.get_ticks()

    def update(self, current_time):
        # Movimento senoidal
        self.time += 1
        self.rect.x += self.speed
        self.rect.y = self.initial_y + self.amplitude * sin(self.time * self.frequency)

        # Inverte direção nas bordas
        if self.rect.right >= 600 or self.rect.left <= 0:
            self.speed *= -1

    def shoot(self, current_time):
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.last_shot_time = current_time
            return EnemyLaser(self.rect.center, 5)
        return None