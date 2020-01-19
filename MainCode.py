from random import randint
import pygame

pygame.init()
W = 400
H = 400
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
sc = pygame.display.set_mode((1920, 1080))


class Car(pygame.sprite.Sprite):
    def __init__(self, ImageName):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(ImageName).convert_alpha()
        self.rect = self.image.get_rect(center=(100, 100))
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=(100, 100))
        self.angle = 0

    def update(self, angle):
        self.angle = angle
        self.rotate()

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


x_ = 120
car1 = Car('Cars/CarGun1.png')
speed = 10

while 1:
    key = pygame.key.get_pressed()
    if key[pygame.K_s]:
        car1.rect.y += speed
    if key[pygame.K_d]:
        car1.rect.x += speed
    if key[pygame.K_w]:
        car1.rect.y -= speed
    if key[pygame.K_a]:
        car1.rect.x -= speed
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_s:
                car1.update(0)
            if i.key == pygame.K_d:
                car1.update(90)
            if i.key == pygame.K_w:
                car1.update(180)
            if i.key == pygame.K_a:
                car1.update(270)

    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    pygame.display.update()

    clock.tick(60)
