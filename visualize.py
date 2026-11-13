import pandas as pd
import csv
import matplotlib.pyplot as plt

sizes = ['10', '100', '800']
inputs = ['Sorted', 'Reverse sorted', 'Random', 'Duplicate heavy']
pivots = ['First pivot', 'Last pivot', 'Random pivot', 'Median of three pivot']
metrics = ['Comparisons', 'Swaps', 'Runtime (nano)', 'Max Recursion Depth']

with open("quicksort_results.csv", "r") as file:
    rows = list(csv.DictReader(file))
for metric in metrics:
    for pivot in pivots:
        plt.figure(figsize=(10, 6))
        for input_type in inputs:
            filtered_rows = [row for row in rows if row['Pivot Strat'] == pivot and row['Input Type'] == input_type]
            sizes = [int(row['Array Size']) for row in filtered_rows]
            values = [int(row[metric]) for row in filtered_rows]
            plt.plot(sizes, values, marker='o', label=input_type)
        plt.title(f'{metric} vs Array Size for {pivot}')
        plt.xlabel('Array Size')
        plt.ylabel(metric)
        plt.legend()
        plt.grid()
        plt.savefig(f'{metric.replace(" ", "_")}_{pivot.replace(" ", "_")}.png')
        plt.close()