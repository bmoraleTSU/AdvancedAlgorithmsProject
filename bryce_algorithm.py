#This is where I will code the algorithm that I am creating

def boyer_moore_algorithm(text, pattern):
    """
    A function that takes in a text string and searches for a given pattern within the text.

    Args:
    text: A string of all the text you want the algorithm to search through.
    pattern: A string of the pattern that you want to search for in the given string of text.

    Returns:
    The number of times that the pattern was found in the given text.
    """
    m = len(pattern)
    n = len(text)
    #If the pattern is longer than the text than there can't be any matches
    if m > n:
        return 0
    else:
        #Limit the alphabet because we know that there are no other characters in the text we are using
        #Initialize to 
        skip = {'a': m, 'b': m, 'c': m, 'd': m, 'e': m}
        #Find last(c) for each character in the pattern
        for k in range(m-1):
            skip[pattern[k]] = m - k - 1
        #Initalize the spot in the text we are looking at (the first possible ending of a pattern in the text)
        i = m - 1
        count = 0
        #Loop through entire text
        while i < n:
            j = m - 1
            k = i
            #Loop through entire pattern to see if we have found a match in the text
            while j >= 0 and text[k] == pattern[j]:
                j -= 1
                k -= 1          
            if j == -1:
                #We have found a pattern match!
                count += 1
            #Grab the last occurrence of the character or default to the length of the pattern if the character is missing in the dict
            #Skip ahead in the text by that last(c) value
            i += skip.get(text[i], m)
    
    return count
