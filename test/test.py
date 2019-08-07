import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import exit
#向sys模块借一个exit函数用来退出程序
import random
#导入random模块，用来生成随机数

'''
1.判断蛇碰到墙壁
2.判断蛇碰到自身
exit()
'''


pygame.init()
#初始化pygame,为使用硬件做准备
 
screen = pygame.display.set_mode((640, 640), 0, 32)
#创建了一个窗口
pygame.display.set_caption("贪吃蛇")
#设置窗口标题

snake = [(10, 10), (10, 11), (10, 12)]
apple = (random.randint(0, 19), random.randint(0, 19))
direction = 0
#0为向上，1为向下，2为向左，3为向右
pygame.time.set_timer(pygame.USEREVENT, 400)
while True:
#游戏主循环
 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
            elif event.key == K_UP:
                direction = 0
            elif event.key == K_DOWN:
                direction = 1
            elif event.key == K_LEFT:
                direction = 2
            elif event.key == K_RIGHT:
                direction = 3
        if event.type == pygame.USEREVENT:
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = snake[i - 1]

            if direction == 0:
                snake[0] = (snake[0][0], snake[0][1] - 1)
            elif direction == 1:
                snake[0] = (snake[0][0], snake[0][1] + 1)
            elif direction == 2:
                snake[0] = (snake[0][0] - 1, snake[0][1])
            elif direction == 3:
                snake[0] = (snake[0][0] + 1, snake[0][1])

            if snake[0] == apple:
                if snake[-1][0] == snake[-2][0]:
                    snake.append((snake[-1][0], snake[-1][1] * 2 - snake[-2][1]))
                else:
                    snake.append((snake[-1][0] * 2 - snake[-2][0], snake[-1][1]))
                apple = (random.randint(0, 19), random.randint(0, 19))

    pygame.draw.rect(screen, (255, 255, 0), (0, 0, 640, 640), 0)
    #绘制背景

    for cp in snake[1:]:
        pygame.draw.circle(screen, (255, 0, 255), (cp[0] * 32 + 16, cp[1] * 32 + 16), 16, 0)
    
    pygame.draw.circle(screen, (255, 0, 0), (apple[0] * 32 + 16, apple[1] * 32 + 16), 16, 0)
    #绘制苹果
    
    pygame.draw.circle(screen, (122, 122, 122), (snake[0][0] * 32 + 16, snake[0][1] * 32 + 16), 16, 0)
    #绘制蛇头
 
    pygame.display.update()
    #视图刷新