def fibonacci(n):
    # initialize the first two terms of the sequence
    sequence = [0, 1]
    
    # loop to generate the subsequent terms
    for i in range(2, n):
        # add the previous two terms to generate the next term
        next_term = sequence[i-1] + sequence[i-2]
        # append the next term to the sequence
        sequence.append(next_term)
    
    # return the sequence
    return sequence

# call the function to generate the first 10 terms of the sequence
print(fibonacci(10))
