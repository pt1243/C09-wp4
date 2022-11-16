import pygame as pg
import numpy as np
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pg.init()

#colours
white = 255, 255, 255
dark_purple = 48, 25, 52
moon_grey = 114, 115, 117
mango_orange = 255, 130, 67
burnt_orange = 191, 87, 0
teal = 0, 128, 128
light_wood_brown = 193, 154, 107
colour_lst = [(240, 232, 205), (219, 213, 185), (192, 186, 153), (254, 235, 201), (253, 202, 162), ( 252, 169, 133),
              (255, 237, 81), (255, 250, 129), (224, 243, 176), (191, 228, 118), (133, 202, 93), (207, 236, 207),
              (181, 225, 174), (145, 210, 144), (179, 226, 221), (134, 207, 190), (72, 181, 163), (204, 236, 239),
              (154, 206, 223), (111, 183, 214), (191, 213, 232), (191, 213, 232), (148, 168, 208), (117, 137, 191),
              (231, 212, 232), (193, 179, 215), (165, 137, 193), (253, 222, 238), (251, 182, 209), (249, 140, 182)]

size = width, height = 800, 800
brick_size = brick_width, brick_height = 40, 40  #40 by 15 was in original assignment
paddle_size = paddle_width, paddle_height = 60, 6

reso = screenwidth, screenheight = 800, 800  #note: y axis is pointing positive DOWN
scr = pg.display.set_mode(reso)
pg.display.set_caption(("Breakout"))

font = pg.font.SysFont('arial', 30)
end_text = font.render("G A M E   O V E R", True, white, dark_purple)
end_text_rect = end_text.get_rect()
end_text_rect.center = (width // 2, height // 2)
score_lst = []

background = pg.image.load("fuji_3.jpg") #in some folder as this .py
background = pg.transform.scale(background, (size[0], size[1]))

paddle_pos_x, paddle_pos_y = 0.5 * size[0], size[1] - 20    #horizontal, 20 pixels from bottom
paddle_displacement = 5
ball_pos = ball_pos_x, ball_pos_y = 0.5 * size[0] + 30, 0.5 * size[1] + 100 +100             #30 pixels to the right of the centre of the window
ball_speed = ball_speed_x, ball_speed_y = 0, 200      #initial velocity of 600, 600
ball = pg.Rect(ball_pos_x, ball_pos_y, 4, 4)
ball_sprite = pg.sprite.Sprite()  #I wanted to collide, but doesnt work with rect, so defined (an invinsible rect ghost ball) which is a sprite
Ball_group = pg.sprite.Group(ball_sprite)

timestep = 20   #in milliseconds
clock = pg.time.Clock()


class Brick(pg.sprite.Sprite):
    def __init__(self, colour, brick_x, brick_y, width, height): #replace picture_path with colour or else
       pg.sprite.Sprite.__init__(self)
       self.image = pg.Surface([width, height])
       self.rect = self.image.get_rect()

       image_lst = ["Cookie_1.png", "Cookie_2.png", "Cookie_3.png", "Cookie_4.png", "Cookie_5.png", "Cookie_6.png",
                    "Cookie_7.png", "Cookie_8.png"]
       colour = random.choice(colour_lst)
       image = [pg.image.load(name) for name in image_lst]
       image_random_not_scaled = random.choice(image)
       self.image = pg.transform.scale(image_random_not_scaled, (brick_width, brick_height)) #

       #self.image.fill(colour)
       self.rect.center = [brick_x + 0.5 * brick_width, brick_y + 0.5 * brick_height]
    def destroy(self):
        pg.sprite.spritecollide(ball_sprite, Wall_group, True)


#Wall of bricks
Wall_group = pg.sprite.Group()
for yb in range(100, 100 + brick_height * 8, brick_height):
    for xb in range(0, size[0], brick_width):
        new_brick = Brick(moon_grey, xb, yb, brick_width, brick_height) #moon_grey instead of "png"
        pg.draw.rect(scr, white, (xb, yb, brick_width, brick_height), 0)
        Wall_group.add(new_brick)


running = True
grid = []
while running:
    for event in pg.event.get(): #user did something
        if event.type == pg.QUIT:
            running = False

    scr.fill(dark_purple)
    scr.blit(background, (0, 0))
    score = len(score_lst)
    score_text = font.render("SCORE " + str(score), True, dark_purple)

    ball_sprite.image = pg.Surface((8, 8)) #basicaly the hitbox of the ball
    ball_sprite.rect = pg.Rect(ball_pos_x, ball_pos_y, 8, 8)
    collide = pg.sprite.spritecollide(ball_sprite, Wall_group, True)

    #paddle movement
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        if paddle_pos_x > 0:
            paddle_pos_x -= paddle_displacement
        else:
            paddle_pos_x = 0
    if keys[pg.K_RIGHT]:
        if paddle_pos_x < size[0] - paddle_width:  #it takes x position starting from left side
            paddle_pos_x += paddle_displacement
        else:
            paddle_pos_x = size[0] - paddle_width


    switch_x = ""
    switch_y = ""
    if ball_pos_y + 4 >= paddle_pos_y and paddle_pos_x <= ball_pos_x <= paddle_pos_x + paddle_width and ball_speed_y > 0:
        incidence_angle_deg = 45 * np.pi / 180
        ball_speed = abs(200) / np.sin(incidence_angle_deg)
        d = abs(ball_pos_x - paddle_pos_x - 0.5 * paddle_width)

        multiplier = d / (0.5 * paddle_width)
        max_angle_deg = 35 * np.pi / 180
        if paddle_pos_x <= ball_pos_x < paddle_pos_x + 0.5 * paddle_width:
            ball_speed_x = -np.cos((incidence_angle_deg - multiplier * max_angle_deg)) * ball_speed
            ball_speed_y = -1 * np.sin((incidence_angle_deg - multiplier * max_angle_deg)) * ball_speed
        if paddle_pos_x + 0.5 * paddle_width < ball_pos_x <= paddle_pos_x + paddle_width:
            ball_speed_x = np.cos((incidence_angle_deg - multiplier * max_angle_deg)) * ball_speed
            ball_speed_y = -1 * np.sin((incidence_angle_deg - multiplier * max_angle_deg)) * ball_speed
        if ball_pos_x == paddle_pos_x + 0.5 * paddle_width:
            ball_speed_y = -ball_speed_y
    elif ball_pos_x + 4 >= size[0]:
        ball_speed_x = -1 * ball_speed_x
    elif ball_pos_x - 4 <= 0:
        ball_speed_x = -1 * ball_speed_x
    elif ball_pos_y -4 <= 0:
        ball_speed_y = -1 * ball_speed_y
    elif ball_pos_y + 4 >= size[1]:
        paddle_displacement = 0
        if ball_pos_y - 100 > size[1]:
            ball_speed_x = ball_speed_y = 0
    elif ball_pos_y - 4 > paddle_pos_y:
        paddle_displacement = 0
        if ball_pos_y - 100 > size[1]:
            ball_speed_x = ball_speed_y = 0
    if collide:
        score_lst.append(1)
        if ball_speed_y < 0:
            ball_speed_y = -1 * ball_speed_y
        #ball_speed_y *= 1.005
        #paddle_displacement *= 1.005


    ball_pos_x += ball_speed_x * timestep / 1000
    ball_pos_y += ball_speed_y * timestep / 1000

    #misc
    clock.tick(75)  # 75fps

    scr.blit(score_text, (0, 0))

    Wall_group.draw(scr)  #NB, wall before draw circle, so ball will be drawn over/ on top of wall :)
    if paddle_displacement == 0:
        scr.blit(end_text, end_text_rect)
    pg.draw.rect(scr, light_wood_brown, (paddle_pos_x, paddle_pos_y, paddle_width, paddle_height))
    pg.draw.circle(scr, burnt_orange, (ball_pos_x, ball_pos_y), 4, 0)
    pg.time.wait(timestep)
    pg.display.update()
    pg.display.flip()

pg.quit()

"""Credit background: Inkpendude: https://www.inprnt.com/gallery/inkpendude/mount-fuji-japan-pixel-art/"""
