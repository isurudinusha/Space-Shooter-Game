# Space Shooter Game

This is a two-player spaceship shooting game built using the Pygame library. The objective of the game is to eliminate the opponent's spaceship by firing bullets and reducing their health to zero.

## Gameplay

- Each player controls a spaceship, one in yellow color and the other in red color.
- The yellow spaceship is controlled using the **WASD** keys (W for up, A for left, S for down, D for right), and the red spaceship is controlled using the **arrow keys** (up for up, left for left, down for down, right for right).
- Press the **left control (LCTRL)** key to fire bullets from the yellow spaceship, and press the **right control (RCTRL)** key to fire bullets from the red spaceship.
- Each player can fire a maximum of **3 bullets** at a time.
- The game window is divided by a vertical border, allowing the spaceships to move on their respective sides.

## Features

- Health bars: The current health of each spaceship is displayed as a numerical value at the top of the screen.
- Bullets: Bullets fired by each spaceship are displayed as rectangles on the screen.
- Collision detection: When a bullet fired by one spaceship collides with the other spaceship, the health of the hit spaceship is reduced by 1.
- Sound effects: Sound effects are played when a bullet is fired and when a spaceship is hit.
- Background animation: The game window features a scrolling space background to create a dynamic visual effect.

## How to Run

1. Make sure you have Python installed on your system (version 3.7 or later).
2. Install the Pygame library by running the following command: `pip install pygame`
3. Clone this repository or download the source code files.
4. Open a terminal or command prompt and navigate to the project directory.
5. Run the game by executing the following command: `main.py`
6. The game window will open, and you can start playing!

## Dependencies

- Pygame library: This game relies on the Pygame library for handling graphics, sound, and user input. Make sure to install Pygame before running the game.

## Acknowledgments

This game is inspired by classic space shooter games and was developed as a learning project using the Pygame library.

Feel free to modify and customize the game according to your preferences. Have fun playing!
