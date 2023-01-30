def calculate_gcd(a, b):
    # Assign the larger number to a and the smaller number to b
    if a < b:
        a, b = b, a
    
    # Use integer division to divide a by b and get the quotient
    quotient = a // b

    # Use the modulo operator to find the remainder when dividing a by b
    remainder = a % b

    # Repeat the division and calculation of remainder until the remainder is 0
    while remainder != 0:
        a, b = b, remainder
        quotient = a // b
        remainder = a % b
    
    # The GCD is equal to the last non-zero value of b
    return b
