#This is where you will type your code for you algorithm
# define a function to perform a naive search for a pattern in a text file
def naive_search_algorithm(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    #print(f"Naive search took {(end_time-start_time)*1000:.4f} milliseconds")
    return count


