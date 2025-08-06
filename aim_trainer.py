import pygame
import random
import math
import time
import json
import os

pygame.init()

# — Configuration —
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TOP_BAR_HEIGHT = 50
BG_COLOR = (10, 30, 50)
BAR_COLOR = (200, 200, 200)
FONT = pygame.font.SysFont("arial", 24)
LIVES = 3
SPAWN_INTERVAL_MS = 400
PADDING = 30

# Optional sound effects (place hit.wav & miss.wav in same folder)
try:
    HIT_SFX = pygame.mixer.Sound("hit.wav")
    MISS_SFX = pygame.mixer.Sound("miss.wav")
except FileNotFoundError:
    HIT_SFX = MISS_SFX = None

# High‐score persistence
HS_FILE = "highscore.json"
def load_highscore():
    if os.path.exists(HS_FILE):
        with open(HS_FILE, "r") as f:
            return json.load(f).get("highscore", 0)
    return 0

def save_highscore(score):
    with open(HS_FILE, "w") as f:
        json.dump({"highscore": score}, f)

# — Target Class —
class Target:
    MAX_RADIUS = 30
    GROWTH_RATE = 0.2

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.radius = 0
        self.shrinking = False

    def update(self):
        if not self.shrinking and self.radius >= self.MAX_RADIUS:
            self.shrinking = True
        self.radius += -self.GROWTH_RATE if self.shrinking else self.GROWTH_RATE

    def draw(self, surface):
        # Outer red ring
        pygame.draw.circle(surface, (255, 0, 0), (self.x, self.y), int(self.radius))
        # Inner white ring
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), int(self.radius * 0.8))

    def is_expired(self):
        return self.radius <= 0

    def hit_test(self, pos):
        dx, dy = pos[0] - self.x, pos[1] - self.y
        return math.hypot(dx, dy) <= self.radius

# — Main Game Class —
class AimTrainer:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Aim Trainer Reloaded")
        self.clock = pygame.time.Clock()
        self.targets = []
        self.hits = 0
        self.shots = 0
        self.misses = 0
        self.start_time = time.time()
        self.highscore = load_highscore()
        pygame.time.set_timer(pygame.USEREVENT, SPAWN_INTERVAL_MS)

    def spawn_target(self):
        x = random.randint(PADDING, SCREEN_WIDTH - PADDING)
        y = random.randint(PADDING + TOP_BAR_HEIGHT, SCREEN_HEIGHT - PADDING)
        self.targets.append(Target(x, y))

    def draw_top_bar(self):
        elapsed = time.time() - self.start_time
        pygame.draw.rect(self.screen, BAR_COLOR, (0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT))
        # Time
        txt_time = FONT.render(f"Time: {elapsed:.1f}s", True, (0, 0, 0))
        # Speed
        speed = round(self.hits / (elapsed or 1), 1)
        txt_speed = FONT.render(f"Speed: {speed} hits/s", True, (0, 0, 0))
        # Hits & Lives
        txt_hits = FONT.render(f"Hits: {self.hits}", True, (0, 0, 0))
        txt_lives = FONT.render(f"Lives: {LIVES - self.misses}", True, (0, 0, 0))

        self.screen.blit(txt_time, (10, 10))
        self.screen.blit(txt_speed, (200, 10))
        self.screen.blit(txt_hits, (450, 10))
        self.screen.blit(txt_lives, (650, 10))

    def game_over_screen(self):
        elapsed = time.time() - self.start_time
        accuracy = round(self.hits / (self.shots or 1) * 100, 1)

        # Save high score if beaten
        if self.hits > self.highscore:
            save_highscore(self.hits)
            self.highscore = self.hits

        messages = [
            "Game Over!",
            f"Hits: {self.hits}   Accuracy: {accuracy}%",
            f"High Score: {self.highscore}"
        ]

        self.screen.fill(BG_COLOR)
        for idx, line in enumerate(messages):
            surf = FONT.render(line, True, (255, 255, 255))
            x = (SCREEN_WIDTH - surf.get_width()) // 2
            y = 150 + idx * 100
            self.screen.blit(surf, (x, y))

        pygame.display.flip()
        # Wait for quit or keypress
        while True:
            for ev in pygame.event.get():
                if ev.type in (pygame.QUIT, pygame.KEYDOWN):
                    pygame.quit()
                    return

    def run(self):
        running = True
        while running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
                elif ev.type == pygame.USEREVENT:
                    self.spawn_target()
                elif ev.type == pygame.MOUSEBUTTONDOWN:
                    self.shots += 1
                    clicked = False
                    for tgt in self.targets[:]:
                        if tgt.hit_test(ev.pos):
                            self.targets.remove(tgt)
                            self.hits += 1
                            if HIT_SFX: HIT_SFX.play()
                            clicked = True
                            break
                    if not clicked:
                        self.misses += 1
                        if MISS_SFX: MISS_SFX.play()

            # Update targets & check for expires
            for tgt in self.targets[:]:
                tgt.update()
                if tgt.is_expired():
                    self.targets.remove(tgt)
                    self.misses += 1

            # If out of lives → end
            if self.misses >= LIVES:
                self.game_over_screen()
                running = False

            # Draw everything
            self.screen.fill(BG_COLOR)
            for tgt in self.targets:
                tgt.draw(self.screen)
            self.draw_top_bar()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    AimTrainer().run()
