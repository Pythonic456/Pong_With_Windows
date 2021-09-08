#!/usr/bin/python3
import tkinter as tk
import time, random, math

root = tk.Tk()
root.title('Pong V1')

root.iconify()


#FPS_LIMIT: 60 is recommended
#FRAME_SLEEP_OFFSET: If this is 0, the program will do its best to reach the FPS_LIMIT
#SCREEN_RESOLUTION: This is the "play" area, the area everything will happen in
#BOUNCE_X: The X value at which the "ball" can bounce off the mouse
FPS_LIMIT = 60
FRAME_SLEEP_OFFSET = 0

SCREEN_RESOLUTION = [1920, 1200]
BOUNCE_X = 1200
BALL_BOUNCE_SPEED = 2


MOVE_SPEED = round(480/FPS_LIMIT)

if MOVE_SPEED == 0:
    MOVE_SPEED = 1


frame_time_limit = 1/FPS_LIMIT
score = 0
move_speed_float = MOVE_SPEED

class window:
    def __init__(self, title, root):
        self.toplevel = tk.Toplevel(root)
        self.root = root
        self.toplevel.title(title)
    def setpos(self, x, y):
        self.toplevel.geometry('+'+str(x)+'+'+str(y))
        self.toplevel.update()
    def return_toplevel(self):
        return self.toplevel


#Info windows & decoration
playarea_right_edge = window('Right Edge', root)
playarea_left_edge = window('Left Edge', root)
playarea_bottom_edge = window('Bottom Edge', root)
playarea_top_edge = window('Play Area', root)
score_window = window('Score', root)

score_label = tk.Label(score_window.toplevel, text=str(score))
score_label.pack()
score_label.config(font=("Courier", 44))

score_window.toplevel.geometry('200x100+'+str(SCREEN_RESOLUTION[0]-200)+'+35')
playarea_right_edge.toplevel.geometry('5x'+str(SCREEN_RESOLUTION[1]-50)+'+'+str(SCREEN_RESOLUTION[1])+'+35')
playarea_left_edge.toplevel.geometry('5x'+str(SCREEN_RESOLUTION[1])+'+0+0')
playarea_bottom_edge.toplevel.geometry(str(SCREEN_RESOLUTION[1])+'x5+0+'+str(SCREEN_RESOLUTION[1]))
playarea_top_edge.toplevel.geometry(str(SCREEN_RESOLUTION[1])+'x5+0+0')



ball = window('Ball', root)
ballpos = [0, 100]
ball.setpos(ballpos[0], ballpos[1])
ball.toplevel.geometry('200x200')
ball_direction = 'right'
ball_offset_y = 0

#See if the mouse is over the ball window or not
mouse_touching_ball = False
def mouse_over_ball(event):
    global mouse_touching_ball
    mouse_touching_ball = True
def mouse_not_over_ball(event):
    global mouse_touching_ball
    mouse_touching_ball = False
ball.toplevel.bind('<Enter>', mouse_over_ball)
ball.toplevel.bind('<Leave>', mouse_not_over_ball)


itercount = 0
start = 0
end = 1
while not (ballpos[0] >= SCREEN_RESOLUTION[0]-200):
    s = time.time()
    if itercount == FPS_LIMIT:
        end = time.time()
        fps = round(FPS_LIMIT/(end-start), 1)
        print(fps, 'fps', mouse_touching_ball, end=' \r')
        root.title(str(fps))
        itercount = 0
        start = time.time()

    if ballpos[1] >= SCREEN_RESOLUTION[1]-250:
        ball_offset_y = -BALL_BOUNCE_SPEED
    elif ballpos[1] <= 0:
        ball_offset_y = BALL_BOUNCE_SPEED

    if ball_direction == 'right':
        ball.setpos(ballpos[0]+MOVE_SPEED, ballpos[1]+ball_offset_y)
        ballpos = [ballpos[0]+MOVE_SPEED, ballpos[1]+ball_offset_y]
    elif ball_direction == 'left':
        ball.setpos(ballpos[0]-MOVE_SPEED, ballpos[1]+ball_offset_y)
        ballpos = [ballpos[0]-MOVE_SPEED, ballpos[1]+ball_offset_y]
    
    if ballpos[0] >= BOUNCE_X and mouse_touching_ball == True and ball_direction == 'right':
        ball_direction = 'left'
        ball_offset_y = random.randint(-BALL_BOUNCE_SPEED, BALL_BOUNCE_SPEED)
    elif ballpos[0] <= 0:
        ball_direction = 'right'
        score += 1
        score_label.config(text=str(score))
        score_window.toplevel.update()
        move_speed_float += 0.2
        MOVE_SPEED = math.floor(move_speed_float)


    
    e = time.time()
    if e-s < frame_time_limit:
        delay = (frame_time_limit-(e-s))+FRAME_SLEEP_OFFSET
        if not (delay < 0):
            time.sleep(delay)

    itercount += 1
