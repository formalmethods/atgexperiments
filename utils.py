def prettyPrintIndPairs(indpairs):
    """
    Prints the given independence pair
    """
    for condition, pair in indpairs.iteritems():
        print condition + ': ' + str(pair[0]) + ', ' + str(pair[1])