"""
Utilities for data presentation
"""

def pretty_print_ind_pair(indpairs):
    """
    Prints the given independence pair
    """
    for condition, pair in indpairs.iteritems():
        print condition + ': ' + str(pair[0]) + ', ' + str(pair[1])
