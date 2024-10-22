import numpy as np
import random
import time

def dead_state():
    rows=48
    height=48
    global row_length, height_length
    row_length=rows
    height_length=height
    the_board=np.zeros([rows,height] ,dtype=int)
    return the_board

def random_state():
    the_board=dead_state()
    for i in range(row_length):
        
        for j in range(height_length):
            determinator=random.randrange(0,11,1)
            if determinator>8:
                the_board[i][j]=1
    
    return the_board
    

def render(the_board):
    rendered_output = ""

    # Loop through each row in the array
    for row in the_board:
        # Initialize an empty string for each row
        row_str = ""
        
        # Loop through each cell in the row
        for cell in row:
            if cell == 1:
                row_str += u"\u2588"+u"\u2588"
            else:
                row_str += "  "
        
        # Add the row string to the rendered output with a newline
        rendered_output += row_str + "\n"

    # Print the output (strip the trailing newline for clean output)
    print(rendered_output.strip())

def next_board_state(the_board):
    new_state=dead_state()
    #the_board=the_board.tolist()
    for i in range(0,len(the_board)):
        for j in range(0,len(the_board[i])):
            new_state[i][j]= next_cell_value(the_board,i,j)
    
    return new_state        
            
def next_cell_value(the_board,i,j): 
    live_neighbours=0
    for x1 in range(i-1,i+2):
        if x1<0 or x1>row_length-1:
            continue
        for y1 in range(j-1,j+2):
            if  y1>height_length-1 or y1<0 :
                continue
            if x1==i and y1==j:
                continue
            if the_board[x1][y1]==1:
                live_neighbours=live_neighbours+1
                
    if the_board[i][j]==1:
        if live_neighbours<2  or live_neighbours>3:
            return 0
        else:
            return 1
    else:
        if live_neighbours==3:
            return 1
        else: 
            return 0
        
def run_forever(the_board):
    next_state = the_board
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.09)
if __name__ == "__main__":
    init_state = random_state()
    # init_state = load_board_state('./toad.txt')
    run_forever(init_state)