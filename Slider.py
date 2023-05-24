import pygame


class Slider:
    def __init__(self, x, y, width, height, min_value, max_value, initial_value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.slider_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.slider_pos = self.calculate_slider_pos()

    def calculate_slider_pos(self):
        range_value = self.max_value - self.min_value
        pos = (self.value - self.min_value) / \
            range_value * (self.width - self.height)
        return self.x + pos

    def update_value(self, mouse_pos):
        if self.slider_rect.collidepoint(mouse_pos):
            pos = mouse_pos[0]
            pos = max(pos, self.x)
            pos = min(pos, self.x + self.width - self.height)
            self.slider_pos = pos
            range_value = self.max_value - self.min_value
            self.value = self.min_value + \
                ((pos - self.x) / (self.width - self.height)) * range_value

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.slider_rect)
        pygame.draw.circle(screen, (100, 100, 100), (int(
            self.slider_pos), int(self.y + self.height/2)), int(self.height/2))
