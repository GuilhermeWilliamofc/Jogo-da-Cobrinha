import pygame
import random
from emoji import emojize

pygame.init()
pygame.display.set_caption(emojize('Snake Game :red_apple: :snake: By Gw'))
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores
cinza = (150, 150, 150)
roxo = (128, 0, 128)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

# parametros da cobrinha
tamanho_quadrado = 10
velocidade_atualizacao_cobrinha = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, roxo, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Pontos {pontuacao}", True, branco)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels_cobra = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(cinza)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)

        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        pixels_cobra.append([x, y])
        if len(pixels_cobra) > tamanho_cobra:
            del pixels_cobra[0]

        for pixel in pixels_cobra[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        desenhar_cobra(tamanho_quadrado, pixels_cobra)
        desenhar_pontuacao(tamanho_cobra - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_atualizacao_cobrinha)

rodar_jogo()


