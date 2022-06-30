from vec import Vec

position = Vec(0, 0, 0)

def on_move(x, y):
    global position
    position = Vec(x, y, 0)