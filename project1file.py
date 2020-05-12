#           Alex Petralia
#           CSCI 141
#           11/8/2013
#           Project #1: Sierpinski Triangles!


import pygame, random, math

width = 400     #max number of pixels across the width
height = 300    #max number of pixels across the height
iteration_number = 10000 #number of points that get plotted

def newImage(size):
    """ Create new 3d array of pixels """
    return pygame.surfarray.array3d(pygame.Surface(size))

triangle = newImage((width, height)) #creates the image

def Corner():
    """ Selects a corner location by random """
    cornerlocation_bot_left = (0, height)
    cornerlocation_top = (width // 2, 0)
    cornerlocation_bot_right = (width , height)
    z = random.randrange(1,4)
    if z == 1:
        return cornerlocation_bot_left
    elif z == 2:
        return cornerlocation_top
    elif z == 3:
        return cornerlocation_bot_right
def max_distance(width, height):
    """ determines the maximum distance between a point and a corner """
    """ uses the width and height as inputs """
    side = math.sqrt(((width/2)**2) + (height**2))
    s = side**2
    if width < s:
        maxdistance = s 
        return maxdistance
    else:
        maxlength = width 
        return maxdistance

def Color(x,y):
    """ Determines the color pigment of a pixel """
    s = math.sqrt(((width/2)**2) + (height**2))
    w = width
    d_red = math.sqrt(((x - 0)**2) + ((y - height)**2))
    d_green = math.sqrt(((x - (width//2))**2) + ((y - 0)**2))
    d_blue = math.sqrt(((x - width)**2) + ((y - height)**2))
    r = int((1 - (d_red/w))*255)
    g = int((1 - (d_green/w))*255)  
    b = int((1 - (d_blue/w)) *255)   
    return((r,g,b))

def showImage(image):
    """ Displays the current image """
    width,height,depth = image.shape
    pygame.display.set_mode((width,height))
    surf = pygame.display.get_surface()
    pygame.surfarray.blit_array(surf, image)
    pygame.display.flip()

ycord = random.randrange(1,height) #creates a random y coordinate
xcord = random.randrange(1,width)  #creates a random x coordinate

for i in range(iteration_number):
    RandCorner = Corner()
    xcord = (xcord + RandCorner[0]) // 2
    ycord = (ycord + RandCorner[1]) // 2
    triangle[xcord][ycord] = Color(xcord, ycord)
    showImage(triangle)
