# **********************************************************************
# Homework Assignment 5: <Animation>
#
# Description:>
# <Make an at least 5 seconds long animation of a running man in minimum of two positions of a running man by using graphics.py.>
#
# Author: <Behina.Bahramsari@mytwu.ca> <student_id: 660360>
# Date: <October 31, 2024>
#
#   I pledge that I have completed the programming assignment independently.
#   I have not copied the code from a student or any source.
#   I have not given my code to any student.
#
# Sign here: <Behina Bahramsari>
# *********************************************************************/

from graphics import *  # needed for drawing simple shapes
import time  # needed for the sleep function

# import os # to change working directory
# os.chdir("/Users/be_bhr/Code/TWU/homework-5/hw5-BahramsariBehina.py")

# input: win is an instance of the GraphWin class from the graphics.py module. The GraphWin object (win) serves as the window (canvas) on which all shapes are drawn.
# passing win as an argument ensures that the same window instance is used across multiple functions, maintaining consistency in the drawings and animations.
# Function to draw the head, body, and arms of the stick figure.
def drawManBodyArm(win):
    h = win.getHeight()
    w = win.getWidth()
    # Draw head
    head = Circle(Point(w // 2, h // 4 - h // 8), h // 8)
    head.draw(win)

    # Draw body
    center = Point(w // 2, h // 2 + h // 8)
    body = Line(Point(w // 2, h // 4), center)
    body.draw(win)

    # Draw arms as a straight line
    arm = Line(Point(w // 2 - w // 4, h // 4 + h // 10), Point(w // 2 + w // 4, h // 4 + h // 10))
    arm.draw(win)

    return h, w, center


# Function to draw a man in run position 1
def drawMan1(win):
    h, w, center = drawManBodyArm(win)

    # Right leg forward and slightly bent at the knee
    right_leg_upper = Line(center, Point(w // 2 + w // 8, h // 2 + h // 5))
    right_leg_lower = Line(Point(w // 2 + w // 8, h // 2 + h // 5), Point(w // 2 + w // 3, h // 2 + h // 2.25))
    right_leg_upper.draw(win)
    right_leg_lower.draw(win)

    # Left leg backward
    left_leg = Line(center, Point(w // 2 - w // 10, h // 2 + h // 2))
    left_leg.draw(win)


# Function to draw a man in run position 2
def drawMan2(win):
    h, w, center = drawManBodyArm(win)

    # Right leg little forward and slightly bent at the knee
    right_leg_upper = Line(center, Point(w // 2 + w // 24, h // 2 + h // 4.5))
    right_leg_lower = Line(Point(w // 2 + w // 24, h // 2 + h // 4.5), Point(w // 2 , h // 2 + h // 2))
    right_leg_upper.draw(win)
    right_leg_lower.draw(win)


    # Left leg back near the body with slightly bent knee
    left_leg_upper = Line(center, Point(w // 2, h // 2 + h // 4.5))
    left_leg_lower = Line(Point(w // 2, h // 2 + h // 4.5), Point(w // 2 - w // 8, h // 2 + h // 2.25))
    left_leg_upper.draw(win)
    left_leg_lower.draw(win)

if __name__ == "__main__":
    # Create the canvas for drawing
    win = GraphWin("Running Man Animation", 200, 200)

    # Simulate the animation with iterating through the still images
    for i in range(0, 5):
        drawMan1(win)
        time.sleep(0.5)
        win.delete("all")
        drawMan2(win)
        time.sleep(0.5)
        win.delete("all")

    win.getMouse()  # Pause to view result
    win.close()  # Close window when done

