"""
Part 2, Lecture 1, Example 1

Implement and test argmax() function that returns the location of a maximum.
"""


def argmax(values):
    """
    Return the location and value of the maximum contained in a given sequence.

    Parameters
    ----------
    values : Sequence of numbers

    Returns
    -------
    imax : int
        Location of the maximum
    vmax : int or float
        Maximum value
    """
    vmax = max(values)
    imax = values.index(vmax)
    return(imax, vmax)

    # ADD YOUR IMPLEMENTATION HERE


def main():

    # Create list of values to test argmax()
    values = [2, 3, -1, 7, 4]

    # Use argmax() to locale the maximum
    (i, max) = argmax(values)
    # ADD YOUR IMPLEMENTATION HERE
    print("The max value is at {} index and has value {}".format(i, max))

if __name__ == '__main__':
    main()