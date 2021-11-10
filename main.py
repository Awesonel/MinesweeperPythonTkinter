import random
import tkinter as tk


def defeat():
    for i in range(10):
        for j in range(10):
            buttons[i][j].button['bg'] = 'white'
            buttons[i][j].button['state'] = tk.DISABLED
            if buttons[i][j].isMine is True:
                buttons[i][j].button['text'] = '@'
            else:
                buttons[i][j].button['text'] = f'{buttons[i][j].mines_around}'
                if buttons[i][j].mines_around == 0:
                    buttons[i][j].button['text'] = ''


class MyButton:
    def __init__(self):
        self.button = tk.Button(win, bg='grey', font=('Arial', 15, 'bold'), command=self.click)
        self.row = -1
        self.column = -1
        self.isMine = False
        self.mines_around = 0

    def click(self):
        self.button['bg'] = 'white'
        self.button['state'] = tk.DISABLED
        if self.isMine is True:
            self.button.config(text='@')
            defeat()
        else:
            self.button.config(text=f'{self.mines_around}')
            if self.mines_around == 0:
                self.button.config(text='')
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 10 > self.row + i >= 0 != abs(i) + abs(j) and 0 <= self.column + j < 10 and buttons[self.row + i][self.column + j].button['state'] != tk.DISABLED:
                            buttons[self.row + i][self.column + j].click()


# --------------------------------------------- WINDOW

win = tk.Tk()

icon = tk.PhotoImage(file="bomb.png")

win.iconphoto(False, icon)

win.title('My Minesweeper - 15 mines')
win.geometry('500x500')
win.resizable(False, False)

# ---------------------------------------------MINES

mines_count = 15
mines = [[False for i in range(10)] for j in range(10)]
while mines_count > 0:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    if mines[x][y] is False:
        mines_count -= 1
        mines[x][y] = True

# ---------------------------------------------FIELD

buttons = [[MyButton() for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        buttons[i][j].button.grid(column=j, row=i, stick='news')
        buttons[i][j].row = i
        buttons[i][j].column = j
        if mines[i][j] is True:
            buttons[i][j].isMine = True

for i in range(10):
    for j in range(10):
        for k in range(-1, 2):
            for m in range(-1, 2):
                if 0 <= i + k < 10 and 0 <= j + m < 10 and buttons[i+k][j+m].isMine is True:
                    buttons[i][j].mines_around += 1

# ---------------------------------------------FIELD CONFIG

    win.grid_columnconfigure(i, minsize=50)
    win.grid_rowconfigure(i, minsize=50)

while True:
    random_begin_x = random.randint(0, 9)
    random_begin_y = random.randint(0, 9)
    if buttons[random_begin_y][random_begin_x].mines_around == 0:
        buttons[random_begin_y][random_begin_x].click()
        break

win.mainloop()
