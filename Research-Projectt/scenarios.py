# Scenario data
scenarios = [
    {
    "text": "Stephen sets a group project deadline.",    
    "options": [
        {"text": "Oh BOY! Plan an extra group meeting", "category": "Academic", "points": 5},
        {"text": "Work extra, your bills are coming.", "category": "Work", "points": 5},
        {"text": "Take the evening off", "category": "Well-being", "points": 5}
    ],
    "selected_option": None,
    "initial_choice": None,
    "image": "groupMeeting.png"
    },

    {
   "text": "There's a job fair this weekend.",
    "options": [
        {"text": "Prepare a portfolio", "category": "Academic", "points": 5},
        {"text": "You have a shift that day", "category": "Work", "points": 5},
        {"text": "Rest instead of attending", "category": "Well-being", "points": 5}
    ],
    "selected_option": None,
    "initial_choice": None,
    "image": "jobFair.png"
    },

    {
    "text": "Stephen offers extra credit for a coding contest.",
    "options": [
        {"text": "Prepare all weekend", "category": "Academic", "points": 5},
        {"text": "Can't skip work hours", "category": "Work", "points": 5},
        {"text": "Opt for a weekend break", "category": "Well-being", "points": 5}
    ],
    "selected_option": None,
    "initial_choice": None,
    "image": "codingContest.png"
    },
    
    {
        "text": "You have a big Assignment due this week.",
        "options": [
            {"text": "Work all night on it", "category": "Academic", "points": 5},
            {"text": "Go to work, then study", "category": "Work", "points": 5},
            {"text": "Take a night off to relax", "category": "Well-being", "points": 5}
        ],
        "selected_option": None,  # Store the index of the selected option
        "initial_choice": None,  # Add this to track the initial choice
        "image": "ScenarioProject.png"
    },

    {
        "text": "Your friend invites you to a weekend getaway.",
        "options": [
            {"text": "Decline to study for Judson's test", "category": "Academic", "points": 5},
            {"text": "Plan to work on a side project", "category": "Work", "points": 5},
            {"text": "Accept, you need to relax a bit", "category": "Well-being", "points": 5}
        ],
        
        "selected_option": None,  # Store the index of the selected option
        "initial_choice": None,  # Add this to track the initial choice
        "image": "friends.png"
    },

    {
        "text": "You've been offered a part-time job related to your studies.",
        "options": [
            {"text": "Focus solely on studies for now", "category": "Academic", "points": 5},
            {"text": "Accept the job for practical experience", "category": "Work", "points": 5},
            {"text": "Decline to maintain personal free time", "category": "Well-being", "points": 5}
        ],
        "selected_option": None,  # Store the index of the selected option
        "initial_choice": None,  # Add this to track the initial choice
        "image": "work1.png"
    },

    {
        "text": "Your child is feeling under the weather and needs care.",
        "options": [
            {"text": "Spend the day caring for your child", "category": "Well-being", "points": 10},
            {"text": "Balance work and child care duties", "category": "Work", "points": 5},
            {"text": "Hire help so you can focus on studies", "category": "Academic", "points": 5}
        ],
        
        "image": "caringForChild.png",
        "selected_option": None,
        "initial_choice": None
    }
]