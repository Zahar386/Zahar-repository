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
target_pos_x, target_pos_y = bullet_pos_x, bullet_pos_y = -100, -100

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                target_pos_x, target_pos_y = pygame.mouse.get_pos()
                bullet_pos_x, bullet_pos_y = player_pos
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
    

    if bullet_pos_x < target_pos_x:
        bullet_pos_x += 6
    elif bullet_pos_x > target_pos_x:
        bullet_pos_x -= 6
        
    if bullet_pos_x in range(int(target_pos_x)-10,int(target_pos_y)+10):
        bullet_pos_x = target_pos_x
        
    if bullet_pos_y < target_pos_y:
        bullet_pos_y += 6
    elif bullet_pos_y > target_pos_y:
        bullet_pos_y -= 6
        
    if bullet_pos_y in range(int(target_pos_y)-10,int(target_pos_y)+10):
        bullet_pos_y = target_pos_y
        
    if (target_pos_x, target_pos_y) != (bullet_pos_x, bullet_pos_y):
        pygame.draw.circle(screen, "green", (bullet_pos_x, bullet_pos_y), 20)
    else:
        target_pos_x, target_pos_y = bullet_pos_x, bullet_pos_y = -100, -100

    pygame.display.flip()

    dt = clock.tick(FPS) / 1000

pygame.quit()