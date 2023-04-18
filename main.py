from bryce_algorithm import boyer_moore_algorithm
from mohammad_algorithm import xx_algorithm
from timeit import default_timer as timer

#Driver Code
start = timer()
boyer_moore_algorithm()
end = timer()
print(f'The boyer_moore_algorithm() took {end - start:.2} seconds to complete on the given text.')
start = timer()
xx_algorithm()
end = timer()
print(f'The xx_algorithm took {end - start:.2} seconds to complete on the given text.')
