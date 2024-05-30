PYTHON_FILES := $(wildcard cerinta*.py)
TARGETS := $(PYTHON_FILES:.py=)

.PHONY: all $(TARGETS)

all: $(TARGETS)

$(TARGETS):
	python3 $@.py