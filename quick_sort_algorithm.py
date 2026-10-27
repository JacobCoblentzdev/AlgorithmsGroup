# this file is for the algorithm code. 

import random
import time

quick_comparisons = 0
quick_swaps = 0
max_depth = 0

def partition(values, low, high):
    global quick_comparisons, quick_swaps
    pivot = values[high]
    i = low - 1

    for j in range(low, high):
        quick_comparisons += 1
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
            quick_swaps += 1

    values[i + 1], values[high] = values[high], values[i + 1]
    quick_swaps += 1
    return i + 1


# quick sort with last pivot partition
def quick_sort_last(values, low, high, depth=0):
    # before if low < high to include the base case in recursion depth
    global max_depth
    max_depth = max(max_depth, depth)
    
    if low < high:
        p = partition(values, low, high)
        quick_sort_last(values, low, p - 1, depth + 1)
        quick_sort_last(values, p + 1, high, depth + 1)

# quick sort with first pivot partition. 
def quick_sort_first(values, low, high, depth=0):
    # before if low < high to include the base case in recursion depth
    global max_depth
    max_depth = max(max_depth, depth)
    
    if low < high:
        # what at low becomes the pivot. what at index of high is the pivot, so we put the value at low in there. this is so we don't have to change the calling line of the partition, can still call it with high
        # not incrementing swap, since i'm just moving the pivot in place
        values[low], values[high] = values[high], values[low]
        
        p = partition(values, low, high)
        quick_sort_first(values, low, p - 1, depth + 1)
        quick_sort_first(values, p + 1, high, depth + 1)
        
# quick sort with random pivot partition. 
def quick_sort_random(values, low, high, depth=0):
    # before if low < high to include the base case in recursion depth
    global max_depth
    max_depth = max(max_depth, depth)
    
    if low < high:
        # this is inclusive of both low and high, which is good here
        rand = random.randint(low, high)
        
        # what at low becomes the pivot. what at index of high is the pivot, so we put the value at low in there. this is so we don't have to change the calling line of the partition, can still call it with high
        values[rand], values[high] = values[high], values[rand]
        
        p = partition(values, low, high)
        quick_sort_random(values, low, p - 1, depth + 1)
        quick_sort_random(values, p + 1, high, depth + 1)
        
# quick sort with median-of-3 pivot partition. 
def quick_sort_median_of_3(values, low, high, depth=0):
    # before if low < high to include the base case in recursion depth
    global max_depth
    max_depth = max(max_depth, depth)
    
    if low < high:
        
        # get middle index
        mid = int(low + (high - low) / 2)
        
        iterable1 = (low, mid, high)
        
        # gives sorted list of median of 3 list
        sorted_median_list = sorted(iterable1, key=lambda parameter: values[parameter])
        
        # 1 is the middle element of the sorted list, which is the median of three
        median_of_3 = sorted_median_list[1]
        
        # what at low becomes the pivot. what at index of high is the pivot, so we put the value at low in there. this is so we don't have to change the calling line of the partition, can still call it with high
        values[median_of_3], values[high] = values[high], values[median_of_3]
        
        p = partition(values, low, high)
        quick_sort_median_of_3(values, low, p - 1, depth + 1)
        quick_sort_median_of_3(values, p + 1, high, depth + 1)

#------------------------------------------------------

# seeding with 50, fixed pseudorandom numbers
random.seed(a=50, version=2)

# sorted(random.sample(range(n), r))
# n = pool of number, population it chooses from. r is how many unique numbers, what will the size of the array be. 
# sample gives unique numbers, n >= r

#arrays of size 10
sorted_10 = sorted(random.sample(range(20), 10))
# print(sorted_10)
# print()

# reversed input of size 10
reversed_10 = sorted(random.sample(range(20), 10), reverse=True)
# print(reversed_10)
# print()

# random input of size 10
random_10 = random.sample(range(20), 10)
# print(random_10)
# print()

# choices allows repeats. here n < r to force repeats
# random.choices(range(n), k=r)
duplicate_10 = random.choices(range(5), k=10)
# print(duplicate_10)
# print()
# print()

#---------------------------------------------------------------
# arrays of size 100
sorted_100 = sorted(random.sample(range(200), 100))
# print(sorted_100)
# print()

# reversed input of size 10
reversed_100 = sorted(random.sample(range(200), 100), reverse=True)
# print(reversed_100)
# print()

# random input of size 10
random_100 = random.sample(range(200), 100)
# print(random_100)
# print()

# choices allows repeats. here n < r to force repeats
# random.choices(range(n), k=r)
duplicate_100 = random.choices(range(50), k=100)
# print(duplicate_100)
# print()
# print()

#--------------------------------------------------------------------

# arrays of size 800
sorted_800 = sorted(random.sample(range(1600), 800))
# print(sorted_800)
# print()

# reversed input of size 10
reversed_800 = sorted(random.sample(range(1600), 800), reverse=True)
# print(reversed_800)
# print()

# random input of size 10
random_800 = random.sample(range(1600), 800)
# print(random_800)
# print()

# choices allows repeats. here n < r to force repeats
# random.choices(range(n), k=r)
duplicate_800 = random.choices(range(400), k=800)
# print(duplicate_800)

#--------------------------------------------------------------------

print("Quick sort results - First element pivot on Sorted input array of size 10")
print("Original: ", sorted_10)

start_time = time.perf_counter_ns()
quick_sort_first(sorted_10, 0, len(sorted_10) - 1)
finish_time = time.perf_counter_ns()
run_time = finish_time - start_time

print("Sorted: ", sorted_10)
print("Comparisons: ", quick_comparisons)
print("Swaps: ", quick_swaps)
print("Run time: ", run_time)
print("Max recursion depth: ", max_depth)
print()

# reset variables before next run
quick_comparisons = 0
quick_swaps = 0
start_time = 0
finish_time = 0
run_time = 0
max_depth = 0

print("Quick sort results - First element pivot on Reverse-Sorted input array of size 10")
print("Original: ", reversed_10)

start_time = time.perf_counter_ns()
quick_sort_first(reversed_10, 0, len(reversed_10) - 1)
finish_time = time.perf_counter_ns()
run_time = finish_time - start_time

print("Sorted: ", reversed_10)
print("Comparisons: ", quick_comparisons)
print("Swaps: ", quick_swaps)
print("Run time: ", run_time)
print("Max recursion depth: ", max_depth)
print()

# reset variables before next run
quick_comparisons = 0
quick_swaps = 0
start_time = 0
finish_time = 0
run_time = 0
max_depth = 0

print("Quick sort results - First element pivot on Random-Sorted input array of size 10")
print("Original: ", random_10)

start_time = time.perf_counter_ns()
quick_sort_first(random_10, 0, len(random_10) - 1)
finish_time = time.perf_counter_ns()
run_time = finish_time - start_time

print("Sorted: ", random_10)
print("Comparisons: ", quick_comparisons)
print("Swaps: ", quick_swaps)
print("Run time: ", run_time)
print("Max recursion depth: ", max_depth)
print()

# reset variables before next run
quick_comparisons = 0
quick_swaps = 0
start_time = 0
finish_time = 0
run_time = 0
max_depth = 0

print("Quick sort results - First element pivot on Duplicate-Heavy input array of size 10")
print("Original: ", duplicate_10)

start_time = time.perf_counter_ns()
quick_sort_first(random_10, 0, len(duplicate_10) - 1)
finish_time = time.perf_counter_ns()
run_time = finish_time - start_time

print("Sorted: ", duplicate_10)
print("Comparisons: ", quick_comparisons)
print("Swaps: ", quick_swaps)
print("Run time: ", run_time)
print("Max recursion depth: ", max_depth)
print()

# reset variables before next run
quick_comparisons = 0
quick_swaps = 0
start_time = 0
finish_time = 0
run_time = 0
max_depth = 0

print("---------------------------------------------------------")
print()

print("Quick sort results - Last element pivot on Sorted input array of size 10")
print("Original: ", sorted_10)

start_time = time.perf_counter_ns()
quick_sort_last(sorted_10, 0, len(sorted_10) - 1)
finish_time = time.perf_counter_ns()
run_time = finish_time - start_time

print("Sorted: ", sorted_10)
print("Comparisons: ", quick_comparisons)
print("Swaps: ", quick_swaps)
print("Run time: ", run_time)
print("Max recursion depth: ", max_depth)
print()