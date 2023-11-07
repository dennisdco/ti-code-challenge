# Team International Code challenge.
# Dennis Del Castillo (DDC).
# dennisdco@gmail.com

from data_capture import DataCapture

if __name__ == '__main__':
    capture = DataCapture()

    # Add positive numbers
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)

    print(list(capture.bst))

    stats = capture.build_stats()

    # Get numbers greater than a positive number
    greater_than_4 = stats.get_greater_than(4)
    print("Numbers greater than 4:", greater_than_4)

    # Get numbers lower than a positive number
    lower_than_4 = stats.get_lower_than(4)
    print("Numbers lower than 4:", lower_than_4)

    # Get numbers between a range of two positive numbers
    between_3_and_6 = stats.get_between_range(3, 6)
    print("Numbers between 3 and 6:", between_3_and_6)
