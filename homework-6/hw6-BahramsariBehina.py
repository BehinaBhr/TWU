# ***********************************************************************/
# CMPT 140 (2024 Fall) Mazer drawer
#
# Description:
# This python provides a function to draw a maze
# ref: https://docs.python.org/3/library/turtle.html
#
# NOTE: this function contains some bugs!
#
# Author: Samuel Leung, samuel.leung@twu.ca
# Date: Oct, 2024
#
# Input: maze specification (csv file) - see https://rosettacode.org/wiki/Maze_generation#Python
# Output: draws maze on screen
# *********************************************************************/
import turtle

# This function draws a block with the specified width/height/color
# The end position of the turtle will be at x,y
# The heading (turtle pointing direction) is 0
# The pen/fill color of the turtle will revert back to its current color
#
# input:
#     t = turtle object
#     x = x coordinate of lower-left corner of block
#     y = y coordinate of lower-left corner of block
#     width = width of block
#     height = height of block
#     color = color of block
#
def draw_block(t, x, y, width, height, color):
    # determine whether turtle pen is currently up or down
    curr_pen_state = "down" if t.isdown() else "up"
    t.penup()

    # capture current position
    curr_x, curr_y = t.pos()
    t.setpos(x, y)

    # capture current pen/fill color
    curr_pen_color, curr_fill_color = t.color()
    t.color(color, color)  # set turtle color to the specified color

    # capture current heading
    curr_heading = t.heading()
    t.setheading(0)

    # draw and fill
    t.pendown()
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    t.penup()

    # clean up
    t.color(curr_pen_color, curr_fill_color)
    t.setheading(curr_heading)
    t.setpos(curr_x, curr_y)
    if curr_pen_state == "down":
        t.pendown()
    else:
        t.penup()

# draw maze using the input turtle graphics object
#
# input:
#     tt turtle graphics object
#     maze_fname - maze csv file name
#     block_width - maze block width
#     block_height - maze block height
#     x_org - origin x coordinate i.e. lower left corner
#     y_org - origin y coordinate i.e. lower left corner
#
def draw_maze(tt, maze_fname, block_width, block_height, \
              x_org, y_org, maze_wall_color):
    # read maze
    try:
        f = open(maze_fname, "r")  # the "r" indicates read only mode
    except:
        print("file (" + db_fname + ") not found.")
        return

    # move turtle to inital position: 0,0
    tt.penup()
    x, y = (x_org, y_org)
    tt.setpos(x, y)

    lines = f.readlines()
    lines.reverse()

    for line in lines:
        row = line.split(",")
        x, y = draw_maze_row(tt, row, x, y, \
                             block_width, block_height, maze_wall_color)
        tt.setpos(x, y)

# draw a line of the maze - cache consecutive wall blocks and
# draw them in one go
#
# input:
#     tt
#     row
#     x
#     y
#     block_width
#     block_height
#     maze_wall_color
#
# return:
#     (x,y) - current x,y coordinate of the turtle "pen"
def draw_maze_row(tt, row, x, y, block_width, block_height, maze_wall_color):
    # assumption about the maze
    maze_wall = 0
    x_org = x  # capture start x-coordinate
    num_wall = 0  # keeps track of number of consecutive wall blocks
    for i in range(0, len(row)):
        if int(row[i]) == maze_wall and i < (len(row) - 1):
            # do not draw wall right way ... wait and see if there are
            # consecutive wall block
            num_wall = num_wall + 1
        else:
            if int(row[i]) == maze_wall:
                # if this is a wall block and this is the last column
                num_wall = num_wall + 1
            if num_wall > 0:
                draw_block(tt, x, y, block_width * num_wall, block_height, maze_wall_color)
                x = x + block_width * num_wall
                num_wall = 0 
            x = x + block_width
        tt.setx(x)
    y = y + block_height
    x = x_org
    return (x, y)

if __name__ == '__main__':
    # create turtle object
    tt = turtle.Turtle()

    maze_fname = "/Users/be_bhr/Code/TWU/homework-6/maze_example_very_small.csv"

    block_width, block_height = (20, 20)  # set wall / road width

    x_org, y_org = 0, 0  # origin i.e. lower-left corner of maze

    draw_maze(tt, maze_fname, block_width, block_height, x_org, y_org, "grey")

    input("press enter to quit. ")
