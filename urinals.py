# You need to write a function that returns the maximum of free urinals 
# as an integer according to the unwritten rule.

# Input
# A String containing 1s and 0s (Example: 10001) (1 <= Length <= 20)
# A one stands for a taken urinal and a zero for a free one.


def get_free_urinals(urinals):
    if '11' in urinals:
        return -1
    # Initialize variables
    free = 0
    i = 0
    # Count maximum free urinals
    while i < len(urinals):
        if urinals[i] == '0':
            # Check if the previous and next urinals are also free
            if (i == 0 or urinals[i - 1] == '0') and (i == len(urinals) - 1 or urinals[i + 1] == '0'):
                free += 1
                # Skip the next urinal since it cannot be used
                i += 1
        i += 1
    return free
