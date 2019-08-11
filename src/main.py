# -*- encoding: utf-8 -*-

"""
@file: main.py.py
@time: 2019/8/11 21:46
@author: 姬小野
@version: 0.1
"""
import pygame
import sys
import random
from Status import *
from Dino import Dino
from Cactus import Cactus
from Cloud import Cloud


def main():
    # 一些初始化
    pygame.init()
    pygame.mixer.init()
    pygame.display.init()
    pygame.key.set_repeat(100, 10)  # 设置重复响应间隔位10ms
    bg_size = width, height = 1200, 600  # 设置游戏窗口大小
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("模仿dino游戏")  # 设置标题

    dino_1 = Dino('../images/dino_1.png', (50, 300), [0, 0])
    dino = dino_1
    dino_2 = Dino('../images/dino_2.png', (50, 300), [0, 0])
    dino_3 = Dino('../images/dino_3.png', (50, 300), [0, -7])
    cactus_1 = Cactus('../images/cactus_1.png', (400, 300), [-7, 0])
    cactus_2 = Cactus('../images/cactus_2.png', (random.random()*200 + 500, 320), [-7, 0])

    running = True
    is_game_over = False
    clock = pygame.time.Clock()
    count = 0
    jump = False
    jump_count = 0  # 跳跃计数

    while running:
        count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 叉掉退出
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # 按q退出
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    jump = True
        if not is_game_over:
            if cactus_1.rect.left < 0:
                cactus_1.rect.left = width
            if cactus_2.rect.left < 0:
                cactus_2.rect.left = width

            enemies = [cactus_1, cactus_2]
            knock = pygame.sprite.spritecollide(dino, enemies, False, pygame.sprite.collide_mask)
            if len(knock) != 0:
                is_game_over = True

            screen.fill((255, 255, 255))
            if not jump:
                if count % 30 < 15:
                    dino = dino_1
                    screen.blit(dino_1.image, dino_1.rect)
                else:
                    dino = dino_2
                    screen.blit(dino_2.image, dino_2.rect)
            else:
                dino = dino_3
                jump_count += 1
                if jump_count == 30:
                    dino_3.speed = [0, 7]
                elif jump_count == 60:
                    jump = False
                    dino_3.rect.left, dino_3.rect.top = 50, 300
                    dino_3.speed = [0, -7]
                    jump_count = 0
                dino_3.move()
                # print(dino_3.rect)
                screen.blit(dino_3.image, dino_3.rect)
            cactus_1.move()
            screen.blit(cactus_1.image, cactus_1.rect)
            cactus_2.move()
            screen.blit(cactus_2.image, cactus_2.rect)

        if is_game_over:  # 游戏结束, 两个选项, 重新开始还是退出游戏
            screen.fill((255, 255, 255))
            screen.blit(dino_1.image, dino_1.rect)
            game_over = pygame.font.Font('../font/font.ttf', 80)
            game_over_font = game_over.render("Game Over", True, (0, 0, 0))
            game_over_loc = (450, 150)
            screen.blit(game_over_font, game_over_loc)
            restart = game_over.render("Restart Game", True, (0, 0, 0))
            restart_loc = (450, 220)
            screen.blit(restart, restart_loc)
            restart_pos = restart.get_rect()
            game_exit = game_over.render("Exit Game", True, (0, 0, 0))
            game_exit_loc = (450, 300)
            screen.blit(game_exit, game_exit_loc)
            game_exit_pos = game_exit.get_rect()

            # 奇怪的位置, 为什么初始时不是返回正确位置
            restart_pos.left, restart_pos.top = restart_loc
            game_exit_pos.left, game_exit_pos.top = game_exit_loc

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if restart_pos.left < pos[0] < restart_pos.right and \
                        restart_pos.top < pos[1] < restart_pos.bottom:
                    # print('重新开始游戏')
                    main()
                elif game_exit_pos.left < pos[0] < game_exit_pos.right and \
                        game_exit_pos.top < pos[1] < game_exit_pos.bottom:
                    # print('退出游戏')
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()