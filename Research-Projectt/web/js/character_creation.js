// web/js/character_creation.js

/////// TEST  ////////////////
// function autoFillForm() {
//     document.getElementById('name').value = 'Test Name';
//     document.getElementById('age').value = '25';
//     document.querySelector('input[name="student_type"][value="International"]').checked = true;
//     document.querySelector('input[name="work_status"][value="Part-time"]').checked = true;
//     document.getElementById('has_kids').checked = false;
// }

// Ensure DOM is fully loaded before calling autoFillForm
document.addEventListener('DOMContentLoaded', (event) => {
    autoFillForm();
});

////////////////////////////

function submitCharacter() {
    var name = document.getElementById('name').value;
    var age = document.getElementById('age').value;
    var studentType = document.querySelector('input[name="student_type"]:checked').value;
    var workStatus = document.querySelector('input[name="work_status"]:checked').value;
    var hasKids = document.getElementById('has_kids').checked;

    var characterData = {
        name: name,
        age: age,
        studentType: studentType,
        workStatus: workStatus,
        hasKids: hasKids
    };

 // Call Python function to process character creation
 eel.process_character_creation(characterData)(function(response) {
    // Handle the response from Python
    console.log(response);
    // Redirect to the game scenarios page
    window.location.href = 'game_scenarios.html';
});
}

function backToMain() {
    console.log("Going back to the main page from javascript.");
       window.location.href = 'index.html';  // Redirects to the main page
}