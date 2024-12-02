# Day 1, Part 1

https://adventofcode.com/2024/day/1

### Work to do:

In order to calculate the Total Distance, we must:

* Parse the text file into two vertical "columns" of equal length

    * The file is in a delimited text format - not CSV

    * Columns are (usually?) separated by three spaces

    * The file includes blank lines, which should be skipped!

    * Numbers should be converted back into integers for sorting & math purposes

* Sort each vertical column of numbers in ascending order

* Calculate a distance for Each "row" across the two (sorted) columns

    * Subtract the integer values of the two columns

    * (subtract the smaller from the larger)

    * (or just subtract, then get the absolute value)

* Sum the distances from each row to get Total Distance

    * Some rows may have a distance of 0

### Hints

* Each column should contain the same number of integers

* Each number is an integers with five digits

* There are 1,000 rows (of two numbers, column A and column B) to be processed

    * (995 rows have a non-zero distance)
 
* Each column must be sorted in ascending order, before calculating distance:

    * "distance" is the difference between values in a "row" (after columns are sorted!)

### Debugging:

* See [test_day_01_part_1.py](test_day_01_part_1.py) for the example data at each step

___
# Day 1, Part 2

### Work to do:

In order to calculate the Total Similarity, we must:

* Parse the text file into two vertical "columns" of equal length

    * (as per Day 1, Part 1)

* But Do NOT Sort each vertical column - not required on this part

    * (sorting will change the results!)

* Calculate the number of times each unique value occurs in Column B

* Iterate Column A, multiplying it by the times appearing in Column B:

    * If the value from Column A does not appear in column B, times appearing is zero

    * This results in a zero similarity ( N * 0 = 0)

* Sum the similarities of each column (which may be 0) to get Total Similarity

## Hints

* Each column should contain the same number of integers

* Each number is an integer with five digits

* There are 1,000 rows (of two numbers, column A and column B) to be processed

* Do NOT sort the columns - In Part 2, they must remain in their original order!

* Column B contains 579 unique values

* Only 43 values in Column B correspond with Column A

    * (This results in 43 non-zero Similiaries)
 
## Debugging:

* See [test_day_01_part_2.py](test_day_01_part_2.py) for the example data at each step
