screen Leaderboard(data):
    tag leaderboard
    $ print(data.leaderboard)
    vbox style "st_leaderboard_box":
        hbox style "st_leaderboard_box":
            frame style "st_leaderboard_col1":
                background Solid("#ffffff33")
                text "Player Name" style "st_leaderboard_header"
            frame style "st_leaderboard_col2":
                background Solid("#ffffff33")
                text "Points" style "st_leaderboard_header"
        $ index = 0
        for name, score in data.leaderboard.items():
            python:
                index += 1
                row_color = "#ffffff22" if index % 2 == 0 else "#ffffff11"
            hbox style "st_leaderboard_box":
                frame style "st_leaderboard_col1":
                    background Solid(row_color)
                    text "[name]" style "st_leaderboard_text"
                frame style "st_leaderboard_col2":
                    background Solid(row_color)
                    text "[score]" style "st_leaderboard_text"
    frame:
        background None
        anchor (1.0, 0.0)
        offset (-10, 10)
        pos (1.0, 0.0)
        vbox:
            xalign 1.0
            spacing 5
            button style "st_leaderboard_button":
                action Function(data.reload_leaderboard)
                text "Reload" style "st_leaderboard_button_text"
            button style "st_leaderboard_button":
                action Return()
                text "Close" style "st_leaderboard_button_text"
        
screen ScoreOverlay():
    tag score_overlay
    frame:
        anchor (0.5, 0.0)
        background Solid("#ffffff99")
        offset (0, 10)
        pos (0.5, 0.0)
        vbox:
            vpgrid:
                cols 2
                frame:
                    background None
                    xsize 200
                    text _("Points") xalign 0.5 bold True
                frame:
                    background None
                    xsize 200
                    text _("Mistakes") xalign 0.5 bold True
                text "[variables.points]" xalign 0.5
                text "[variables.mistakes]" xalign 0.5
            button:
                xalign 0.5
                background Solid("#00000099")
                hover_background Solid("#000000cc")
                action ShowMenu("Leaderboard", variables)
                text "Leaderboard"

style st_leaderboard_text:
    xalign 0.5

style st_leaderboard_header is st_leaderboard_text:
    size int(gui.text_size * 1.4)
    bold True

style st_leaderboard_box:
    align (0.5, 0.5)
    spacing 5

style st_leaderboard_col1:
    xsize 400
    xalign 0.5

style st_leaderboard_col2 is st_leaderboard_col1:
    xsize 200

style st_leaderboard_button:
    background Solid("#ffffff99")
    hover_background Solid("#ffffff66")
    xsize 200

style st_leaderboard_button_text:
    xalign 0.5