#This is where you will type your code for you algorithm
# define a function to perform a naive search for a pattern in a text file
def naive_search(pattern, txt):
    m = len(pattern)
    n = len(txt)
    count = 0
    for i in range(n - m + 1):
        j = 0
        while(j < m):
            if (txt[i + j] != pattern[j]):
                break
            j += 1
 
        if (j == m):
          count += 1
    return count


