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

* Parse file and Reports (lists of integers) as per Part 1

* Determine the Safety as per Part 1...

* Implement "problem-dampening":

    * If removing any one Measurement makes the report Safe: Consider it to be Safe

* Count the total number of Safe (as opposed to Unsafe) Reports

### Hints

* (Part 1 Hints are still applicable!)

* Measurement safety is "relative":

    * If we remove any one measurement, leaving the remaining measurements in order:

    * If the reduced Report is now Safe, consider it Safe!

    * If the reduced Report is still Unsafe, consider it Unsafe!

        * (We aren't interested in removing multiple values)

        * (We must consider each Measurement being removed...)

        * (There may be a more clever solution than testing them all?)

        * (But testing them all, at 5 measurements per Record, isn't too expensive)

### Debugging:

* See [test_day_02_part_1.py](test_day_02_part_1.py) for example data at each step
