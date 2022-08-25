#Drawing squares inside a hyperbola y=1/x.
#Beginning with (1, 1) denoted n=0.
import math

def find_coordinates(number):
    """Display the coordinates of the
    first number squares."""
    xn = 1
    yn = 1
    n = 0
    while n < number:
        print("The coordinates of square {0} are ({1:.5f} , {2:.5f})."\
        .format(n, xn, yn))

        xnbefore = xn
        xn = (xn + math.sqrt(xn**2 + 4))/2
        yn = xn - xnbefore

        n += 1
        



if __name__ == '__main__':
    find_coordinates(30) #choose how many to display
