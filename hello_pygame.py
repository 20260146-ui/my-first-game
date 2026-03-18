import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("My First Pygame")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()

# FPS 표시용 폰트
font = pygame.font.SysFont(None, 30)

# 원의 초기 위치
circle_x = 400
circle_y = 400
circle_radius = 60
circle_width = 40
move_speed = 3  # 원 이동 속도

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 상태 확인
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= move_speed
    if keys[pygame.K_RIGHT]:
        circle_x += move_speed
    if keys[pygame.K_UP]:
        circle_y -= move_speed
    if keys[pygame.K_DOWN]:
        circle_y += move_speed

    # 경계 처리: 화면 밖으로 나가지 않도록
    min_pos = circle_radius  # 원 중심이 최소 위치
    max_pos = 800 - circle_radius  # 원 중심이 최대 위치
    circle_x = max(min_pos, min(circle_x, max_pos))
    circle_y = max(min_pos, min(circle_y, max_pos))
    # 화면 채우기
    screen.fill(BLACK)

    # 원 그리기
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius, circle_width)

    # FPS 계산
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {int(fps)}", True, WHITE)  # 흰색으로 표시

    # FPS 화면에 표시
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)  # FPS를 60으로 설정
    
pygame.quit()
sys.exit()