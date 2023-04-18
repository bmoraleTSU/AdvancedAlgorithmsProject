#Class to be exported that will handle the timing of the execution for the algorithms
'''

'''
from timeit import default_timer as timer

class ExecutionTimer:
    def __init__(self):
        self._start = 0
        self._end = 0
        print("Timer created!")
    
    def start(self):
        self._start = timer()

    def end(self):
        self._end = timer()

    def print_exec_time(self):
        """
        A function that returns the time difference between the end() function being called and the start() function being called.
        
        Returns:
        The time calculated by the two function calls and converts the units from seconds to milliseconds
        """
        return (self._end - self._start)*1000