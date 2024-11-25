# ***********************************************************************/
# Homework Assignment 7: <SuperTurtle – Going Through a Maze>
#
# Description:
# SuperTurtle Class implementing to guide turtle go through a maze by reading a list of x/y coordinates that defines a direction (route) and memorize it and according to that go through the specific maze
#
# Author: <Behina.Bahramsari@mytwu.ca> <student_id: 660360>
# Date: <November 22, 2024>
#
# Input:
# Output:
#
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: <Behina Bahramsari>
# *********************************************************************/

from Point import *
class SuperTurtle:

    # constructor
    def __init__(self,input_tt):
        # turtle object
        self._tt = input_tt
        # route is a list, each item in a list is a list of two items: 
        # x and y coordinate
        self._route = []
    
    # read route
    # @param route_fname - file name containing the routes
    def memorize_route(self,route_fname):
        # open file
        try:
            f = open(route_fname,"r") # the "r" indicates read only mode
        except:
            print("file ("+route_fname+") not found.")
            return
        
        # clear any previously "memorized" route
        self._route = []

        # TODO: read file, assume file is a CSV file with first row as header
        # row followed by x, y coordinates in format:
        # [x-coordinate], [y-coordinate]
        # Please store the x/y coordinates as objects of the Point class.

        # Read the file
        lines = f.readlines()
        # Skip header and read coordinates
        for line in lines[1:]:
            # Split the line into x and y coordinates
            coords = line.strip().split(",")
            # Convert them to integers
            x = int(coords[0])
            y = int(coords[1])
            # Create Point object and store it in the route
            self._route.append(Point(x, y))

        f.close()
    # move the turtle based on the route and starting position
    # 
    # @param x_org: x-coordinate of the starting position 
    # @param y_org: y-coordinate of the starting position
    def go(self,x_org,y_org):
        self._tt.penup()
        self._tt.setpos(x_org,y_org)

        # TODO: call class methods to set the x/y origin
        # (i.e. set starting position)
        # Set the origin for points
        Point.setOrgX(x_org)
        Point.setOrgY(y_org)

        # TODO: move turtle according to the "memorized" route
        self._tt.pendown()
        # Iterate over the stored route and move the turtle to each point
        for point in self._route:
            # Move to the absolute position of the current point
            self._tt.setpos(point.getAbsoluteX(), point.getAbsoluteY())
