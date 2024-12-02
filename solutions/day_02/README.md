# Day 2, Part 1

_(Note: You must have completed Day 1 to access Day 2)_

https://adventofcode.com/2024/day/2

### Work to do:

In order to find the count of Safe Reports, we must:

* Parse the data file, which is in plain text format

* Parse each (non-blank) line into a Report: an ordered collection of integers

* Determine if each Report is "safe" or not:

    * Safe reports contain integer measurements that uniformly increase or decrease

    * Safe reports contain integer measurements that differ by 1, 2, or 3

    * (Reports with measurements that don't meet these requirements are NOT SAFE)

* Count the total number of Safe (as opposed to Unsafe) Reports

### Hints

* Blank lines should be ignored

* Integer measurements can increase or decrease - Differences may be positive or negative

   * It may be useful to consider them as absolute values

   * (as long as they consistently increase, or decrease)

### Debugging:

* See [test_day_02_part_1.py](test_day_02_part_1.py) for example data at each step

___
# Day 2, Part 2

### Work to do:

In order to apply the "Problem Dampener" to our Report Safety checker, we must:

* Parse the data file, which is in plain text format

* Parse each (non-blank) line into a Report: an ordered collection of integers

* Determine the safety of each integer measurement, relative to the previous one:

    * Safe measurements uniformly increase, or decrease

    * Safe measurements differ by 1, 2, or 3

    * (Measurements that don't meet these requirements are NOT SAFE)

* Determine Report safety based on Safe vs. Unsafe measurements:

    * Reports with 0 or 1 Unsafe measurements are Safe

    * Reports with more than 1 Unsafe measurements are Unsafe

* Count the total number of Safe (as opposed to Unsafe) Reports

### Hints

* (Part 1 Hints are still applicable!)

* The first measurement in a Report is always Safe

   * Subsequent measurements must be compared to the previous adjacent Measurement

### Debugging:

* See [test_day_02_part_1.py](test_day_02_part_1.py) for example data at each step
