# Advent of Code 2024 Solutions

Fully tested, annotated solutions for the Advent of Code 2024 challenges, organized by Day.

Each Day includes, roughly in order of spoilery-ness:

* A README.md file containing:

  * A breakdown of the necessary work (summary of the Advent Of Code description)

  * Hints about non-obvious details or edge cases

* PyTest test files, containing:

  * (Intended to be run via `pytest`, which should work at any location within the repo, but )

  * Tests for each functional unit of code used in the solution (per "Part" for multi-part days)
  
    * Including the example/sample data, sometimes in multiple intermediate forms

* Implementations of each day, broken down by part if applicable (e.g. `day_01_part_1.py`)

  * (Intended to be run from inside the "day" folder)

  * The code itself is arguably a fairly large spoiler, as an implementation of a working solution

  * Run directly, these will generate the answer for each part of each day _(possibly along with some intermediate stats along the way)_

  * This output is a direct spoiler for the correct answer, but not necessarily the implementation?

## Currently Implemented Days:

*Week 1*

* [Day 01](solutions/day_01/README.md) - 
  [Day 02](solutions/day_02/README.md) -
  Day 03 -
  Day 04 -
  Day 05 -
  Day 06 -
  Day 07

## Installation

I strongly recommend creating a virtual environment, either using a tool like pyenv or poetry, or for a simpler manual approach:
```
python -m venv .venv
```
And then activate it (via your manager, or manually):
```
source .venv/bin/activate
```
(Decent editors like VSCode should activate it automatically when you open your project - This will make your terminal line start with `(.venv)`)

Once your virtual environment is activated, you can then install the dependencies for this project, using the makefile with:
```
make install
```
Or manually by running:
```
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

## Development

You can run the "build" command to perform formatting and type validation, and run unit tests:
```
make build
```
(build is also the default command for this makefile, so just running `make` will run it as well)

The release "command" will update and reinstall all dependencies and reinstall them, before building:
```
make release
```

(The Makefile contains all the individual commands, if you'd prefer to run them manually, or as IDE shortcuts, etc...)
