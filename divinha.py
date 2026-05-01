from pygame import *
import sys
import random


init()

window = display.set_mode((1280,720))

running = True
clock=time.Clock()
background_color = (112, 128, 144)

num = random.randint(1,1023)
print(num)

tentativas = 0


#mixer.music.load("musica_fundo.mp3")
#mixer.music.set_volume(0.5)
#mixer.music.play(-1)

#dor = mixer.Sound("dor_fortnite.mp3")

#fonte = font.Font("fonte.ttf", 40)

#coracao = image.load("heart.png")
#coracao = transform.scale(coracao, (60,50))



while running:
    clock.tick(60)
    key_pressed = key.get_pressed()
    window.fill(background_color)
    mouse_x, mouse_y = mouse.get_pos()

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()



    display.update()