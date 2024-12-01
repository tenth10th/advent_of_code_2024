# Advent of Code 2024 Solutions

Fully tested, annotated solutions for the Advent of Code 2024 challenges, organized by Day. Each Day includes, roughly in order of spoilery-ness:

* A README.md file containing a breakdown of the necessary work, and hints about non-obvious details

* PyTest test files, including intermediary steps against the example/sample data

* Implementations of each day, broken down by part if applicable (e.g. `day_01_part_1.py`)

    * If run directly, these will generate the answer for each part of each day

    * (This output is a direct spoiler!)

## Currently Implemented Days:

* [Day 01](solutions/day_01/README.md)

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
