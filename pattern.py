def generate_pyramid(n):
    # Initialize an empty list to store the rows of the pyramid
    pyramid = []
    
    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # Number of stars in the current row is 2 * i - 1
        stars = '*' * (2 * i - 1)
        # Number of leading spaces to center the stars is n - i
        spaces = ' ' * (n - i)
        # Add the centered row to the list
        pyramid.append(spaces + stars + spaces)
    
    # Return the list of pyramid rows
    return pyramid