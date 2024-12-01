build: blacken typecheck test

test:
    # Run all PyTest test suites
	pytest .

typecheck:
    # Perform MyPy type checking on all python files
	mypy .

blacken:
    # Use Black to apply PEP8 code formatting on all python files
	black .

release: deps install build

deps:
    # Use UV to explicitly resolve all dependencies
    # requirements.in: High level dependencies (optionally pinned)
    # requirements.txt: Full, Verbose, explicitly versioned dependencies (generated)
	uv pip compile requirements.in > requirements.txt
	uv pip compile requirements_dev.in > requirements_dev.txt

install:
    # Install the fully versioned dependency files with pip
	pip install -r requirements.txt
	pip install -r requirements_dev.txt
