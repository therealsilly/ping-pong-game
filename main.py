from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < S_HEIGHT- 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < S_HEIGHT- 150:
            self.rect.y += self.speed

BACK = (38,38,38)
S_WIDTH = 600
S_HEIGHT = 500

screen = display.set_mode((S_WIDTH, S_HEIGHT))
screen.fill(BACK)

display.set_caption("shooting game")
window = display.set_mode((S_WIDTH, S_HEIGHT))
window.fill(BACK)

game = True
finish = False
clock = time.Clock()
FPS = 60

paddle1 = Player('racket.png', 30, 200, 50, 150, 4)
paddle2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        paddle1.update_l()
        paddle2.update_r()

        window.fill(BACK)
        ball.reset()
        paddle1.reset()
        paddle2.reset()

    display.update()
    clock.tick(FPS)
