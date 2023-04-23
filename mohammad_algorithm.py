#This is where you will type your code for you algorithm
# define a function to perform a naive search for a pattern in a text file
def naive_search(pattern, text):
    
    # Initialize a counter to count pattern occurrences
    occurrences = 0

    # Iterate over every possible substring in the text with the same length as the pattern
    for i in range(len(text)-len(pattern)+1):
        
        # If the current substring matches the pattern, increase the counter
        if text[i:i+len(pattern)] == pattern:
            occurrences += 1

    # Return the number of occurrences
    return occurrences

