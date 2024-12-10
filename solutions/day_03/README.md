# Day 3 (part 1)

_(Note: You must have completed Day 2 to access Day 3)_

https://adventofcode.com/2024/day/3

### Work to do:

In order to find the sum of the Multiplications:

* Parse the data file, which is in plain text format

* Find sequences where `mul()` contains multiple numbers separated by commas, such as `mul(1,2)`

    * (ignore any partial, invalid, or corrupted `mul()` expressions!)

    * (ignore any `mul()` containing anything other than digits and commas!)

* Interpet the numbers as integers: `mul(2,3)` should be parsed as integers `[2, 3]`

* Multiply the numbers in the `mul()` expression together to get a result (also an integer)

    * `[2, 3]` should be multipled together to get `6`

* Sum all of the results to get the answer (also an integer)

### Hints

* The groups of numbers to be multplied start with `mul(` and end with `)`

* Numbers are always in pairs (of two)

* The only valid characters to be inside of a "mul" are `["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]`

### Debugging:

* See [test_day_03_part_1.py](test_day_03_part_1.py) for example data at each step

___
# Day 3, Part 2

### Work to do:


We need to do most of the same steps from Day 1, including finding the `muls()`: But they can be enabled or disabled by the special strings `do()` and `don't()`. Disabled `muls()` shouldn't be included in the results!

* All the rules and steps from Part 1 still apply!

* `muls()` are enabled by default, which means we should interpret and count them normally

* `don't()` is a special string which, when encountered, disables "muls" - the following "muls" should not be counted!

* `do()` is a special string which, when encountered, re-enables "muls" - following "muls" can be counted as usual again!

### Hints

* Keep track of whether "muls" are enabled or not - They start out enabled

* Make sure you recognize and apply "dos" and "dont's" before moving on to any following "muls"

* Hopefully straightforward, if your Day 1 solution works?

    * (once you have found the "muls", everything else is the same...)

### Debugging:

* See [test_day_03_part_2.py](test_day_03_part_2.py) for example data at each step
