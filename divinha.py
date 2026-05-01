from pygame import *
import sys
import random


init()

window = display.set_mode((1280,720))

running = True
clock=time.Clock()
background_color = (112, 128, 144)


escolha = int(input("Escolha 0 para adivinhar o numero ou 1 para o computador tentar adivinhar o numero: "))

if escolha != 0 and escolha != 1:
    quit()

num = random.randint(1,1023)



min_pc = 1
max_pc = 1023
modo_pc = "jogando"
chute_pc = (min_pc + max_pc) // 2

tentativas = 0

numero_escolhido = int(input("Digite um número entre 1 e 1023: "))
if numero_escolhido < 1 or numero_escolhido > 1023:
    print("Número inválido. Por favor, escolha um número entre 1 e 1023.")
    quit()

lista_numeros_menor = [f'Menor que: {numero_escolhido}']
lista_numero_maior = [f"Maior que: {numero_escolhido}"]


maior_num = 0
menor_num = float('inf')

timer = 0

def reset_jogo():
            global maior_num, menor_num, tentativas, num, numero_escolhido
            maior_num = 0
            menor_num = float('inf')
            num = random.randint(1,1023)
            print("-"*30)
            tentativas = 0
            numero_escolhido = 1

def reset_jogo_pc():
            global maior_num, menor_num, tentativas, numero_escolhido, chute_pc, min_pc, max_pc, num
            maior_num = 0
            menor_num = float('inf')
            min_pc = 1
            max_pc = 1023
            num = random.randint(1,1023)
            print("-"*30)
            tentativas = 0
            chute_pc = 512
            numero_escolhido = int(input("Digite um número entre 1 e 1023: "))


#mixer.music.load("musica_fundo.mp3")
#mixer.music.set_volume(0.5)
#mixer.music.play(-1)

#dor = mixer.Sound("dor_fortnite.mp3")

fonte = font.Font("fontechique.ttf", 40)

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

        
        if ev.type == MOUSEBUTTONDOWN and escolha == 0 and timer == 0:
            if 490 <= mouse_x <= 790 and 250 <= mouse_y <= 350:
                if ev.button == 1:
                    print("-"*30)
                    numero_escolhido = int(input("Digite um número entre 1 e 1023: "))
                    if numero_escolhido < 1 or numero_escolhido > 1023:
                        print("Número inválido. Por favor, escolha um número entre 1 e 1023.")
                        quit()
                    tentativas += 1
                    if numero_escolhido < menor_num and numero_escolhido>num:
                        menor_num = numero_escolhido
                    if numero_escolhido > maior_num and numero_escolhido<num:
                        maior_num = numero_escolhido



        if ev.type == MOUSEBUTTONDOWN and escolha == 1 and timer == 0 and modo_pc == "jogando":
            if 490 <= mouse_x <= 790 and 250 <= mouse_y <= 350:
                if ev.button == 1:
                    if chute_pc > numero_escolhido:
                        max_pc = chute_pc-1
                        if chute_pc > maior_num:
                            menor_num = chute_pc
                    
                        
                    if chute_pc < numero_escolhido:
                        min_pc = chute_pc+1
                        if chute_pc < menor_num:
                            maior_num = chute_pc
                    chute_pc = (min_pc + max_pc) // 2
                    tentativas += 1

    if escolha == 0:
        #num_texto = fonte.render(f"Seu número é {numero_escolhido}", True, (255,255,255))
        #window.blit(num_texto, (500,50))

        #num_random = fonte.render(f"{num}", True, (255,255,255))
        #window.blit(num_random, (600,600))


        draw.rect(window, (0, 200, 100), (490, 250,300,100))
        draw.rect(window, (0, 0, 0), (490, 250,300,100),5)
        
        nova_tent = fonte.render(f"Tentar novamente?", True, (255,255,255))
        window.blit(nova_tent, (525,280))
        
        


        

        if numero_escolhido < num:
            dica = fonte.render(f"O número é maior que {numero_escolhido}", True, (255,255,255))
            window.blit(dica, (500,150))
            
        if numero_escolhido > num:
            dica = fonte.render(f"O número é menor que {numero_escolhido}", True, (255,255,255))
            window.blit(dica, (500,150))

        tentativas_texto = fonte.render(f"Tentativas: {tentativas}", True, (255,255,255))
        window.blit(tentativas_texto, (10,10))


        num_usados = fonte.render(f"Números usados:", True, (255,255,255))
        window.blit(num_usados, (10,70))
        num_usados_lista = fonte.render(f"{menor_num}", True, (255,0,0))
        window.blit(num_usados_lista, (160,120))
        num_usados = fonte.render(f"{maior_num}", True, (0,255,0))
        window.blit(num_usados, (10,120))
        numa = fonte.render("< X <", True, (255,255,255))
        window.blit(numa, (80, 120))

        texto_vic = fonte.render(f"parabens voce ganhou, o numero era {num}", True, (0,255,0))

        if numero_escolhido == num and timer == 0:
            timer = 300

        if timer > 0:
            window.blit(texto_vic, (370,500))
            timer -=1
        
        if timer == 1:
            reset_jogo()




    if escolha == 1:

        

        
                
        
            


        num_texto = fonte.render(f"Seu número é {numero_escolhido}", True, (255,255,255))
        window.blit(num_texto, (500,50))

        num_random = fonte.render(f"O PC acha que é: {chute_pc}", True, (255,255,255))
        window.blit(num_random, (600,600))


        draw.rect(window, (0, 200, 100), (490, 250,300,100))
        draw.rect(window, (0, 0, 0), (490, 250,300,100),5)
        
        nova_tent = fonte.render(f"Tentar novamente?", True, (255,255,255))
        window.blit(nova_tent, (525,280))
        
        


        

        if chute_pc < numero_escolhido:
            dica = fonte.render(f"O número é maior que {chute_pc}", True, (255,255,255))
            window.blit(dica, (500,150))
            
        if chute_pc > numero_escolhido:
            dica = fonte.render(f"O número é menor que {chute_pc}", True, (255,255,255))
            window.blit(dica, (500,150))

        tentativas_texto = fonte.render(f"Tentativas: {tentativas}", True, (255,255,255))
        window.blit(tentativas_texto, (10,10))


        num_usados = fonte.render(f"Números usados:", True, (255,255,255))
        window.blit(num_usados, (10,70))
        num_usados_lista = fonte.render(f"{menor_num}", True, (255,0,0))
        window.blit(num_usados_lista, (160,120))
        num_usados = fonte.render(f"{maior_num}", True, (0,255,0))
        window.blit(num_usados, (10,120))
        numa = fonte.render("< X <", True, (255,255,255))
        window.blit(numa, (80, 120))

        texto_vic = fonte.render(f"o pc ganhou, o numero era {numero_escolhido}, escolha um novo", True, (0,255,0))

        if chute_pc == numero_escolhido and timer == 0:
            timer = 300

        if timer > 0:
            window.blit(texto_vic, (370,500))
            timer -=1
        
        if timer == 1:
            reset_jogo_pc()


    display.update()