import pygame
from img_transformation import get_image
import numpy as np


# 변수 선언 및 초기화
WIDTH = 1100
HEIGHT = 1000
FPS = 30
TILESIZE = 15

# 색 지정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# binary image 얻기
# get_image 함수의 파라미터 : 원하는 이미지 파일, 픽셀 수 감소 비율, erosion 반복 횟수
# 원본 이미지의 크기에 따라 축소 비율이나 적절한 erosion 반복 횟수가 다름
image = get_image('image/pikachu.png', 0.07, 5)   # 1. 피카츄
# image = get_image('image/dora.png', 0.15, 1)      # 2. 도라에몽
# image = get_image('image/ryan.jpg', 0.13, 3)      # 3. 라이언


H, W = image.shape

# 정답을 리스트 형태로 저장
answer = image.tolist()


# Rect 객체 배열
rects = [[pygame.Rect((x*TILESIZE + 30, y*TILESIZE + 150),(TILESIZE, TILESIZE)) for x in range(W)] for y in range(H)]

# 사각형 클릭 여부
clicked = [[1]*W for _ in range(H)]
# clicked = answer

# 초기화
pygame.init()

# 스크린 크기
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 제목
pygame.display.set_caption("Nonogram")


# Clock의 객체
clock = pygame.time.Clock()

# 배경을 흰색으로 채움
screen.fill(WHITE)

# 가로 및 세로 숫자 힌트의 폰트 설정
hint_font = pygame.font.SysFont( "arial", TILESIZE)

# 정답 시 출력할 문자의 폰트 설정
correction_font = pygame.font.SysFont( "arial", 50)
correction = correction_font.render("Congratulation!!!", True, (0,0,255))


# 가로줄 힌트 계산
for y in range(H):
    cnt = 0
    count_rows = []
    for x in range(W):
        if image[y,x] == 0:
            cnt += 1
        elif cnt != 0:
            count_rows.append(str(cnt) + '   ')
            cnt = 0
        if x == W-1 and cnt != 0:
            count_rows.append(str(cnt) + '   ')
            cnt = 0

    if not count_rows:
        hint = hint_font.render("0", True, (0,0,0))
    else:
        hint = hint_font.render("".join(count_rows), True, (0,0,0))
    screen.blit(hint, (W*TILESIZE + 40, y*TILESIZE + 150))


# 세로줄 힌트 계산
for x in range(W):
    cnt = 0
    count_cols = []
    for y in range(H):
        if image[y,x] == 0:
            cnt += 1
        elif cnt != 0:
            count_cols.append(str(cnt))
            cnt = 0
        if y == H-1 and cnt != 0:
            count_cols.append(str(cnt))
            cnt = 0

    for k in range(len(count_cols)):
        hint = hint_font.render(count_cols[k], True, (0,0,0))
        screen.blit(hint, (30 + x*TILESIZE, 120 + (k + 1 - len(count_cols))*TILESIZE))

    if not count_cols:
        hint = hint_font.render("0", True, (0, 0, 0))
        screen.blit(hint, (30 + x*TILESIZE, 120))


running = True
while running:
    # FPS 지정
    clock.tick(FPS)

    # 사각형 그리기
    for y in range(H):
        for x in range(W):
            if clicked[y][x] == 1:
                pygame.draw.rect(screen, WHITE, rects[y][x])
                pygame.draw.rect(screen, BLACK, rects[y][x], 1)
            else:
                pygame.draw.rect(screen, BLACK, rects[y][x])


    # 마우스 클릭 이벤트
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # 마우스 클릭 이벤트
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for y in range(H):
                for x in range(W):
                    if rects[y][x].collidepoint(event.pos):
                        clicked[y][x] = 0 if clicked[y][x] == 1 else 1

    # 정답과 일치할 경우
    if clicked == answer:
        screen.blit(correction,(300,80))

    pygame.display.update()