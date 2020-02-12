#Lab #14
#Due Date: 12/13/2019, 11:59PM
########################################
#                                      
# Name: Joshua Famous
# Collaboration Statement: I worked on this assignment alone.             
#  
########################################


def genInf(aList):
    '''
        >>> g = genInf([5,'a',2])
        >>> next(g)
        5
        >>> next(g)
        'a'
        >>> next(g)
        2
        >>> next(g)
        5
        >>> next(g)
        'a'
        >>> next(g)
        2
        >>> g = genInf([0])
        >>> next(g)
        0
        >>> next(g)
        0
        >>> next(g)
        0
        >>> next(g)
        0
    '''

    # Check iterable types
    try: 
        testIterable = iter(aList)
    except TypeError:
        raise ValueError("Must provide iterable!")

    # Check empty list
    if(len(aList) == 0):
        return

    # Start at 0, iterate through and reset index at end of seq
    index = 0
    while True:
        yield aList[index]
        index += 1
        if(index == len(aList)):
            index = 0


def genFilter(seq, fn):
    """ 
        >>> isEven = lambda x: x % 2 == 0 
        >>> list(genFilter(range(5), isEven)) 
        [0, 2, 4]
        >>> oddNum = (2*i-1 for i in range (10)) 
        >>> list(genFilter(oddNum, isEven)) 
        []
        >>> g = genFilter(range(1,11), isEven) 
        >>> next(g) 
        2
        >>> next(g) 
        4
        >>> next(g) 
        6
        >>> next(g) 
        8
        >>> next(g) 
        10
        >>> next(g) 
        Traceback (most recent call last):
        ...
        StopIteration
    """

    # Check iterable types
    try: 
        testIterable = iter(seq)
    except TypeError:
        raise ValueError("Must provide iterable!")


    # For each item check fn, only yield when true
    for num in seq:
        if(fn(num)):
            yield num
    return

def genAccum(seq, fn):
    '''
        >>> add = lambda x, y: x + y
        >>> mul = lambda x, y: x * y
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    '''

    # Check iterable types
    try: 
        thisIter = iter(seq)
    except TypeError:
        raise ValueError("Must provide iterable!")


    # Iterate, updating total and yielding
    total = next(thisIter)
    yield total
    for num in thisIter:
        total = fn(total, num)
        yield total
    return