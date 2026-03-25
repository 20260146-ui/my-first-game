import pygame
import sys
import math
from sprites import load_sprite

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Test")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# 색상
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 스프라이트
adventurer_img = load_sprite("adventurer", (80, 110))
sword_img = load_sprite("sword", (100, 100))

adventurer = adventurer_img.get_rect(topleft=(100, 100))
sword = sword_img.get_rect(center=(WIDTH//2, HEIGHT//2))

speed = 5
angle = 0

# -----------------------
# OBB 생성 함수 (크기 직접 지정 가능)
# -----------------------
def get_obb_points(center, width, height, angle):
    cx, cy = center
    w, h = width / 2, height / 2

    corners = [
        (-w, -h),
        ( w, -h),
        ( w,  h),
        (-w,  h)
    ]

    rad = math.radians(angle)
    result = []

    for x, y in corners:
        rx = x * math.cos(rad) - y * math.sin(rad)
        ry = x * math.sin(rad) + y * math.cos(rad)
        result.append((cx + rx, cy + ry))

    return result

# -----------------------
# SAT 충돌
# -----------------------
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def get_axes(points):
    axes = []
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i+1) % len(points)]

        edge = (p2[0] - p1[0], p2[1] - p1[1])
        normal = (-edge[1], edge[0])

        length = math.hypot(normal[0], normal[1])
        if length != 0:
            normal = (normal[0]/length, normal[1]/length)

        axes.append(normal)
    return axes

def project(points, axis):
    dots = [dot(p, axis) for p in points]
    return min(dots), max(dots)

def sat_collision(p1, p2):
    axes = get_axes(p1) + get_axes(p2)

    for axis in axes:
        min1, max1 = project(p1, axis)
        min2, max2 = project(p2, axis)

        if max1 < min2 or max2 < min1:
            return False

    return True

# -----------------------
# 게임 루프
# -----------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # 이동
    if keys[pygame.K_LEFT]:
        adventurer.x -= speed
    if keys[pygame.K_RIGHT]:
        adventurer.x += speed
    if keys[pygame.K_UP]:
        adventurer.y -= speed
    if keys[pygame.K_DOWN]:
        adventurer.y += speed

    angle += 2

    # 중심
    a_center = adventurer.center
    s_center = sword.center

    # -----------------------
    # 1. Circle 충돌
    # -----------------------
    a_radius = adventurer.width // 2
    s_radius = sword.width // 2

    dx = a_center[0] - s_center[0]
    dy = a_center[1] - s_center[1]
    circle_hit = (dx*dx + dy*dy) < (a_radius + s_radius) ** 2

    # -----------------------
    # 2. AABB 충돌
    # -----------------------
    aabb_hit = adventurer.colliderect(sword)

    # -----------------------
    # 3. OBB 충돌
    # -----------------------
    # 아바타 (회전 없음)
    a_obb = get_obb_points(a_center, adventurer.width, adventurer.height, 0)

    # 소드 (크기 직접 조정: 가로40 세로100)
    s_obb = get_obb_points(s_center, 40, 100, -angle)

    obb_hit = sat_collision(a_obb, s_obb)

    # -----------------------
    # 배경 (하나라도 충돌하면 빨강)
    # -----------------------
    if circle_hit or aabb_hit or obb_hit:
        screen.fill(RED)
    else:
        screen.fill(WHITE)

    # -----------------------
    # 그리기
    # -----------------------
    screen.blit(adventurer_img, adventurer.topleft)

    rotated = pygame.transform.rotate(sword_img, angle)
    r_rect = rotated.get_rect(center=s_center)
    screen.blit(rotated, r_rect.topleft)

    # AABB
    pygame.draw.rect(screen, RED, adventurer, 2)
    pygame.draw.rect(screen, RED, sword, 2)

    # Circle
    pygame.draw.circle(screen, BLUE, a_center, a_radius, 2)
    pygame.draw.circle(screen, BLUE, s_center, s_radius, 2)

    # OBB
    pygame.draw.polygon(screen, GREEN, a_obb, 2)
    pygame.draw.polygon(screen, GREEN, s_obb, 2)

    # -----------------------
    # 텍스트
    # -----------------------
    screen.blit(font.render(f"Circle: {'HIT' if circle_hit else 'MISS'}", True, (0,0,0)), (10, 10))
    screen.blit(font.render(f"AABB: {'HIT' if aabb_hit else 'MISS'}", True, (0,0,0)), (10, 40))
    screen.blit(font.render(f"OBB: {'HIT' if obb_hit else 'MISS'}", True, (0,0,0)), (10, 70))

    pygame.display.flip()
    clock.tick(60)