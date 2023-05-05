from bryce_algorithm import boyer_moore_algorithm
from mohammad_algorithm import naive_search_algorithm
from execution_timer import ExecutionTimer

def read_file(path):
    """
    Function that takes in a path to find a file at then returns the contents of that file.

    Args:
    path: A string that is the path to the file that you are attempting to read.

    Returns:
    A string of all of the text found in the given file.
    """
    try:
        with open(path, mode='r') as file:
            all_text = file.read()

        return all_text
    except FileNotFoundError as err:
        print(f'Unable to process file because it could not be found: {err}')

# Create timer object
timer = ExecutionTimer()
# Driver code
# -Initialize the constants
SEARCH_PATTERN = "ababada"
FILE = "input.txt"
timer.start()
boyer_occurrences = boyer_moore_algorithm(read_file(FILE), SEARCH_PATTERN)
timer.end()
print(f'The pattern was found in the given text file {boyer_occurrences} times when using the Boyer-Moore Algorithm.')
print(f'The Boyer-Moore Algorithm took {timer.print_exec_time():.2f} milliseconds to complete on the given text.')
timer.start()
naive_occurrences = naive_search_algorithm(read_file(FILE), SEARCH_PATTERN)
timer.end()
print(f'The pattern was found in the given text file {naive_occurrences} times when using the Naive Algorithm.')
print(f'The Naive Algorithm took {timer.print_exec_time():.2f} milliseconds to complete on the given text.')
