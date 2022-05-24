from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("pink")
        self.goto(0, 270)
        self.score = 0
        self.high_score = self.read_high_score()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()

    def read_high_score(self):
        with open("high_score.txt") as file:
            score = int(file.read())
        return score

    def write_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(f"{self.high_score}")

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER",align=ALIGNMENT, font=FONT)
