import pygame
import os

pygame.font.init()
pygame.mixer.init()

# These lines of code are setting up the game window with a width of 900 pixels and a height of 500
# pixels using the `pygame.display.set_mode()` function. The `pygame.display.set_caption()` function
# is used to set the title of the game window to "Space Shooter Game!".
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# `BORDER` is creating a rectangular object using the `pygame.Rect()` function. It is positioned in
# the middle of the game window horizontally (`WIDTH//2 - 5`), starting from the top of the window
# (`0`), with a width of `10` pixels and a height equal to the height of the game window (`HEIGHT`).
# This rectangle is used as a visual divider between the two sides of the game window, where the two
# spaceships can move.
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound("Assets/Grenade+1.mp3")
BULLET_FIRE_SOUND = pygame.mixer.Sound("Assets/Gun+Silencer.mp3")

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# `YELLOW_HIT` and `RED_HIT` are custom events created using the `pygame.USEREVENT` constant.
# `pygame.USEREVENT` is a constant that represents the start of a range of custom event types that can
# be used in a pygame program. By adding 1 to `pygame.USEREVENT`, we create a new custom event type
# that can be used in our program. These custom events are used to detect when a bullet fired by one
# spaceship collides with the other spaceship, so that we can reduce the health of the hit spaceship.
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# These lines of code are loading and transforming images to be used in the game.
# `YELLOW_SPACESHIP_IMAGE` and `RED_SPACESHIP_IMAGE` are loading images of yellow and red spaceships
# respectively from the "Assets" folder. These images are then scaled to the size of `SPACESHIP_WIDTH`
# and `SPACESHIP_HEIGHT` using `pygame.transform.scale()`. They are also rotated by 90 and 270 degrees
# respectively using `pygame.transform.rotate()`. The resulting images are stored in
# `YELLOW_SPACESHIP` and `RED_SPACESHIP` variables.
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png")
)
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    90,
)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    270,
)

SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT)
)


def draw_window(
    red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, bg_x
):
    """
    This function draws a window with two spaceships, their health bars, and their bullets.

    Args:
      red: The object representing the red spaceship, with attributes such as its position on the screen
    (x and y coordinates) and its movement speed.
      yellow: The yellow spaceship object, which has attributes for its position and movement.
      red_bullets: A list of rectangles representing the bullets fired by the red spaceship.
      yellow_bullets: A list of rectangles representing the bullets fired by the yellow spaceship.
      red_health: The current health of the red spaceship.
      yellow_health: The current health of the yellow spaceship.
    """

    SPACE_FLIP = pygame.transform.flip(SPACE, True, False)
    WIN.blit(SPACE_FLIP, (bg_x + WIDTH * 2, 0))
    SPACE_FLIP = pygame.transform.flip(SPACE_FLIP, True, False)

    WIN.blit(SPACE_FLIP, (bg_x + WIDTH, 0))
    SPACE_FLIP = pygame.transform.flip(SPACE_FLIP, True, False)
    WIN.blit(SPACE_FLIP, (bg_x, 0))

    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    """
    This function handles the movement of a yellow ship based on the keys pressed by the user.

    Args:
      keys_pressed: This parameter is a list of boolean values that represent which keys are currently
    being pressed on the keyboard.
      yellow: This parameter represents the yellow player in the game. The function is using this parameter to
    update the position of the yellow player based on the keys pressed by the user.
    """
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if (
        keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15
    ):  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    """
    This function handles the movement of a red ship based on the keys pressed by the user.

    Args:
      keys_pressed: This parameter is a list of boolean values that represent which keys are currently
    being pressed on the keyboard.
      red: This parameter is representing the red player in the game. It
    has attributes such as x and y coordinates, width, and height, which are used to determine
    its position and movement on the screen.
    """
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    """
    This function handles the movement and collision detection of bullets between two players in a game.

    Args:
      yellow_bullets: A list of bullets fired by the yellow player.
      red_bullets: A list of bullets belonging to the red player.
      yellow: This parameter refers to the yellow player's
    character in a game.
      red: This parameter refers to the position and size of the
    red player's character in a game. It is used to check for collisions with yellow bullets.
    """
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    """
    This function draws a text on the screen using a specific font and color, updates the display, and
    delays for 5 seconds.

    Args:
      text: The text that will be displayed on the screen as the winner.
    """
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(
        draw_text,
        (
            WIDTH / 2 - draw_text.get_width() / 2,
            HEIGHT / 2 - draw_text.get_height() / 2,
        ),
    )
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    """
    This function runs the main game loop for a two-player spaceship shooting game.
    """
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    bg_x = 0  # Initial position of the background image

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # This code block is checking if the left or right control key is pressed and if the
                # number of bullets fired by the corresponding player is less than the maximum number
                # of bullets allowed (`MAX_BULLETS`). If these conditions are met, a new bullet is
                # created using the `pygame.Rect()` function with a width of 10 pixels and a height of
                # 5 pixels. The position of the bullet is determined based on the position of the
                # corresponding player's spaceship (`yellow` or `red`). The bullet is then added to
                # the corresponding list of bullets (`yellow_bullets` or `red_bullets`). Finally, a
                # gunshot sound effect is played using the `BULLET_FIRE_SOUND` sound object.
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width,
                        yellow.y + yellow.height // 2 - 2,
                        10,
                        5,
                    )
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            # These lines of code are checking if a custom event has occurred. The custom events are
            # `RED_HIT` and `YELLOW_HIT`, which are created using the `pygame.USEREVENT` constant.
            # These events are triggered when a bullet fired by one spaceship collides with the other
            # spaceship. If the `RED_HIT` event occurs, the health of the red spaceship is reduced by
            # 1 and a bullet hit sound effect is played. If the `YELLOW_HIT` event occurs, the health
            # of the yellow spaceship is reduced by 1 and a bullet hit sound effect is played.
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        # The below code is checking the health of two players (red and yellow) in a game and
        # determining the winner based on whose health is greater than zero. If one player's health
        # reaches zero or below, the code sets the winner_text variable to the name of the other
        # player and calls the draw_winner function to display the winner on the screen. The break
        # statement is used to exit the loop once a winner has been determined.
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        bg_x -= 1  # Update the position of the background image

        # Reset the position of the background image to the right side of the screen
        if bg_x <= -WIDTH * 2:
            bg_x = 0

        draw_window(
            red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, bg_x
        )

    main()


if __name__ == "__main__":
    main()
