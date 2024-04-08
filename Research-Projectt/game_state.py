#Game Logic Separation: game_state.py is designed to encapsulate the game's logic, such as managing scenarios, 
# tracking points, and controlling game flow. This file contains the GameState class and its methods, 
# which are purely Python-based and are meant to be used within the Python environment 
# (i.e., called from main.py or other Python modules).


from scenarios import scenarios  # Make sure to import scenarios if they're used within this class


class GameState:
    def __init__(self):
        self.reset_game_state()

    def reset_game_state(self):
        # Initialize or reset the game state
        self.points = {"Academic": 0, "Work": 0, "Well-being": 0}
        self.current_scenario_index = 0
        # Assuming scenarios is a list of dictionaries each representing a scenario
        self.scenarios = scenarios[:]  # Create a shallow copy of the scenarios to avoid modifying the original
        for scenario in self.scenarios:
            scenario["selected_option"] = None
            scenario["initial_choice"] = None

    def update_points(self, category, points_added, scenario_index, option_index):
        # Retrieve the current scenario
        scenario = self.scenarios[scenario_index]

        # Check and update the initial choice and selected option
        if scenario.get('initial_choice') is None or scenario.get('initial_choice') != option_index:
            # Deduct points if changing choice after initial selection
            if scenario.get('initial_choice') is not None:
                prev_option = scenario["options"][scenario.get('initial_choice')]
                self.points[prev_option["category"]] -= prev_option["points"]
            scenario['initial_choice'] = option_index  # Update the initial choice
            self.points[category] += points_added  # Add points for the new choice

        # Update the selected option to reflect the current choice
        scenario['selected_option'] = option_index

        print(f"Updated {category} by {points_added} points. Total in {category}: {self.points[category]}")
        return self.points

    def advance_scenario(self):
        # Proceed to the next scenario, or handle game end if there are no more scenarios
        self.current_scenario_index += 1
        if self.current_scenario_index >= len(self.scenarios):
            # All scenarios have been completed
            return "end"
        else:
            return "continue"

    def revert_scenario(self):
        # Go back to the previous scenario if possible
        if self.current_scenario_index > 0:
            self.current_scenario_index -= 1