from pygame import *
import play

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
background = (255, 255, 255)
window.fill(background)

class GameSprite(sprite.Sprite):
    def _init_(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super()._init_()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x -= self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x += self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x -= self.speed



game = True
finish = False
clock = time.Clock()
FPS = 60






ball = play.new_circle(
    color='green',
    x=-370, y=80,
    radius=15,
    border_color='yellow')

ball = GameSprite('', 350, 250, 50, 50, 5)


speed_x = 3
speed_y = 3

while game:

    if finish !=True:
        ball.rect.x += speed_x
        ball.rect.y -= speed_y

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
