
import pygame
import random
import sys

# تهيئة مكتبة pygame
pygame.init()

# إعداد شاشة اللعبة
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("لعبة صيد الحروف")

# الألوان
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# الخطوط
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# الحروف الأبجدية
letters = ['أ', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ']
score = 0
speed = 5

# الحرف الحالي والموقع
current_letter = random.choice(letters)
letter_x = random.randint(50, WIDTH - 50)
letter_y = -50

# المؤقت
clock = pygame.time.Clock()

# الوظائف
def draw_text(text, font, color, x, y):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def reset_letter():
    global current_letter, letter_x, letter_y
    current_letter = random.choice(letters)
    letter_x = random.randint(50, WIDTH - 50)
    letter_y = -50

# الوظيفة الرئيسية
def main():
    global letter_x, letter_y, score, speed
    running = True
    
    while running:
        screen.fill(WHITE)

        # عرض الحرف المطلوب
        draw_text("صيد الحرف: " + current_letter, font, BLUE, 50, 50)
        draw_text(f"النتيجة: {score}", small_font, GREEN, WIDTH - 200, 50)

        # تحريك الحرف للأسفل
        letter_y += speed
        draw_text(current_letter, font, RED, letter_x, letter_y)

        # إذا خرج الحرف من الشاشة
        if letter_y > HEIGHT:
            reset_letter()

        # معالجة الأحداث
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if letter_x - 50 < mouse_x < letter_x + 50 and letter_y - 50 < mouse_y < letter_y + 50:
                    score += 1
                    speed += 0.5  # زيادة السرعة مع كل حرف صحيح
                    reset_letter()

        # تحديث الشاشة
        pygame.display.flip()
        clock.tick(30)

# بدء اللعبة
if __name__ == "__main__":
    main()
