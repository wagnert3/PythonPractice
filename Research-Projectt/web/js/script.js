function startNewGame() {
    eel.start_new_game(); // Calls the Python function
}

function exitGame() {
    eel.close_application(); // Calls the Python function to close the application
}

eel.expose(change_page);
function change_page(page) {
    window.location.href = page; // Redirects to the character creation page
}
