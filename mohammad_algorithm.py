#This is where you will type your code for you algorithm

def naive_algorithm(text, pattern):
    start_naive = time.time()
    n = len(text)
    m = len(pattern)

    count_naive = sum(
        [1 for i in range(n - m + 1) if text[i:i + m] == pattern]
    )

    return count_naive, time.time() - start_naive
text = "your_text_here"
pattern = "your_pattern_here"
count, time_taken = naive_algorithm(text, pattern)
print(f"Pattern found {count} times in {time_taken} seconds.")
