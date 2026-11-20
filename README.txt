Project Title: Final Project - Best Quick Sort Pivot Strategy

Team Members: Shahzaib Hayat, Nicholas Hinojosa, Jacob Coblentz

Project Summary: The goal of this project is to find out which pivot strategy from last pivot, first pivot, random pivot, and median-of-three pivot is most efficient on each input type of sorted, reversed, random, and duplicate heavy arrays. 

Dependencies: Python 3. Also python’s standard library modules, including random, time, and csv. Also the third party package called matplotlib, and Git (optional, if cloning the repository). 

Installations/setup steps:
A user must have Python 3 installed. To install, enter these commands based on your operating system (OS):

Windows: winget install -e --id Python.Python.3.13
macOS (needs Homebrew): brew install python
Ubuntu/Debian Linux: sudo apt install python3 python3-pip

To verify Python 3 installation, enter these commands based on your OS:

Windows: python --version
macOS/Linux: python3 --version

A user must have matplotlib installed. To install, enter these commands based on your operating system:

Windows: python -m pip install matplotlib
macOS / Linux: python3 -m pip install matplotlib
For Linux, if that doesn’t work, enter: sudo apt install python3-matplotlib

To verify matplotlib installation, enter these commands based on your OS:

Windows: python -c "import matplotlib; print(matplotlib.__version__)"
macOS/Linux: python3 -c "import matplotlib; print(matplotlib.__version__)"

To install Git (optional), enter these commands based on your operating system:
Windows: winget install --id Git.Git -e --source winget
macOS (needs Homebrew): brew install git
Ubuntu/Debian Linux: sudo apt install git

To verify Git installation, enter this command (same on all OSs):
git --version

To run the code, clone this repository onto your machine using GitHub Desktop and the URL of the repository. To clone it through terminal instead, type the command “git clone https://github.com/JacobCoblentzdev/AlgorithmsGroup.git”. Or you can download the ZIP from the repository page and extract the files. 

Execution instructions:
1.	cd (change directory) into the project folder, once you’ve cloned the repository or downloaded the files. If in Visual Studio Code (VS Code), open the project folder. 
2.	If in terminal, type “python script.py” on Windows or the command “python3 script.py” on macOS / Linux to run script.py. In VS Code, click on the file “script.py”. Run the file. This is by clicking the triangle button at the top. 
3.	This will display the initial terminal User Interface (UI). It will explain what’s being tested, the four pivot strategies, input types, efficiency ranking rules, and will ask if you’d like to run all 48 tests. Enter “Yes” to move forward. Enter “No” to end the program.
4.	After entering “Yes”, all the 48 tests will be run and a CSV file with the results will be created. This will be the “quicksort_results.csv” file. Do not modify the file.
5.	The terminal UI will then ask if you’d like to see the 48 results in the terminal. Enter “Yes” to see them. Enter “No” to move onto the next step.
6.	If you entered “Yes” you will see 48 tests, each with the pivot strategy name, input type, array size, and number of comparisons, swaps, runtime in nanoseconds (this will vary between runs), and number of maximum recursion depth. It will also show True if the array was correctly sorted and False if not. The terminal UI will then ask if you want to see the visualizations of the tests. If you entered “No” earlier, you would skip straight to this. At this current prompt, enter “Yes” to see the visualizations, or “No” to move to the next step.
7.	If you entered “Yes”, then 16 images will be generated as files in your folder. One image (all are line graphs) will pop up at a time. View it, exit it, and a new one will pop up. Do this 16 times to view all images. If you entered “No” to see visualizations earlier, it would skip this part, but it would still create the image files in your folder.
8.	Then the terminal UI will ask if you want to see the conclusion. For this current prompt, enter “Yes” to see the final results, or “No” to end the program.
9.	If you entered “Yes”, you will see four sections of output. Each is the winning pivot strategy for the different input types. Each section has that winning pivot strategy’s total number of comparisons, swaps, and recursion depth (across the 3 array sizes), and the average runtime (of the 3 array sizes). The program is now finished. 

Additional notes: 
•	The project folder also has the files “quick_sort_algorithm.py” and “visualize.py”. The algorithm file has the original algorithm code. That file is not run, since the code is pasted into “script.py” which is run. The file “visualize.py” has the code to generate the visualizations. That code is used in “script.py” as well, so “visualize.py” is not run. 
•	No datasets or small sample inputs are required, since script.py generates the input arrays. 

Example usage:
The following example usage does not show all 48 tests or the visualizations to save space. If you want to see them, enter “Yes” as your responses there. 

         Quick Sort UI

What is being tested:
 4 Pivot Strategies
 4 Input Types
 3 Array Sizes (10, 100, 800)
 Total: 48 Tests

Pivot Strategies:
  First pivot
  Last pivot
  Random pivot
  Median of three pivot

Input Types:
 Sorted
 Reverse Sorted
 Random
 Duplicate Heavy

Efficiency ranking rules:
 1. Lowest total comparisons (across 3 array sizes)
 2. Lowest total swaps (across 3 array sizes) - if comparisons are tied
 3. Lowest total max recursion depth (across 3 array sizes) - if both comparisons and swaps are tied
 4. Lowest average runtime (of 3 array sizes) - if all other metrics are tied

Each input type will receive its own winning pivot strategy.

Would you like to run all the tests? (Yes/No): Yes

Running all Quck Sort tests...

Completed test 48/48
All tests completed

CSV file 'quicksort_results.csv' created successfully.

Would you like to see the 48 results in the terminal? (Yes/No): No

Would you like to see the visualization? (Yes/No): No

Generating visualization files...
Saved visualization: Comparisons_First_pivot.png
Saved visualization: Comparisons_Last_pivot.png
Saved visualization: Comparisons_Random_pivot.png
Saved visualization: Comparisons_Median_of_three_pivot.png
Saved visualization: Swaps_First_pivot.png
Saved visualization: Swaps_Last_pivot.png
Saved visualization: Swaps_Random_pivot.png
Saved visualization: Swaps_Median_of_three_pivot.png
Saved visualization: Runtime_(nano)_First_pivot.png
Saved visualization: Runtime_(nano)_Last_pivot.png
Saved visualization: Runtime_(nano)_Random_pivot.png
Saved visualization: Runtime_(nano)_Median_of_three_pivot.png
Saved visualization: Max_Recursion_Depth_First_pivot.png
Saved visualization: Max_Recursion_Depth_Last_pivot.png
Saved visualization: Max_Recursion_Depth_Random_pivot.png
Saved visualization: Max_Recursion_Depth_Median_of_three_pivot.png

All 16 visualizations have been generated.

Charts saved without being displayed.

Would you like to see the conclusion? (Yes/No): Yes
        Quick sort conclusion

Input Type: Sorted
Winning pivot strat: Median of three pivot
Comparisons (total number across 3 array sizes): 6686
Swaps (total number across 3 array sizes): 3737
Max recursion depth (total number across 3 array sizes): 18
Average runtime (of 3 array sizes): 488,933.33 ns

Input Type: Reverse sorted
Winning pivot strat: Random pivot
Comparisons (total number across 3 array sizes): 8685
Swaps (total number across 3 array sizes): 5229
Max recursion depth (total number across 3 array sizes): 37
Average runtime (of 3 array sizes): 462,566.67 ns

Input Type: Random
Winning pivot strat: Median of three pivot
Comparisons (total number across 3 array sizes): 7598
Swaps (total number across 3 array sizes): 4112
Max recursion depth (total number across 3 array sizes): 26
Average runtime (of 3 array sizes): 492,000.00 ns

Input Type: Duplicate heavy
Winning pivot strat: Median of three pivot
Comparisons (total number across 3 array sizes): 7839
Swaps (total number across 3 array sizes): 5096
Max recursion depth (total number across 3 array sizes): 31
Average runtime (of 3 array sizes): 446,466.67 ns


Quick Sort Performance finished.
