define e = Character("Eileen")
define player = Character("Player")
define A = Character("Character A")
define B = Character("Character B")
define C = Character("Character C")
define D = Character("Character D")
define teacher = Character("Teacher")
define correct = "You got the right answer!"
define wrong = "You got the wrong answer!"

label start:
    call variables  
    show screen ScoreOverlay
    scene bg laboratory

    A "Hi! I'm [A]! Nice to meet you!"
    B "Hello! I'm [B]. Let's split up the parts, I'll do the second experiment!"
    C "Then the third should be mine! [C] by the way, nice to meet you!"
    D "I guess the last one's mine then. The name's [D]."
    B "You should help everyone, [player]!"
    player "Sure!"
    A "Let's do mine first!"
    
    jump scene_2

label scene_2:

    scene bg laboratory_table
    
    A "I'll read out the process in the book, then you keep it in mind."
    player "*nods*"
    A "Here I go! It says that we should-"
    A "Note the appearance of the wire."
    A "Using the tongs..."
    A "We must hold the wire in the hottest part of a burner flame for 1 to 2 minutes."
    A "But first, to do that, we need to fix the Bunsen burner. Put the end of the tube into the yellow faucet, and the other end to the Bunsen burner."
    A "Then, we place the evaporating dish near the base of the burner."
    A "After that, we get a piece of magnesium from the laboratory coordinator. Using crucible tongs, hold the sample in the burner flame until the magnesium starts to burn. REMEMBER, DO NOT LOOK DIRECTLY AT THE FLAME."
    A "When the ribbon stops burning, put the remains in the evaporating dish. Then we examine all that!"
    A "Did you get all that?"
    player "*nods*"
    A "Great! Let's start!"
    
    jump scene_3        

label scene_3:
    A "What are the materials we need?"
    menu:
        "Wire, Tongs, Bunsen Burner, Evaporating Dish, and Magnesium":
            $ variables.points += 5
            A "[correct]"
        "Test Tubes, Test Tube Holder, Matches, and Copper (II) Carbonate (CuCO3)":
            $ variables.points -= 1
            A "[wrong]"
    
    A "There! We prepared everything, what's the first step?"
    menu:
        "Hold the wire in the hottest part of a burner flame for 1 to 2 minutes.":
            $ variables.points += 5
            A "You're so good at this!"
        "Hold the wire above the fire for 1 to 2 minutes":
            $ variables.points -= 1
            B "I don't think that's how it goes..."
            B "That's okay! I'll read the book again!"
        "Hold the wire in the hottest part of a burner flame for 3 minutes":
            $ variables.points -= 1
            B "I don't think that's how it goes..."
        "Hold the wire above the fire for 3 minutes":
            $ variables.points -= 1
            B "I don't think that's how it goes..."
    
    A "What do we do with this?"
    menu:
        "Hold the sample in the burner flame until the magnesium starts to burn":
            $ variables.points += 5
            A "Right! I remember now! DON'T LOOK AT IT DIRECTLY!"
        "Put aside":
            $ variables.points -= 1
            A "[wrong]"
        "Hold the sample beside the burner flame for 2 to 3 minutes":
            $ variables.points -= 1
            A "[wrong]"
        "dgsgsdsg":
            $ variables.points -= 1
            A "[wrong]"
    
    jump scene_4

label scene_4:
    if variables.points >= 10:
        A "We're finally done!"
        teacher "Great Job!"
    else:
        teacher "That is wrong! Re-do it right now!"
        jump scene_2

    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    jump scene_5

label scene_5:
    scene bg laboratory_table
    
    B "Oh! Great, you've finished the first experiment. Let's move on to mine next. It says here in the book that-"
    
    B "Place 2 heaping micro spatulas of copper (II) carbonate (CuCO3) in a clean, dry test tube. Note the appearance of the sample."
    
    B "Watch the appearance closely—it's a light green powder."
    
    B "Next, we'll heat it for about 3 minutes. Use the test tube holder like this. Make sure you hold it at the top, and don't touch the bottom."
    
    B "After heating, we insert a burning wood splint into the test tube. If carbon dioxide (CO2) is present, it will extinguish the flame. Make sure you observe any changes in the residue inside the test tube."
    
    B "Did you get all that?"
    player "*nods*"
    B "Great! Let's start!"
    
    jump scene_6

label scene_6:
    B "What are the materials we need?"
    menu:
        "Test tube holder, Test tube, Matches, Copper (II) Carbonate (CuCO3), Bunsen burner":
            $ variables.points += 5
            B "That's right!"
        "Salt, Magnesium, Evaporating dish":
            $ variables.points -= 1
            B "I don't think that's right, let's use this instead."
    
    B "Great! Next, what will we put in the clean, dry test tube?"
    menu:
        "2 heaping micro spatulas of copper (II) carbonate (CuCO3)":
            $ variables.points += 5
            B "That's amazing!"
        "3 heaping micro spatulas of copper (II) carbonate (CuCO3)":
            $ variables.points -= 1
            B "Haha! I see you got confused. Here's the right one."
    
    B "Now, let's heat it for 3 minutes. Do you have the test tube holder ready?"
    menu:
        "Hold the top of the test tube firmly":
            $ variables.points += 5
            B "Wow, that's great!"
        "Hold the middle half of the test tube firmly":
            $ variables.points -= 1
            B "Oh no! Be careful with that. You need to hold the test tube like this—"
    
    B "How long will we heat this up?"
    menu:
        "3 minutes":
            $ variables.points += 5
            B "Wow, you have good memory!"
        "2 minutes":
            $ variables.points -= 1
            B "Oh you got it wrong. Here look at the textbook again."
    
    B "It's almost 3 minutes, what do we put inside the test tube?"
    menu:
        "Burning wood splint":
            $ variables.points += 5
            B "Wow, that's great!"
        "Copper (II)":
            $ variables.points -= 1
            B "No! Put this instead."
    
    B "Oh shoot! I forgot, what's present if the flame of the burning wood splint inside the test tube gets put out?"
    menu:
        "Carbon dioxide gas (CO2) is present":
            $ variables.points += 5
            B "Okay, thanks!"
        "Copper (II) carbonate (CuCO3) is present":
            $ variables.points -= 1
            B "Hmm, are you sure?"
    
    B "Okay, are we finished?"
    menu:
        "No, we have to take note of the appearance of the residue in the test tube":
            $ variables.points += 5
            B "Oh, right!"
        "Yes, let's move on to the next experiment":
            $ variables.points -= 1
            B "Oh no, did you take note of the appearance of the residue? Hmm, that's okay, I did!"
    
    jump scene_7

label scene_7:
    if variables.points >= 20:
        B "We're finally done!"
        teacher "Great Job!"
    else:
        teacher "That is wrong! Re-do it right now!"
        jump scene_5

    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    jump scene_8

label scene_8:
    scene bg laboratory_table
    
    C "Congratulations! You've made it to the third experiment, substitution! I'm eager to explain what the book says here. So listen carefully!"
    
    player "*nods*"
    
    label substitution_book:

    C "CAUTION. IT IS IMPORTANT TO WEAR PROPER ATTIRE INSIDE THE LABORATORY EXPERIMENT SUCH AS: LABORATORY GOWN, SAFETY GOGGLES, FACE MASK, AND DISPOSABLE GLOVES."
    
    C "Let's start! First, stand a clean, dry test tube in the test tube rack."
    
    C "Add about 5 mL of 3 M hydrochloric acid (HCl) to the tube."
    
    C "Then, carefully drop a small piece of zinc metal (Zn) into the acid in the test tube. Observe and record what happens."
    
    C "Using a test tube holder, invert a second test tube over the mouth of the test tube in which the reaction is taking place. Then, remove the inverted tube after 30 seconds and quickly insert a burning wood splint into the mouth of the tube. A 'pop' indicates the presence of hydrogen gas."
    
    C "Take note of the appearance of the substance in the reaction test tube."
    
    C "Now, for the second part: Add about 5 mL of 1 M copper (II) sulfate (CuSO4) solution to a clean, dry test tube. Place a small amount of zinc metal in the solution. Observe the solution and the zinc before and after the reaction."
    
    C "Did you get all that?"
    player "*nods*"
    
    C "Great! Let's start!"
    
    jump scene_9
    
label scene_9:
    C "Alright, to check your knowledge, it's time for a quiz!"
    C "What are the materials we need?"
    
    menu:
        "5 mL of 3 M hydrochloric acid (HCl), test tube rack, test tube, zinc metal (Zn), wood splint, 5 mL of 1 M copper (II) sulfate (CuSO4)":
            $ variables.points += 5
            C "Amazing! You remembered the materials we used."
        "Bunsen burner, evaporating dish, copper (II) carbonate (CuCO3)":
            $ variables.points -= 1
            C "You got it wrong, let me show you the materials we used."
    
    C "Why should you be careful when handling hydrochloric acid (HCl)?"
    menu:
        "A. It can cause fire":
            $ variables.points -= 1
            C "Oh no! You did not pay attention to the caution."
        "B. It can cause painful burns":
            $ variables.points += 5
            C "That's right! It is important to handle acids with care."
        "C. It can stain your clothes":
            $ variables.points -= 1
            C "Oh no! You did not pay attention to the caution."
    
    C "What is the next step after inverting the test tube for 30 seconds?"
    menu:
        "A. Immediately add about 5 mL of 1 M copper (II) sulfate (CuSO4) solution":
            $ variables.points -= 1
            C "Oh no! Let me read the book again for you."
            jump substitution_book
        "B. Remove the inverted test tube and quickly insert burning wood splint into the mouth of the tube":
            $ variables.points += 5
            C "Very good! You have remembered the procedure."
        "C. Smell the test tube and wait for another 1 minute":
            $ variables.points -= 1
            C "Oh no! Let me read the book again for you."
            jump substitution_book
    
    jump scene_10
    
label scene_10:
    if variables.points >= 30:
        C "We're finally done!"
        teacher "Great Job!"
    else:
        teacher "That is wrong! Re-do it right now!"
        jump scene_8

    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    jump scene_11

label scene_11:

    scene bg laboratory_table
    
    D "Good morning! Are you ready for our last experiment? This one is called metathesis! I'm excited to walk you through it, so pay close attention!"
    
    D "First, we'll start by adding about 2 mL of 0.1 M Lead Nitrate Pb (NO3)2 to a clean, dry test tube."
    
    D "Next, we'll add 2 mL of 0.1 M Potassium Iodide (KI) to the test tube. Watch closely!"
    
    D "Look at that! Observe the reaction and note any changes in the mixture."
    
    D "Next, we need to prepare three solutions. For Beaker A, add 5 drops of alcohol and 5 drops of phenolphthalein."
    
    D "For Beaker B, we'll prepare a saturated lead nitrate solution. That means adding 30g of lead nitrate to 10 mL of H2O."
    
    D "And for Beaker C, we'll add 15g of copper sulfate to 100 mL of H2O."
    
    D "Now, let's fill an Erlenmeyer flask with 1M ammonium hydroxide (NH4OH). We'll dissolve 3.5 g in 100 mL of H2O."
    
    D "Now comes the fun part! We'll fill each beaker with the ammonium hydroxide solution to produce red, white, and blue solutions."
    
    D "Make sure to observe the colors that develop!"
    
    jump scene_12

label scene_12:

    D "Did you follow all of that? Let's do a quick quiz to check your understanding!"
    
    D "What should we add to the first test tube to start our reaction?"
    menu:
        "A. 2 mL of sodium chloride (NaCl)":
            $ variables.points -= 1
            D "Not quite! It should be potassium iodide. Let's remember that for next time!"
        "B. 2 mL of potassium iodide (KI)":
            $ variables.points += 5
            D "Exactly! Potassium iodide is correct!"
    
    D "What color did the mixture turn after adding the potassium iodide?"
    menu:
        "A. Blue":
            $ variables.points -= 1
            D "Nope! It was yellow. Let's keep an eye out for that!"
        "B. Yellow":
            $ variables.points += 5
            D "Right! It turned bright yellow!"
    
    D "What do we need to observe in the beakers after adding the ammonium hydroxide solution?"
    menu:
        "A. The color changes in the solutions":
            $ variables.points += 5
            D "Correct! We need to observe the color changes!"
        "B. The temperature of the solutions":
            $ variables.points -= 1
            D "That's not it! We're looking for color changes, not temperature."
    
    jump scene_13

label scene_13:
    if variables.points >= 40:
        D "We did it! Great job!"
    else:
        teacher "That is wrong! You need to re-do it!"
        jump scene_metathesis
    
    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."
    
    jump scene_14

label scene_14:

    scene bg classroom

    A "Good morning, everyone! We are here today to present our findings on four interesting chemistry experiments: Synthesis, Analysis, Substitution, and Metathesis."
    B "Let's begin with the Synthesis experiment, where we observed the reaction of magnesium with a Bunsen burner flame."
    A "We noted the appearance of the wire before heating and then heated it in the hottest part of the flame for 1-2 minutes. The key thing was to observe the changes."
    C "Next, the Analysis experiment. We heated copper(II) carbonate and observed its color change and the emission of carbon dioxide."
    D "The Substitution experiment involved the reaction of zinc with hydrochloric acid and copper(II) sulfate. Safety precautions were very important, as we worked with acids."
    A "Finally, the Metathesis experiment. We mixed lead nitrate with potassium iodide and observed the precipitate formation."
    B "Now, let's test your knowledge with a quiz!"
    
    jump quiz

label quiz:
    B "Question 1: What important observation must be made in the Synthesis experiment before heating the wire?"
    menu:
        "A. The color of the flame":
            $ variables.points -= 1
            C "Not yet! If you don't record the original look of the wire, you cannot see how it changed."
        "B. The length of the wire":
            $ variables.points -= 1
            C "Not yet! If you don't record the original look of the wire, you cannot see how it changed."
        "C. The appearance of the wire":
            $ variables.points += 1
            B "That's right! Observing the wire before heating is crucial. You get 1 point!"
        "D. The temperature of the burner":
            $ variables.points -= 1
            C "Not yet! If you don't record the original look of the wire, you cannot see how it changed."

    C "Question 2: In the Analysis experiment, what gas was tested using the burning splint method?"
    menu:
        "A. Hydrogen":
            $ variables.points -= 1
            A "Oops, incorrect! We tested for carbon dioxide."
        "B. Oxygen":
            $ variables.points -= 1
            A "Oops, incorrect! We tested for carbon dioxide."
        "C. Carbon dioxide":
            $ variables.points += 1
            D "That is correct! Carbon dioxide extinguished the flame."
        "D. Nitrogen":
            $ variables.points -= 1
            A "Oops, incorrect! We tested for carbon dioxide."

    D "Question 3: In the Substitution experiment, what safety precaution is most important when handling hydrochloric acid?"
    menu:
        "A. Wear gloves":
            $ variables.points -= 1
            B "Not quite, though gloves are important!"
        "B. Wear a lab coat":
            $ variables.points -= 1
            B "Not quite, though protective clothing is needed!"
        "C. Don't inhale fumes":
            $ variables.points -= 1
            B "Important, but there's more to consider."
        "D. All of the above":
            $ variables.points += 1
            D "Correct! Safety first in all cases!"

    A "Question 4: What was the noticeable observation when lead nitrate reacted with potassium iodide in a Metathesis reaction?"
    menu:
        "A. Temperature change":
            $ variables.points -= 1
            C "No, we were expecting a color change due to a precipitate forming."
        "B. Color change":
            $ variables.points += 1
            C "That's correct! A precipitate formed, causing a color change."
        "C. Gas production":
            $ variables.points -= 1
            C "No, we were expecting a color change due to a precipitate forming."
        "D. No change":
            $ variables.points -= 1
            C "No, we were expecting a color change due to a precipitate forming."

    jump results

label results:
    if variables.points >= 50:
        "You have [variables.points] points."
        "In total, you made [variables.mistakes] wrong choices."
        B "Well done! You certainly listened well. As a reward—an extra credit point!"
        D "Congratulations! Here's a chemistry-themed sticker!"
    else:
        A "Looks like you're a bit of practice away. Don't worry!"
        C "You need to retake the quiz to improve your score. Let's go over the main observations again."
        D "Reloading the slideshow for review."
        jump quiz

    B "We hope you learned something new about these experiments. Thanks for trying it out!"

    python:
        player_name = renpy.input("Enter your name for the leaderboard:")
        variables.leaderboard.update({player_name: variables.points})
        variables.save_leaderboard()
        
    call screen Leaderboard(variables)

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

label addtional_options:
    
    if variables.retry_option and not variables.continue_anyway:
        menu too_many_mistakes_menu:
            "You made too many mistakes."
            "Continue anyway!":
                $ variables.continue_anyway = True
            "Retry from the beginning!":
                jump start
        return


#    if variables.retry_option == True and variables.continue_anyway == False:
#        menu too_many_mistakes_menu:
#            "You made too many mistakes."
#            "Continue anyway!":

#                $ variables.continue_anyway = True
#                pass
#            "Retry from the beginning!":
#                jump start
#    return
#    menu:
#        "You made too many mistakes."
#        "Continue anyway!":
#            pass
#        "Retry from the beginning":
#            return