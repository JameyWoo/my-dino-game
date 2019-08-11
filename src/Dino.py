# -*- encoding: utf-8 -*-

"""
@file: Dino.py
@time: 2019/8/11 21:46
@author: 姬小野
@version: 0.1
"""
import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed =  speed
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]