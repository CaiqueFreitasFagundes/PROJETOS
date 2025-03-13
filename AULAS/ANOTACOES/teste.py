import pygame
import math

# Configurações iniciais
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAVITY = 0.3  # Gravidade aumentada
FRICTION = 0.98  # Fator de atrito para a bola
BOUNCE_DAMPING = 0.8  # Fator de amortecimento para quicar várias vezes

# Inicializa o pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Configuração do quadrado rotatório
square_size = 300
angle = 0
cx, cy = WIDTH // 2, HEIGHT // 2

# Configuração da bola
ball_radius = 15
ball_x, ball_y = cx, cy
ball_vx, ball_vy = 2, -7  # Velocidades iniciais

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Rotação do quadrado
    angle += 1  # Incrementa o ângulo de rotação
    rad = math.radians(angle)
    cos_a, sin_a = math.cos(rad), math.sin(rad)
    
    # Define os vértices do quadrado rotacionado
    half = square_size // 2
    corners = [
        (-half, -half), (half, -half), (half, half), (-half, half)
    ]
    rotated_corners = [
        (cx + x * cos_a - y * sin_a, cy + x * sin_a + y * cos_a)
        for x, y in corners
    ]
    pygame.draw.polygon(screen, BLUE, rotated_corners, 2)
    
    # Atualiza posição da bola
    ball_vy += GRAVITY  # Aplica gravidade
    ball_x += ball_vx
    ball_y += ball_vy
    
    # Verifica colisão com o quadrado rotatório
    for i in range(4):
        x1, y1 = rotated_corners[i]
        x2, y2 = rotated_corners[(i + 1) % 4]
        
        # Vetor da aresta
        edge_dx = x2 - x1
        edge_dy = y2 - y1
        
        # Vetor bola para vértice
        to_ball_x = ball_x - x1
        to_ball_y = ball_y - y1
        
        # Projeção do vetor bola sobre a aresta
        edge_length = math.sqrt(edge_dx**2 + edge_dy**2)
        dot_product = (to_ball_x * edge_dx + to_ball_y * edge_dy) / edge_length
        
        # Ponto mais próximo na borda
        closest_x = x1 + (dot_product / edge_length) * edge_dx
        closest_y = y1 + (dot_product / edge_length) * edge_dy
        
        # Distância da bola ao ponto mais próximo
        dist = math.sqrt((ball_x - closest_x) ** 2 + (ball_y - closest_y) ** 2)
        
        if dist <= ball_radius:  # Colisão
            normal_x = edge_dy / edge_length
            normal_y = -edge_dx / edge_length
            dot = ball_vx * normal_x + ball_vy * normal_y
            ball_vx -= 2 * dot * normal_x
            ball_vy -= 2 * dot * normal_y
            ball_vx *= FRICTION
            ball_vy *= FRICTION
            ball_vy *= -BOUNCE_DAMPING  # Permite que a bola continue quicando
    
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
