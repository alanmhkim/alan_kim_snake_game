from turtle import Turtle

# alignment and font of scoreboard on screen
ALIGNMENT = "center"
FONT = ("Arial", 25, "bold")

# Class Scoreboard: at the top of the screen, displays player's score as the game plays on the left as well as the highest score on the right.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.score
        self.color("pink")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

# update scoreboard function: function that updates scores - both the current and high score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

# reset function: when the player dies, the score resets back to zero and if that score is greater than high score, it replaces it.
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

# increase score function: whenever the player eats food, it gains 1 point that is added to the score.
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
