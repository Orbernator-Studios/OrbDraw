from turtle import *


#Not filling. Remove numbers and switch to letter

hideturtle()

def fatalError():
    print("Quitting")
    exit()

def colorSet(selection):
    pencolor(selection)
    fillcolor(selection)



def square(size, lor, fill):
    if fill == ("Yes"):
        begin_fill()
    else:
        print("")
    for count in range(4):
        forward(size)
        if lor == ("Left"):
            right(90)
        elif lor == ("Right"):
            left(90)
        else:
            print("Fatal Error. Square. Left Or Right")
            fatalError()
    if fill == ("Yes"):
        end_fill()
    else:
        print("")
    exitonclick()



def triangle(size, lor, fill):
    if fill == ("Yes"):
        begin_fill()
    else:
        print("")
    for count in range(3):
        forward(size)
        if lor == ("Left"):
            left(120)
        elif lor == ("Right"):
            right(120)
        else:
            print("Fatal Error. Triangle. Left Or Right")
            fatalError()
    if fill == ("Yes"):
        end_fill()
    else:
        print("")
    exitonclick()


def rectangle(sideone, sidetwo, lor, fill):
    loop = (0)
    if fill == ("Yes"):
        begin_fill()
    else:
        print("")
    for count in range(4):
        if loop == (0):
            loop = 1
        else:
            if loop == (1):
                forward(sideone)
            elif loop == (2):
                forward(sidetwo)
            else:
                print("Fatal Error. Rectangle. Side loop")
                fatalError()
            if lor == ("Left"):
                left(90)
            elif lor == ("Right"):
                right(90)
            else:
                print("Fatal Error. Rectangle. Left Or Right")
                fatalError()
            if loop == (1):
                loop = (2)
            else:
                loop = (1)
    if fill == ("Yes"):
        end_fill()
    else:
        print("")
    exitonclick()


def hexagon(size, lor, fill):
    if fill == ("Yes"):
        begin_fill()
    else:
        print("")
    for count in range(6):
        forward(size)
        if lor == ("Left"):
            left(60)
        elif lor == ("Right"):
            right(60)
        else:
            print("Fatal Error. Hexagon. Left Or Right")
            fatalError()
    if fill == ("Yes"):
        end_fill()
    else:
        print("")

def executer(shape, shapesize, lor, fill, shapelength, shapewidth):
    print("\n")
    print("Executing Shape: " + shape)
    if shape == ("Square"):
        square(shapesize, lor, fill)
    elif shape == ("Hexagon"):
        hexagon(shapesize, lor, fill)
    elif shape == ("Rectangle"):
        rectangle(shapelength, shapewidth, lor, fill)
    elif shape == ("Triangle"):
        triangle(shapesize, lor, fill)
    else:
        print("\n")
        print("A fatal error has occured")
        fatalError()

def finalChecksTwo(shape, shapesize, lor, fill, shapelength, shapewidth):
    if fill == ("Yes"):
        executer(shape, shapesize, lor, "Yes", shapelength, shapewidth)
    elif fill == ("yes"):
        executer(shape, shapesize, lor, "Yes", shapelength, shapewidth)
    elif fill == ("Y"):
        executer(shape, shapesize, lor, "Yes", shapelength, shapewidth)
    elif fill == ("y"):
        executer(shape, shapesize, lor, "Yes", shapelength, shapewidth)
    elif fill == ("No"):
        executer(shape, shapesize, lor, "No", shapelength, shapewidth)
    elif fill == ("no"):
        executer(shape, shapesize, lor, "No", shapelength, shapewidth)
    elif fill == ("N"):
        executer(shape, shapesize, lor, "No", shapelength, shapewidth)
    elif fill == ("n"):
        executer(shape, shapesize, lor, "No", shapelength, shapewidth)
    else:
        print("Please change your Fill option as " + fill + " is not accepted.")
        finalMenu(shape, shapesize, shapelength, shapewidth)


def finalChecksOne(shape, shapesize, lor, fill, shapelength, shapewidth):
    if lor == ("Left"):
        finalChecksTwo(shape, shapesize, "Left", fill, shapelength, shapewidth)
    elif lor == ("left"):
        finalChecksTwo(shape, shapesize, "Left", fill, shapelength, shapewidth)
    elif lor == ("L"):
        finalChecksTwo(shape, shapesize, "Left", fill, shapelength, shapewidth)
    elif lor == ("l"):
        finalChecksTwo(shape, shapesize, "Left", fill, shapelength, shapewidth)
    elif lor == ("Right"):
        finalChecksTwo(shape, shapesize, "Right", fill, shapelength, shapewidth)
    elif lor == ("right"):
        finalChecksTwo(shape, shapesize, "Right", fill, shapelength, shapewidth)
    elif lor == ("R"):
        finalChecksTwo(shape, shapesize, "Right", fill, shapelength, shapewidth)
    elif lor == ("r"):
        finalChecksTwo(shape, shapesize, "Right", fill, shapelength, shapewidth)
    else:
        print("Please change your Left Or Right Value as " + lor + " is not accepted.")
        finalMenu(shape, shapesize, shapelength, shapewidth)





def finalMenu(shape, shapesize, shapelength, shapewidth):
    print("\n")
    lorinput = input("Would you like your shape drawn to the left or right?")
    print("\n")
    print("You have selected: " + lorinput)
    print("\n")
    fillinput = input("Would you like your shape filled?")
    print("\n")
    print("You have selected: " + fillinput)
    finalChecksOne(shape, shapesize, lorinput, fillinput, shapelength, shapewidth)

def rectangleAdds(shape, shapesize):
    print("You have selected: " + shape)
    print("\n")
    shapelength = int(input("Please enter the length of the rectangle: "))
    print("\n")
    shapewidth = int(input("Please enter the width of the rectangle: "))
    print("\n")
    finalMenu(shape, shapesize, shapelength, shapewidth)

def shapecheck(shapetocheck, shapesizeinputcont):
    if shapetocheck == ("Square"):
        finalMenu("Square", shapesizeinputcont, 0, 0)
    elif shapetocheck == ("square"):
        finalMenu("Square", shapesizeinputcont, 0, 0)
    elif shapetocheck == ("Rectangle"):
        rectangleAdds("Rectangle", shapesizeinputcont)
    elif shapetocheck == ("rectangle"):
        rectangleAdds("Rectangle", shapesizeinputcont)
    elif shapetocheck == ("Hexagon"):
        finalMenu("Hexagon", shapesizeinputcont, 0,0)
    elif shapetocheck == ("hexagon"):
        finalMenu("Hexagon", shapesizeinputcont, 0,0)
    elif shapetocheck == ("Triangle"):
        finalMenu("Triangle", shapesizeinputcont, 0,0)
    elif shapetocheck == ("triangle"):
        finalMenu("Triangle", shapesizeinputcont, 0,0)
    else:
        print("This shape does not exist.")
        print("Restarting...")
        fatalError()

def mainCode():
    print("")
    colorinput = input("Select a color: ")
    print("\n")
    print("You have selected: " + colorinput)
    colorSet(colorinput)
    print("\n")
    shapesizeinput = int(input("Enter a size: "))
    print("Shapes available: Square, Rectangle, Triangle, Hexagon")
    print("\n")
    shapeinput = input("Enter a shape: ")
    print("\n")
    print("You have selected: " + shapeinput)
    shapecheck(shapeinput, shapesizeinput)


def MainMenu():
    print("OrbDraw")
    print("A creation of Orbernator Studios")
    print("")
    print("Visit us on Github")
    print("https://github.com/Orbernator-Studios")
    print("")
    randomthingywithnovalue = input("Press Enter To Continue")
    mainCode()

def RestartMenu():
    restartInput = input("Would you like to draw another shape? (Y/N)")
    print("\n")
    if restartInput == "Y" or restartInput == "y":
        mainCode()
    else:
        print("Ending Program.")
        exit()

MainMenu()
RestartMenu()