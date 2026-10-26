# this file is for the algorithm code. 

import random

# seeding with 50, fixed pseudorandom numbers
random.seed(a=50, version=2)

# sorted(random.sample(range(n), r))
# n = pool of number, population it chooses from. r is how many unique numbers, what will the size of the array be. 
# sample gives unique numbers, n >= r

sorted_10 = sorted(random.sample(range(20), 10))
print(sorted_10)

# reversed input of size 10
reversed_10 = sorted(random.sample(range(20), 10), reverse=True)
print(reversed_10)

# random input of size 10
random_10 = random.sample(range(20), 10)
print(random_10)

# choices allows repeats. here n < r to force repeats
# random.choices(range(n), k=r)
duplicate_10 = random.choices(range(5), k=10)
print(duplicate_10)