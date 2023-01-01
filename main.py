from tkinter import *
from time import sleep  # NOQA
from random import randint  # NOQA

window = Tk()
size = 30
player_grid = [[size / 2, size / 2], [size / 2, size / 2 - 1], [size / 2, size / 2 - 2], [size / 2, size / 2 - 3]]
game = Frame(master=window, bg='black')
last_movement = ""
speed = 20


class Csnake:
    def __init__(self, map_size, points, frame):
        self.map_size = map_size
        self.points = points
        self.frame = frame

    def update(self):
        for i in self.points:
            if i != self.points[0]:
                Label(master=self.frame, bg="Red", width=2, height=1).grid(row=int(i[0]), column=int(i[1]))
            elif i == self.points[0]:
                Label(master=self.frame, bg="#ffcfcf", width=2, height=1).grid(row=int(self.points[0][0]),
                                                                               column=int(self.points[0][1]))
        window.update()

    def over(self):
        return False

    def move_up(self, event):  # NOQA
        global last_movement
        if last_movement != "u":
            checker = 0
            if last_movement == 'r':  ###
                last_movement = "u"
                for pts in range(len(self.points)):  # movement
                    if event.keysym.lower() != "up":
                        return

                    for j in range(pts + 1):
                        empty_screen()
                        self.points[j][0] = self.points[j][0] - 1  # leaders

                    if checker == 0:
                        empty_screen()
                        self.points[pts][1] = self.points[pts][1] - 1  # fixing last movement
                        checker = 1

                    for k in range(pts + 1, len(self.points)):  # late squares
                        empty_screen()
                        self.points[k][1] = self.points[k][1] + 1

                    self.update()

                    sleep(1 / speed)

            if last_movement == "l":  ###
                last_movement = "u"
                for pts in range(len(self.points)):
                    if event.keysym.lower() != "up":
                        return
                    for j in range(pts + 1):
                        empty_screen()
                        self.points[j][0] = self.points[j][0] - 1  # leaders

                    if checker == 0:
                        empty_screen()
                        self.points[pts][1] = self.points[pts][1] + 1  # fixing last movement
                        checker = 1

                    for k in range(pts + 1, len(self.points)):  # late squares
                        empty_screen()
                        self.points[k][1] = self.points[k][1] - 1

                    self.update()

                    sleep(1 / speed)

            if last_movement == "d":
                return

            while not self.over():
                if event.keysym.lower() != "up":
                    return
                empty_screen()

                for p in range(len(self.points)):
                    self.points[p][0] -= 1
                    window.update()
                    last_movement = "u"

                player_snake.update()
                window.update()

                sleep(1 / speed)

    def move_down(self, event):  # NOQA
        global last_movement

        if last_movement != "d":

            checker = 0
            if last_movement == 'r':
                last_movement = "d"
                for pts in range(len(self.points)):
                    if event.keysym.lower() != "down":
                        return
                    for j in range(pts + 1):
                        empty_screen()
                        self.points[j][0] = self.points[j][0] + 1  # leaders

                    if checker == 0:
                        empty_screen()
                        self.points[pts][1] = self.points[pts][1] - 1  # fixing last movement
                        checker = 1

                    for k in range(pts + 1, len(self.points)):  # late squares
                        empty_screen()
                        self.points[k][1] = self.points[k][1] + 1

                    self.update()

                    sleep(1 / speed)

            if last_movement == "l":
                last_movement = "d"
                for pts in range(len(self.points)):
                    if event.keysym.lower() != "down":
                        return
                    for j in range(pts + 1):
                        empty_screen()
                        self.points[j][0] = self.points[j][0] + 1  # leaders

                    if checker == 0:
                        empty_screen()
                        self.points[pts][1] = self.points[pts][1] + 1  # fixing last movement
                        checker = 1

                    for k in range(pts + 1, len(self.points)):  # late squares
                        empty_screen()
                        self.points[k][1] = self.points[k][1] - 1

                    self.update()

                    sleep(1 / speed)

            if last_movement == "u":
                return
            while not self.over():
                if event.keysym.lower() != "down":
                    return
                empty_screen()

                for p in range(len(self.points)):
                    self.points[p][0] += 1
                    window.update()

                    last_movement = "d"
                player_snake.update()
                window.update()

                sleep(1 / speed)

    def move_left(self, event):  # NOQA
        global last_movement

        if last_movement != "l":
            checker = 0
            if last_movement == 'u':
                last_movement = "l"
                for pts in range(len(self.points)):
                    if event.keysym.lower() != "left":
                        return
                    for j in range(pts + 1):
                        empty_screen()
                        self.points[j][1] = self.points[j][1] - 1  # leaders

                    if checker == 0:
                        empty_screen()
                        self.points[pts][0] = self.points[pts][0] + 1  # fixing last movement
                        checker = 1

                    for k in range(pts + 1, len(self.points)):  # late squares
                        empty_screen()
                        self.points[k][0] = self.points[k][0] - 1

                    self.update()

                    sleep(1 / speed)

            if last_movement == "d":
                last_movement = "l"
                for pts in range(len(self.points)):
                    if event.keysym.lower() != "left":
                        return
                    for j in range(pts + 1):
                        empty_screen()
                        self.points[j][1] = self.points[j][1] - 1  # leaders

                    if checker == 0:
                        empty_screen()
                        self.points[pts][0] = self.points[pts][0] - 1  # fixing last movement
                        checker = 1

                    for k in range(pts + 1, len(self.points)):  # late squares
                        empty_screen()
                        self.points[k][0] = self.points[k][0] + 1

                    self.update()

                    sleep(1 / speed)

            if last_movement == "r":
                return
            while not self.over():
                if event.keysym.lower() != "left":
                    return
                empty_screen()

                for p in range(len(self.points)):
                    self.points[p][1] -= 1
                    window.update()
                    last_movement = 'l'

                player_snake.update()
                window.update()

                sleep(1 / speed)

    def move_right(self, event):  # NOQA
        global last_movement
        if last_movement != "r":
            checker = 0
            if last_movement == 'u':
                last_movement = "r"
                for pts in range(len(self.points)):
                    if event.keysym.lower() != "right":
                        return
                    for j in range(pts + 1):
                        empty_screen()
                        self.points[j][1] = self.points[j][1] + 1  # leaders

                    if checker == 0:
                        empty_screen()
                        self.points[pts][0] = self.points[pts][0] + 1  # fixing last movement
                        checker = 1

                    for k in range(pts + 1, len(self.points)):  # late squares
                        empty_screen()
                        self.points[k][0] = self.points[k][0] - 1

                    self.update()

                    sleep(1 / speed)

            if last_movement == "d":
                last_movement = "r"
                for pts in range(len(self.points)):
                    if event.keysym.lower() != "right":
                        return
                    for j in range(pts + 1):
                        empty_screen()
                        self.points[j][1] = self.points[j][1] + 1  # leaders

                    if checker == 0:
                        empty_screen()
                        self.points[pts][0] = self.points[pts][0] - 1  # fixing last movement
                        checker = 1

                    for k in range(pts + 1, len(self.points)):  # late squares
                        empty_screen()
                        self.points[k][0] = self.points[k][0] + 1

                    self.update()

                    sleep(1 / speed)

            if last_movement == "l":
                return
            while not self.over():
                if event.keysym.lower() != "right":
                    return
                empty_screen()

                for p in range(len(self.points)):
                    self.points[p][1] += 1
                    window.update()
                    last_movement = "r"

                player_snake.update()
                window.update()

                sleep(1 / speed)


for i in range(size):  # making the map
    Label(master=game, bg="black", width=2, height=1).grid(row=i, column=i)


def empty_screen():
    for I in player_grid:
        Label(master=game, bg="black", width=2, height=1).grid(row=int(I[0]), column=int(I[1]))


player_snake = Csnake(map_size=size, points=player_grid, frame=game)
player_snake.update()

window.bind("<Up>", player_snake.move_up)
window.bind("<Down>", player_snake.move_down)
window.bind("<Right>", player_snake.move_right)
window.bind("<Left>", player_snake.move_left)

game.pack()
window.mainloop()
