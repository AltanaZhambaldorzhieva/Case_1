# Case_1
# Zhambaldorzhieva A., Ryaguzova D., Zaytseva D.
#
import turtle
def triangle(x, y, a):
    '''
            Function, drawing square.
            :param x: upper left corner coordinate x
            :param y: upper left corner coordinate y
            :param a: side length of a square
            :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(linecolor, color)
    turtle.begin_fill()
    hyp = a * 2 ** 0.5
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(hyp)
    turtle.left(135)
    turtle.forward(a)
    turtle.end_fill()
    turtle.left(90)
    turtle.done()

def square(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.done()

def paral(x,y,a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.color('dark blue')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a / 2)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a / 2)
    turtle.right(135)
    turtle.end_fill()
    turtle.done()

def main():
    '''
    Main function.
    :return: None
    '''
    square()
    paral()
    triangle()
    turtle.done()


if __name__ == '__main__':
    main()



