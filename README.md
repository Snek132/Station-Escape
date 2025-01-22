README
File Structure
The game consists of a single Python script that implements the entire gameplay. Below is a brief overview of the key sections and functions within the file:

  
  Imports

    The script begins with importing necessary modules:
      random: For generating random outcomes.
      time: To create delays in text output for dramatic effect.
      sys: For system-specific parameters and functions.
  

  Game State

    Defines the initial state of the game, including:
    inventory: A list to store collected items.
    game_state: A dictionary holding:
    oxygen_level
    ethics_score
    location
    endings: Different narrative endings based on player choices.
 
  
  Functions

    print_slow(text): Prints text character by character for a dramatic effect.
    end_game(ending_type): Manages game endings and displays corresponding messages.
    examine_room(): Allows players to explore the starting room and collect items.
    clear_debris(): Clears debris using tools found in the game.
    explore_further(): Handles exploration leading to escape pods.
    repair_terminal(): Repairs the communication terminal and presents choices.
    follow_crew_member(): Follows a crew member's advice for survival.
    navigate_escape_pods(): Concludes the game based on the player's final choice.
    investigate_core(): Investigates the malfunctioning AI core.
    start_game(): Initializes the game and presents the first choices.

    
Running the Game

    Open a terminal or command prompt.
    Navigate to the directory containing the script.
    Execute the following command:
    python allcode.py


Gameplay

    Players will interact with the game by making choices that lead to various outcomes.
        The game can be exited at any time by typing "stop".
