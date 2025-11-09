[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wOo27OxG)
 
# LIGO Gravitational Wave Analysis

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-joshawat/main)

Tools and utilities for analyzing LIGO gravitational wave data, based on the original LIGO Center for Open Science Tutorial Repository.

This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for UC Berkeley's Stat 159/259 course.

## MyST Documentation
View the interactive documentation: [https://ucb-stat-159-f25.github.io/hw3-joshawat/](https://ucb-stat-159-f25.github.io/hw3-joshawat/)

## Project Structure
- `ligotools/` - Python package with LIGO analysis utilities
  - `readligo.py` - Functions for reading LIGO data files
  - `utils.py` - Signal processing utilities (whitening, audio, etc.)
  - `tests/` - Unit tests for the package
- `data/` - LIGO gravitational wave data files
- `figures/` - Generated plots and visualizations
- `audio/` - Generated audio files from gravitational wave signals
- `LOSC_Event_tutorial.ipynb` - Main analysis notebook

## Installation & Usage

### Using Makefile (recommended):
```bash
make env    # Create conda environment
conda activate ligo
make html   # Build documentation
make clean  # Clean generated files