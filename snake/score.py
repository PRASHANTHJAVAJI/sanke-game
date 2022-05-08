from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("score_data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.pu()
        self.goto(0,270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score} Highest score :{self.high_score}", align="center", font=("Courier", 25, "normal"))

    def Increase_score(self):
        self.score+=1
        self.update()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("score_data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER.",align="center",font=("Courier",50,"normal"))