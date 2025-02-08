define e = Character("Eileen")
define correct = "You got the right answer!"
define wrong = "You got the wrong answer!"

show screen ScoreOverlay

init python:
    import requests
    import json

    class Variables:
        def __init__(self):
            self.points = 0
            self.mistakes = 0
            self.retry_option = False
            self.continue_anyway = False
            self.leaderboard = self.load_leaderboard()
        
        def load_leaderboard(self):
            api_url = "https://api.jsonbin.io/v3/b/67a6f945ad19ca34f8fbf243"  # JSONBin ID
            api_key = "$2a$10$V71sdRkkKP535d9MYEZjeeE7wEfgjmulpHsHg7r6M8o.iLdDK2R8W"  # API Key

            headers = {
                "X-Master-Key": api_key
            }
            
            response = requests.get(api_url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                return data.get("record", {}).get("leaderboard", {})
            else:
                print("Error loading leaderboard:", response.text)
                return {}
        
        def save_leaderboard(self):
            api_url = "https://api.jsonbin.io/v3/b/67a6f945ad19ca34f8fbf243"  # JSONBin ID
            api_key = "$2a$10$V71sdRkkKP535d9MYEZjeeE7wEfgjmulpHsHg7r6M8o.iLdDK2R8W"  # API Key
            
            headers = {
                "Content-Type": "application/json",
                "X-Master-Key": api_key
            }
            
            # GET request para hindi madelete existing data
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                existing_data = response.json().get("record", {})
                existing_leaderboard = existing_data.get("leaderboard", {})
                existing_leaderboard.update(self.leaderboard)  # Merge new scores with old ones
                
                # Top 5 Scores
                sorted_leaderboard = dict(sorted(existing_leaderboard.items(), key=lambda item: item[1], reverse=True)[:5])
                updated_data = {"leaderboard": sorted_leaderboard}
            else:
                print("Error retrieving existing leaderboard, creating new one.")
                updated_data = {"leaderboard": self.leaderboard}
            
            # PUT request para masave
            response = requests.put(api_url, headers=headers, json=updated_data)

            if response.status_code == 200:
                print("Leaderboard successfully updated!")
            else:
                print("Error saving leaderboard:", response.text)

label start:
    call variables  
    show screen ScoreOverlay

    menu choice_menu1:
        "Right choice":
            $ variables.points += 5

        "Wrong choice":
            $ variables.points -= 1
            $ variables.mistakes += 1
    
    e  "You have [variables.points] points."
    e "In total, you made [variables.mistakes] wrong choices so far."
    
    jump question_2
    
label question_2:

    menu choice_menu2:
        "The right choice":
            $ variables.points += 5

        "The wrong choice":
            $ variables.points -= 1
            $ variables.mistakes += 1
    
    e  "You have [variables.points] points."
    e "In total, you made [variables.mistakes] wrong choices so far."        

    jump question_3

label question_3:

    menu choice_menu3:
        "Right choice again":
            $ variables.points += 5

        "Wrong choice again":
            $ variables.points -= 1
            $ variables.mistakes += 1
    
    e  "You have [variables.points] points."
    e "In total, you made [variables.mistakes] wrong choices so far."
    
    jump question_4
    
label question_4:  

    menu choice_menu4:
        "Okay choice":
            $ variables.points += 5
    
        "Meh choice":
            $ variables.points -= 1
            $ variables.mistakes += 1
    
    e  "You have [variables.points] points."
    e "In total, you made [variables.mistakes] wrong choices so far."
    
    $ player_name = renpy.input("Enter your name for the leaderboard: ")
    $ variables.leaderboard[player_name] = variables.points
    $ variables.save_leaderboard()  # Save to JSONBin
    
    show screen Leaderboard

    menu leaderboard_menu:
        "Retry from the beginning":
            hide screen Leaderboard
            jump start
        "Exit":
            return
    
    hide screen ScoreOverlay

label rightchoice:
    e "This is the right choice"
    return

label variables:
    python:
        variables = Variables()  
    return

label additional_options:
    
    if variables.retry_option and not variables.continue_anyway:
        menu too_many_mistakes_menu:
            "You made too many mistakes."
            "Continue anyway!":
                $ variables.continue_anyway = True
            "Retry from the beginning!":
                jump start
        return
