import tkinter

width, height = 10, 10
room = [[0 for x in range(width)] for y in range(height)]
location = 8 in room
move = " "
wall = "#"
key = "£"
P = "P"
room[6][6] = P
player_x = 6
player_y = 6
playing = 1
quit = " "

log = []
def room1(room):
    for i in range(0, 10):
        room[i][0] = wall
        room[i][9] = wall
        room[0][i] = wall
        room[9][i] = wall
        room[8][1] = key

room1(room)

def printlog(log):
    formattedlog = ""
    for str in log:
        formattedlog += str + '\n'
    return formattedlog

def printroom(room):
    formattedroom = ""
    for row in room:
        for col in row:
            formattedroom += str(col) + " "
        formattedroom += '\n'
    return formattedroom


def moveN():
    global room, player_x, player_y, log
    if room[int(player_x)-1][int(player_y)] != wall:
        room[int(player_x)][int(player_y)] = 0
        room[int(player_x)-1][int(player_y)] = "P"
        player_x -= 1
        log +=["""You have moved North"""]
        if len(log) == 6:
            del log[0]

        map.delete("all")
        map.create_text(250,175,fill="darkgreen",font="Courier 18 italic bold",
                                text=printroom(room))
        map.create_text(250,420,fill="green", font="Courier 18 italic bold",
                                text=printlog(log))

def moveS():
    global room, player_x, player_y, log
    if room[int(player_x)+1][int(player_y)] != wall:
        room[int(player_x)][int(player_y)] = 0
        room[int(player_x)+1][int(player_y)] = P
        player_x += 1
        log +=["""You have moved South"""]
        if len(log) == 6:
            del log[0]

        map.delete("all")
        map.create_text(250,175,fill="darkgreen",font="Courier 18 italic bold",
                                text=printroom(room))
        map.create_text(250,420,fill="green", font="Courier 18 italic bold",
                                text=printlog(log))


def moveE():
    global room, player_x, player_y, log
    if room[int(player_x)][int(player_y)+1] != wall:
        room[int(player_x)][int(player_y)] = 0
        room[int(player_x)][int(player_y)+1] = P
        player_y += 1
        log +=["""You have moved East"""]
        if len(log) == 6:
            del log[0]

        map.delete("all")
        map.create_text(250,175,fill="darkgreen",font="Courier 18 italic bold",
                                text=printroom(room))
        map.create_text(250,420,fill="green", font="Courier 18 italic bold",
                                text=printlog(log))

def moveW():
    global room, player_x, player_y, log
    if room[int(player_x)][int(player_y)-1] != wall:
        room[int(player_x)][int(player_y)] = 0
        room[int(player_x)][int(player_y)-1] = P
        player_y -= 1
        log +=["""You have moved West"""]
        if len(log) == 6:
            del log[0]

        map.delete("all")
        map.create_text(250,175,fill="darkgreen",font="Courier 18 italic bold",
                                text=printroom(room))
        map.create_text(250,420,fill="green", font="Courier 18 italic bold",
                                text=printlog(log))

top = tkinter.Tk()
content = tkinter.Frame(top)
frame = tkinter.Frame(content, borderwidth=5, relief="sunken", width=200, height=500)
top.configure(bg="gray26")
nbtn = tkinter.Button(top, bg="black", fg="white", text="North", width=15, command=lambda: moveN())
sbtn = tkinter.Button(top, bg="black", fg="white", text="South", width=15, command=lambda: moveS())
ebtn = tkinter.Button(top, bg="black", fg="white", text="East", width=15, command=lambda: moveE())
wbtn = tkinter.Button(top, bg="black", fg="white", text="West", width=15, command=lambda: moveW())
map = tkinter.Canvas(top, bg="black", height=500, width=500, cursor="man")
map.create_text(250,175,fill="darkgreen",font="Courier 18 italic bold",
                        text=printroom(room))
map.create_text(250,420,fill="green", font="Courier 18 italic bold",
                        text=printlog(log))
map.grid(row = 1, column = 1)
nbtn.grid(row = 2, column = 1,)
sbtn.grid(row = 4, column = 1)
ebtn.grid(row = 3, column = 1, sticky=("E"), padx=120)
wbtn.grid(row = 3, column = 1, sticky=("W"), padx=120)
top.mainloop()
