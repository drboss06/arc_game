import pygame
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 800
HEIGHT = 600

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Game Menu")

# Define Button class
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def check_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.color = self.hover_color
        else:
            self.color = WHITE

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

# Define button actions
def start_game():
    print("Starting the game!")

def settings():
    print("Opening settings!")

# Create buttons
start_button = Button("Start Game", 300, 200, 200, 50, WHITE, BLACK, start_game)
settings_button = Button("Settings", 300, 300, 200, 50, WHITE, BLACK, settings)

# -------- Main Program -----------
def main():
    # --- Main event loop
    while True:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Be IDLE friendly
                sys.exit()  # exit the program
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                start_button.check_click(pos)
                settings_button.check_click(pos)

        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)

        # Draw the buttons
        start_button.draw()
        settings_button.draw()

        # Check for hover
        pos = pygame.mouse.get_pos()
        start_button.check_hover(pos)
        settings_button.check_hover(pos)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

if __name__ == "__main__":
    main()