def calculate_ab(P0, P1, P2):
    # Extract x and y coordinates of the three points
    x0, y0 = P0
    x1, y1 = P1
    x2, y2 = P2
    
    # Calculate the coefficients a and b using the Bézier theorem
    a = (x0 + 4 * x1 + x2) / 6
    b = (y0 + 4 * y1 + y2) / 6
    
    # Return the calculated values of a and b
    return a, b
