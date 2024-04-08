var currentScenarioIndex = 0;
var selectedOptionIndex = -1; // -1 indicates no selection
var selectedOption = null;
var selectedCategory = null;
var selectedPoints = 0;


document.addEventListener('DOMContentLoaded', (event) => {

eel.expose(displayScenario);
function displayScenario(scenarioText, options, selectedOptionIndex, scenarioIndex, imageName) {
    document.getElementById('scenario-text').innerText = scenarioText;
    const imageElement = document.getElementById('scenario-image');
    imageElement.src = '../images/' + imageName;  // Update the image source based on the scenario
    currentScenarioIndex = scenarioIndex; // Update the current scenario index

    const optionsContainer = document.getElementById('options');
    optionsContainer.innerHTML = ''; // Clear previous options

    options.forEach(function(option, index) {
        var button = document.createElement('button');
        button.classList.add('learn-more'); // Apply the new style class
        button.innerText = option.text;
        button.onclick = function() { selectOption(option.category, option.points, button, index); };
        optionsContainer.appendChild(button);
    
        // Highlight the previously selected option logic remains the same
        if (index === selectedOptionIndex) {
            button.classList.add('active'); // Optionally adjust if needed
            selectedOption = button;  // Update the global selectedOption reference
        }
    });
}
});

function initGameScenarios() {
    eel.start_game_scenarios();  // Trigger Python to send scenario data
}



function selectOption(category, points, button, optionIndex) {
    // Store the selected option's details
    selectedCategory = category;
    selectedPoints = points;
    selectedOptionIndex = optionIndex;

    // Change button color
    if (selectedOption) {
        selectedOption.style.backgroundColor = "";  // Reset previous selection
    }
    button.style.backgroundColor = "#bbf4ed";  // Highlight new selection
    selectedOption = button;
}


function goBack() {
    eel.previous_scenario()();  // Move to the previous scenario
}

function goNext() {
    if (selectedOption) {
        // Correctly pass the current scenario index and the selected option index to Python
        eel.update_points(selectedCategory, selectedPoints, currentScenarioIndex, selectedOptionIndex)((response) => {
            console.log(response);
            eel.next_scenario()(); // Move to the next scenario
        });
        selectedOption = null; // Reset the selected option
    } else {
        alert("Please select an option before proceeding.");
    }
}

eel.expose(show_end_screen);
function show_end_screen(pointsJson) {
    // Set points data in localStorage
    localStorage.setItem('gamePoints', pointsJson);
    // Redirect to the end screen HTML page
    window.location.href = 'end_screen.html';
}