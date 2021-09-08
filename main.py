#!/usr/bin/python3
import tkinter as tk
import time, random

root = tk.Tk()
root.title('Main')


#FPS_LIMIT: 30 is recommended, 60 will be a struggle for lower-end computers
#FRAME_SLEEP_OFFSET: If this is 0, the program will do its best to reach the FPS_LIMIT
FPS_LIMIT = 60
FRAME_SLEEP_OFFSET = -0.002


frame_time_limit = 1/FPS_LIMIT

class window:
    def __init__(self, title, root):
        self.toplevel = tk.Toplevel(root)
        self.root = root
        self.toplevel.title(title)
    def setpos(self, x, y):
        self.toplevel.geometry('+'+str(x)+'+'+str(y))
        self.toplevel.update()

windows = []
for i in range(5):
    tmp = window('Window '+str(i), root)
    tmp.setpos(i*100, i*100)
    windows.append(tmp)


#moves: [x_pos, y_pos, x_offset, y_offset] (x- and y- offset are used to change EACH window position, one after the other)
moves = []
for i in range(0, 1920, 10):
    moves.append([i, 0, 0, 40])


s = 0
e = 1
sleeps = 0
start = time.time()
for move in moves:
    s = time.time()
    x_offset = 0
    y_offset = 0
    for tmp in windows:
        x_offset += move[2]
        y_offset += move[3]
        tmp.setpos(move[0]+x_offset, move[1]+y_offset)
    e = time.time()
    if e-s < frame_time_limit:
        sleeps += 1
        delay = (frame_time_limit-(e-s))+FRAME_SLEEP_OFFSET
        if not (delay < 0):
            time.sleep(delay)

end = time.time()
print(round(len(moves)/(end-start), 1), 'fps')
print(sleeps)