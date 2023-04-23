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

# open the input file and read its contents
with open("input.txt", "r") as file:
    text = file.read()

# define the pattern to search for
pattern = "ababada"

# call the naive_search function to search for the pattern in the text file
count, duration = naive_search(pattern, text)

# print the results of the search
print(f"Number of occurrences of '{pattern}': {count}")
print(f"Duration: {duration:.3f} ms")
