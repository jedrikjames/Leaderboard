screen ScoreOverlay():
    tag score_overlay
    frame:
        anchor (0.5, 0.0)
        background Solid("#ffffff99")
        offset (0, 10)
        pos (0.5, 0.0)
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

screen Leaderboard():
    frame:
        align (0.5, 0.5)
        background "#00000080"
        padding (20, 20)
        vbox:
            text "Leaderboard" size 30 color "#FFFFFF"
            for name, score in sorted(variables.leaderboard.items(), key=lambda item: item[1], reverse=True):
                text f"{name}: {score} points" size 22 color "#FFD700"
            textbutton "Close" action Hide("Leaderboard") align (0.95, 0.05)