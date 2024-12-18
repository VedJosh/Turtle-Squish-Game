# Turtle-Squish-Game
A simple game built with Python's turtle graphics library. In this game, you control a turtle (player) that must navigate across a screen filled with moving cars. The objective is to cross the road while avoiding collisions with the cars. Each time the player reaches the finish line, the level increases, and the game becomes more challenging.

# Features
Single-player game: Control the turtle using the keyboard.
Dynamic difficulty: The level increases as you successfully cross the road, making the game harder.
Moving cars: Avoid cars that move from right to left across the screen.
Game over: If the player collides with a car, the game ends.
Score display: Your current level is displayed at the top of the screen.

# Requirements
Python 3.x
turtle module (this comes pre-installed with Python)

# How to Play
Run the game script:

bash
Copy code
python3 main_game.py

# Controls:

Use the Up Arrow key to move the turtle forward.

# Objective:

The goal is to make the turtle cross the road to the top of the screen. Each time the player successfully crosses, the level increases, and new cars will start moving.
Game Over:

The game ends if the player collides with any of the moving cars.

# Code Structure
Classes
Player (player.py): Represents the player turtle. It controls the movement and checks if the player has reached the finish line.
CarManager (car_manager.py): Handles the creation and movement of the cars that the player needs to avoid.
Scoreboard (scoreboard.py): Displays the current level on the screen and shows "GAME OVER" when the game ends.

# Game Logic
Car Movement: Cars are generated at random positions and move from the right side of the screen toward the left. As the game progresses, the speed of the cars increases.
Level Progression: Each time the player reaches the finish line, the level increases, and the player is sent back to the starting position.
Collision Detection: If the player collides with a car, the game ends.
# Example Files:
player.py: Contains the Player class that defines the player's turtle and movement.
car_manager.py: Contains the CarManager class that defines how cars are generated and moved.
scoreboard.py: Contains the Scoreboard class that displays the score (level) and handles game over logic.
main_game.py: The main script that runs the game, initializes all game components, and manages the game loop.
