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

speed_x = 3
speed_y = 3

player_1_score = 0
player_2_score = 0

screen = display.set_mode((S_WIDTH, S_HEIGHT))

display.set_caption("ping pong game")
window = display.set_mode((S_WIDTH, S_HEIGHT))

game = True
finish = False
clock = time.Clock()
FPS = 60

paddle1 = Player('racket.png', 30, 200, 50, 150, 4)
paddle2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

font.init()
font1 = font.Font(None, 60)
font2 = font.Font(None, 100)
lose1 = font1.render(
    'PLAYER 1 LOSE!', True, (180, 0, 0)
)
lose2 = font1.render(
    'PLAYER 2 LOSE!', True, (180, 0, 0)
)
score = font2.render(
    '0 | 0' , True, (255, 255, 255)
)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if ball.rect.x < 0:
        player_2_score = player_2_score + 1
        score = font2.render(
            str(player_1_score) + '|' + str(player_2_score)  , True, (255, 255, 255)
        )
        ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

    if ball.rect.x > S_WIDTH - 50:
        player_1_score = player_1_score + 1
        score = font2.render(
            str(player_1_score) + '|' + str(player_2_score)  , True, (255, 255, 255)
        )
        ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

    if player_1_score > 4:
        window.blit(lose2, (150, 150))
        finish = True

    if player_2_score > 4:
        window.blit(lose1, (150, 150))
        finish = True

    if not finish:
        window.fill(BACK)
        window.blit(score, (S_WIDTH // 2 - 60, S_HEIGHT // 2 - 40))

        paddle1.update_l()
        paddle2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y < 0 or ball.rect.y > S_HEIGHT - 50:
            speed_y *= -1

        if sprite.collide_rect(paddle1, ball) or sprite.collide_rect(paddle2, ball):
            speed_x *= -1

        ball.reset()
        paddle1.reset()
        paddle2.reset()

    display.update()
    clock.tick(FPS)
