# this file is for the algorithm code. 

import random

# seeding with 50, fixed pseudorandom numbers
random.seed(a=50, version=2)

# sorted(random.sample(range(n), r))
# n = pool of number, population it chooses from. r is how many unique numbers, what will the size of the array be
sorted_10 = sorted(random.sample(range(20), 10))
print(sorted_10)

reversed_10 = sorted(random.sample(range(20), 10), reverse=True)
print(reversed_10)