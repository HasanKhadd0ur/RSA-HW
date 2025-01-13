# Compiler and Flags
PYTHON = python

# Targets
.PHONY: all run demo clean

# Run the main program
run:
	$(PYTHON) main.py 

# Run the demo script
demo:
	$(PYTHON) demo.py

# Clean temporary files or logs
clean:
	rm -f *.pyc __pycache__/*
	rmdir __pycache__ 2>/dev/null || true
