import pygame

pygame.init()

FPS = 60

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

running = True

dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
bullet_pos = pygame.Vector2(-100,-100)
target_pos = pygame.Vector2(-100,-100)

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                target_pos = pygame.Vector2(pygame.mouse.get_pos())
                bullet_pos = pygame.Vector2(player_pos)
    pygame.draw.circle(screen, "red", player_pos, 40)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if player_pos.y >= 300 * dt: player_pos.y -= 300 * dt
    if key[pygame.K_s]:
        if player_pos.y <= screen.get_height() - 300 * dt: player_pos.y += 300 * dt
    if key[pygame.K_a]:
        if player_pos.x >= 300 * dt: player_pos.x -= 300 * dt
    if key[pygame.K_d]:
        if player_pos.x <= screen.get_width() - 300 * dt: player_pos.x += 300 * dt
        
    if target_pos != bullet_pos:
        bullet_pos += dt * 600 * (target_pos - bullet_pos).normalize()
        pygame.draw.circle(screen, "green", bullet_pos, 20)
        if int(bullet_pos[0]) in range(int(target_pos[0])-10,int(target_pos[0])+10) and int(bullet_pos[1]) in range(int(target_pos[1])-10,int(target_pos[1])+10):
            bullet_pos = target_pos
    else:
        target_pos = bullet_pos = -100, -100

    pygame.display.flip()

    dt = clock.tick(FPS) / 1000

pygame.quit()