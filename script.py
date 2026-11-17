# This is Nick

import random
import time
import csv

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
# sorted_10 is for first pivot partition
sorted_10 = sorted(random.sample(range(20), 10))
last_pivot_sorted_10 = sorted_10.copy()
random_pivot_sorted_10 = sorted_10.copy()
median_of_3_pivot_sorted_10 = sorted_10.copy()
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

# This a test runner to run all of the tests
def run_test(pivot_name, sort_function, input_name, original):
    global quick_comparisons, quick_swaps, max_depth

    quick_comparisons = 0
    quick_swaps = 0
    max_depth = 0

    # this is because sorting is in place, so we make a copy
    values = original.copy()

    #print(f"\nTest: {pivot_name} | {input_name} | Size {len(values)}")
    #print("Original: ", values)

    start_time = time.perf_counter_ns()
    sort_function(values, 0, len(values) - 1)
    finish_time = time.perf_counter_ns()

    runtime = finish_time - start_time
    correctly_sorted = values == sorted(original)

    #print("Sorted: ", values)
    # print("Comparisons: ", quick_comparisons)
    # print("Swaps: ", quick_swaps)
    # print("Runtime: ", finish_time - start_time)
    # print("Max recursion depth: ", max_depth)
    # print("Correctly sorted: ", values == sorted(original))

    return [pivot_name, input_name, len(original), quick_comparisons, quick_swaps, runtime, max_depth, correctly_sorted]

#Four different pivot strats
pivot_strats = [("First pivot", quick_sort_first), 
                ("Last pivot", quick_sort_last), 
                ("Random pivot", quick_sort_random), 
                ("Median of three pivot", quick_sort_median_of_3)]

#Four different input types and three different array sizes
test_arr = [("Sorted", sorted_10),
            ("Reverse sorted", reversed_10),
            ("Random", random_10),
            ("Duplicate heavy", duplicate_10),
                        
            ("Sorted", sorted_100),
            ("Reverse sorted", reversed_100),
            ("Random", random_100),
            ("Duplicate heavy", duplicate_100),
                        
            ("Sorted", sorted_800),
            ("Reverse sorted", reversed_800),
            ("Random", random_800),
            ("Duplicate heavy", duplicate_800)]

CSV_FILE = "quicksort_results.csv"

def yes_no(question):
    while True:
        answer = input(question + " (Yes/No): ").strip().lower()

        if answer in ("yes", "y"):
            return True

        elif answer in ("no", "n"):
            return False

        else:
            print("Please enter Yes or No.")

def introduction():
    print("\tQuick Sort UI")
    print("\nWhat is being tested:")
    print(" 4 Pivot Strategies")
    print(" 4 Input Types")
    print(" 3 Array Sizes (10, 100, 800)")
    print(" Total: 48 Tests")

    print("\nPivot Strategies:")
    for name, function in pivot_strats:
        print(" ", name)

    print("\nInput Types:")
    print(" Sorted")
    print(" Reverse Sorted")
    print(" Random")
    print(" Duplicate Heavy")

    print("\t\nEfficiency ranking rules:")
    print(" 1. Lowest total comparisons (across 3 array sizes)")
    print(" 2. Lowest total swaps (across 3 array sizes) - if comparisons are tied")
    print(" 3. Lowest total max recursion depth (across 3 array sizes) - if both comparisons and swaps are tied")
    print(" 4. Lowest average runtime (of 3 array sizes) - if all other metrics are tied")

    print("\nEach input type will receive its own winning pivot strategy.")

def run_all_tests():
    all_results = []

    total_tests = len(pivot_strats) * len(test_arr)
    test_num = 0

    print("\nRunning all Quck Sort tests...\n")

    for pivot_name, sort_function, in pivot_strats:
            # inner loop runs 12 times (4 input types X 3 array sizes)
        for input_name, original in test_arr:
                test_num += 1
                #print(f"\n\tTest #{test_num} of 48")

                result = run_test(pivot_name, sort_function, input_name, original)

                all_results.append(result)

                print(f"Completed test {test_num}/{total_tests}", end="\r")

    print("\nAll tests completed")

    with open("quicksort_results.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Pivot Strat", "Input Type", "Array Size", "Comparisons", "Swaps", "Runtime (nano)", "Max Recursion Depth", "Correctly Sorted"])

        writer.writerows(all_results)

    print("\nCSV file 'quicksort_results.csv' created successfully.")

    return all_results

def read_csv_results():
    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def display_results():
    results = read_csv_results()

    print("\n\tAll test results")

    for number, result in enumerate(results, 1):

        print(f"\nTest #{number}")
        print("Pivot:", result["Pivot Strat"])
        print("Input:", result["Input Type"])
        print("Size:", result["Array Size"])
        print("Comparisons:", result["Comparisons"])
        print("Swaps:", result["Swaps"])
        print("Runtime:", result["Runtime (nano)"], "ns")
        print("Max Recursion Depth:", result["Max Recursion Depth"])
        print("Correctly Sorted:", result["Correctly Sorted"])

def create_visualizations(show_charts=False):
    import matplotlib.pyplot as plt

    results = read_csv_results()

    # print("Checking visualization data:")

    # for row in results:
    #     if row["Input Type"] == "Sorted":
    #         print(row["Pivot Strat"], row["Array Size"], row["Runtime (nano)"])

    input_types = ["Sorted ", "Reverse sorted", "Random", "Duplicate heavy"]

    metrics = [("Comparisons", "Comparisons", "Total Comparisons"), ("Swaps", "Swaps", "Total Swaps"),
               ("Max Recursion Depth", "Max Recursion Depth", "Maximum Recursion Depth"),
               ("Runtime (nano)", "Runtime (nano)", "Runtime (nano)")]

    for input_name in input_types:

        for csv_column, metric_name, y_label in metrics:

            plt.figure(figsize=(10, 6))

            for pivot_name, function in pivot_strats:

                selected = [row for row in results if row["Input Type"].strip().lower() == input_name.strip().lower() and row["Pivot Strat"].strip().lower() == pivot_name.strip().lower()]

                selected.sort(key=lambda row: int(row["Array Size"]))

                if len(selected) != 3:
                    print(f"Warning: Expected 3 results for "
                          f"{pivot_name} / {input_name}, "
                          f"found {len(selected)}")
                    continue

                sizes = [int(row["Array Size"]) for row in selected]

                metric_values = [int(row[csv_column])
                                for row in selected]

                #runtime = [int(row["Runtime (nano)"]) for row in selected]

                plt.plot(sizes, metric_values, marker="o", label=pivot_name)

            plt.title(f"{metric_name} - {input_name} Input")
            plt.xlabel("Array Size")
            plt.ylabel(y_label)

            plt.xticks([10, 100, 800])

            plt.legend()
            plt.grid(True)

            filename = ("quicksort_" + input_name.lower().replace(" ", "_") + ".png")

            plt.savefig(filename, dpi=300, bbox_inches="tight")

            print("Saved visualization:", filename)

            if show_charts:

                print("Close the chart window to continue.")

                plt.show()

            plt.close()

    print("\nAll 16 visualizations have been generated.")

def display_conclusion():

    results = read_csv_results()

    input_types = ["Sorted", "Reverse sorted", "Random", "Duplicate heavy"]

    print("\tQuick sort conclusion")

    if len(results) != 48 or not all(row["Correctly Sorted"].lower() == "true" for row in results):

        print("\nResults are incomplete or some tests failed.")
        print("Cannot determine the winners.")

        return

    for input_name in input_types: 
        pivot_totals = {}

        for pivot_name, function in pivot_strats:

            selected = [row for row in results if row["Input Type"] == input_name and row["Pivot Strat"] == pivot_name]

            if len(selected) != 3:
                print(f"\nIncomplete data for {input_name}.")
                return

            #total_runtime = sum(int(row["Runtime (nano)"]) for row in selected)

            total_comparisons = sum(int(row["Comparisons"]) for row in selected)

            total_swaps = sum(int(row["Swaps"]) for row in selected)

            total_max_depth = sum(int(row["Max Recursion Depth"]) for row in selected)

            average_runtime = sum(int(row["Runtime (nano)"]) for row in selected) / 3

            pivot_totals[pivot_name] = (total_comparisons, total_swaps, total_max_depth, average_runtime)

        winner = min(pivot_totals, key=lambda name: pivot_totals[name])
        winning_stats = pivot_totals[winner]

        print(f"\nInput Type: {input_name}")
        print("Winning pivot strat:", winner)

        print("Comparisons (total number across 3 array sizes):", winning_stats[0])
        print("Swaps (total number across 3 array sizes):", winning_stats[1])
        print("Max recursion depth (total number across 3 array sizes):", winning_stats[2])
        print("Average runtime (of 3 array sizes):", f"{winning_stats[3]:,.2f} ns")

    print("\n")

def main():

    introduction()

    if not yes_no("\nWould you like to run all the tests?"):
        print("\nGoodbye.")
        return

    run_all_tests()

    if yes_no("\nWould you like to see the 48 results in the terminal?"):
            display_results()

    show_charts = yes_no("\nWould you like to see the visualization?")

    print("\nGenerating visualization files...")

    create_visualizations(show_charts)

    if not show_charts:
        print("\nCharts saved without being displayed.")

    if yes_no("\nWould you like to see the conclusion?"):
        display_conclusion()

    else:
        print("\nGoodbye.")

    print("Quick Sort Performance finished.")

if __name__ == "__main__":
    main()


#Run 4 pivot strats X 4 input types X 3 array sizes = 48 tests
# test_num = 0
# all_results = []
# # outer loop runs through 4 pivot strats
# for pivot_name, sort_function, in pivot_strats:
#     # inner loop runs 12 times (4 input types X 3 array sizes)
#     for input_name, original in test_arr:
#         test_num += 1
#         print(f"\n\tTest #{test_num} of 48")

#         result = run_test(pivot_name, sort_function, input_name, original)

#         all_results.append(result)

# print(f"\n\tCompleted {test_num} tests.")

# with open("quicksort_results.csv", "w", newline="") as file:

#     writer = csv.writer(file)

#     writer.writerow(["Pivot Strat", "Input Type", "Array Size", "Comparisons", "Swaps", "Runtime (nano)", "Max Recursion Depth", "Correctly Sorted"])

#     writer.writerows(all_results)

# print("\nCSV file 'quicksort_results.csv' created successfully.")

