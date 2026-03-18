import pygame
import sys
import random

pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cute Snake Game")

# 색상
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)       # 몸통 색
LIGHT_GREEN = (0, 255, 0) # 머리 색
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# FPS와 폰트
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# 🎮 뱀 & 음식 초기화 함수
def init_game():
    snake = [(300, 300)]
    snake_dir = (20, 0)
    food = (random.randrange(0, WIDTH, 20), random.randrange(0, HEIGHT, 20))
    score = 0
    return snake, snake_dir, food, score

# 🎨 여러 줄 메시지 출력
def draw_message_multi(lines):
    screen.fill(WHITE)
    for i, line in enumerate(lines):
        msg = font.render(line, True, BLACK)
        rect = msg.get_rect(center=(WIDTH//2, HEIGHT//2 - 20 + i*40))
        screen.blit(msg, rect)
    pygame.display.flip()

# 🎮 메인 게임 루프
def game_loop():
    snake, snake_dir, food, score = init_game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 방향키 조작
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != (0, 20):
                    snake_dir = (0, -20)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -20):
                    snake_dir = (0, 20)
                elif event.key == pygame.K_LEFT and snake_dir != (20, 0):
                    snake_dir = (-20, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-20, 0):
                    snake_dir = (20, 0)

        # 뱀 이동
        head_x = snake[0][0] + snake_dir[0]
        head_y = snake[0][1] + snake_dir[1]
        new_head = (head_x, head_y)
        snake.insert(0, new_head)

        # 음식 먹기
        if new_head == food:
            score += 1
            food = (random.randrange(0, WIDTH, 20), random.randrange(0, HEIGHT, 20))
        else:
            snake.pop()

        # 벽 충돌
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            running = False

        # 자기 몸 충돌
        if new_head in snake[1:]:
            running = False

        # 화면 그리기
        screen.fill(WHITE)

        # 🐍 뱀 그리기 (머리 밝게, 몸통 어둡게, 동그랗게)
        for i, segment in enumerate(snake):
            color = LIGHT_GREEN if i == 0 else GREEN
            pygame.draw.circle(screen, color, (segment[0]+10, segment[1]+10), 10)

        # 🍎 음식
        pygame.draw.rect(screen, RED, (*food, 20, 20))

        # 🏆 점수 표시
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)

    return score

# 🎬 시작 화면
while True:
    draw_message_multi(["Press ENTER to Start"])
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

    final_score = game_loop()  # 게임 실행

    # 게임 오버 화면 (줄바꿈 메시지)
    draw_message_multi([f"Game Over! Score: {final_score}", "Press ENTER to Restart"])
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False  # 다시 게임 시작