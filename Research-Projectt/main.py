# The entry point of the game.
# It coordinates the flow between different modules.
# This file will call functions from other modules based on the game's progress.
# When you decorate a Python function with @eel.expose, 
# you're telling Eel, "Hey, I want this function to be accessible from my JavaScript code." 
# This is crucial for the interactivity of Eel applications, 
# allowing your frontend (JavaScript) to interact with your backend (Python) dynamically.

import eel
import sys  # Import sys module
import json
from game_state import GameState

# Create an instance of GameState
game_state = GameState()

# Global variable to track points
points = {"Academic": 0, "Work": 0, "Well-being": 0}
current_scenario_index = 0

# Initialize the Eel application
eel.init('web')

@eel.expose
def perform_action(data):
    print(f"Received data: {data}")
    # Placeholder for actions based on received data
    return "Data processed"

@eel.expose
def start_new_game():
    game_state.reset_game_state()  # Reset the game state for a new game
    eel.change_page("character_creation.html")  # Navigate to character creation page

@eel.expose
def process_character_creation(character_data):
    print("Character Created:", character_data)
    start_game_scenarios()  # Begin the game scenarios
    # Optionally, handle character data as needed

@eel.expose
def update_points(category, points_added, scenario_index, option_index):
    points = game_state.update_points(category, points_added, scenario_index, option_index)
    # Print updated points for debugging
    print(f"Updated {category} by {points_added} points. Total in {category}: {points[category]}")
    
    return json.dumps(points)  # Return updated points as JSON string

@eel.expose       
def start_game_scenarios():
     # Get current scenario details
     scenario = game_state.scenarios[game_state.current_scenario_index]
     selected_option = scenario.get("selected_option", -1)
     eel.displayScenario(scenario["text"], scenario["options"], selected_option, game_state.current_scenario_index, scenario["image"])

@eel.expose
def next_scenario():
    result = game_state.advance_scenario()
    if result == "continue":
        start_game_scenarios()
    else:
        # If no more scenarios, show end screen
        points_json = json.dumps(game_state.points)
        eel.show_end_screen(points_json)

@eel.expose
def previous_scenario():
    game_state.revert_scenario()
    start_game_scenarios()

@eel.expose
def close_application(): # Function to close the application and window
    print("Closing application...")
    sys.exit(0)
    eel.close_window()
   
@eel.expose
def show_end_screen():
    points = {"Academic": 10, "Work": 5, "Well-being": 15}  # Example data
    points_json = json.dumps(points)
    eel.drawChart(points_json)
   
if __name__ == "__main__":
    eel.start('html/index.html', size=(800, 700))