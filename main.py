from bryce_algorithm import boyer_moore_algorithm
from mohammad_algorithm import xx_algorithm
from execution_timer import ExecutionTimer
import time

#Driver Code
timer = ExecutionTimer()
timer.start()
boyer_moore_algorithm()
timer.end()
print(f'The boyer_moore_algorithm() took {timer.print_exec_time():.2} seconds to complete on the given text.')
timer.start()
xx_algorithm()
timer.end()
print(f'The xx_algorithm took {timer.print_exec_time():.2} seconds to complete on the given text.')
