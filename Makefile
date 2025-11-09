.PHONY: env html clean

env:
	@if conda env list | grep -q "ligo-env"; then \
		echo "Updating existing environment..."; \
		conda env update -f environment.yml; \
	else \
		echo "Creating new environment..."; \
		conda env create -f environment.yml; \
	fi

html:
	myst build --html

clean:
	rm -rf figures/*
	rm -rf audio/*
	rm -rf _build/