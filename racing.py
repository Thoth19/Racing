import pygame
import os
import time
screen = pygame.display.set_mode((800,600))
car = pygame.image.load(os.path.join("pics","car.png")).convert()
screen.blit(car,(50,100))
pygame.display.flip()
time.sleep(5)
