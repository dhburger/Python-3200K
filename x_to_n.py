def x_to_n(x,n):
    """returns the value of x raised to the power of n

    >>> x_to_n(2,3)
    8.0
            
    """
    print float(x**n)


def sa_cuboid(h,l,b):
    """height is h, length is l, base is b
    returns the surface area of a cuboid

    >>> sa_cuboid(1,1,1)
    6

    >>> sa_cuboid(1,2,3)
    22

    """
    print 2*(l*b+b*h+h*l)

def super_safe_adder(x,y):
    """returns the value of x+y if x and y are integers, but retun 0 if x and y are any other type

    >>> super_safe_adder(2,3)
    5

    >>> super_safe_adder('tacos',3)
    0

    """
    if isinstance(x, int) and isinstance(y, int):
        return x+y
    else:
        return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()

