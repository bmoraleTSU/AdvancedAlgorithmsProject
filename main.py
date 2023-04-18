from bryce_algorithm import sample_algo
from mohammad_algorithm import xx_algorithm
from timeit import default_timer as timer

#Driver Code
start = timer()
sample_algo()
end = timer()
print(f'The sample_algo took {end - start:.2} seconds to complete on the given text.')
start = timer()
xx_algorithm()
end = timer()
print(f'This xx_algorithm took {end - start:.2} seconds to complete on the given text.')
