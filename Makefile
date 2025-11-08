.PHONY: env html clean

env:
	conda env create -f environment.yml || conda env update -f environment.yml

html:
	myst build --html

clean:
	rm -rf figures/*
	rm -rf audio/*
	rm -rf _build/