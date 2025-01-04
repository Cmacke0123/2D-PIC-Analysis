
# PIC Simulation Analysis

## Overview
This repository contains tools for processing, visualizing, and analyzing data from PIC (Particle-In-Cell) simulations. It is designed to facilitate comparisons between simulations with varying parameters, such as hydrogen vs. deuterium gas.

## Features

- **Data Loading**: Scripts to load .mco files and handle varying grid sizes.

- **Visualization**: Tools to generate contour and heatmap plots for simulation data.

- **Comparison**: Automated comparison of datasets, highlighting differences between simulations.

- **Batch Processing**: Support for handling multiple files corresponding to different quantities.

## Repo Structure (under construction)

PIC-Simulation-Analysis/
│
├── data/                   # Example or sample .mco files (if permissible)
├── scripts/                # Python scripts for processing and visualization
│   ├── load_mco.py         # Code for loading .mco files
│   ├── compare_simulations.py # Code for hydrogen vs. deuterium comparisons
├── results/                # Output files (plots, difference arrays, etc.)
├── requirements.txt        # List of Python dependencies
├── README.md               # Overview of the project
└── .gitignore              # Files to ignore (e.g., large datasets, logs)

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Libraries listed in requirements.txt

## Installation
- Clone the repository:

git clone https://github.com/yourusername/PIC-Simulation-Analysis.git
cd PIC-Simulation-Analysis

- Install dependencies:

pip install -r requirements.txt

## Usage

**Prepare Data**:

Place .mco files for hydrogen and deuterium simulations in appropriate directories (e.g., data/hydrogen/, data/deuterium/).

**Run Scripts**:

**Load and visualize data**:

python scripts/load_mco.py

**Compare datasets**:

python scripts/compare_simulations.py

**Results**:

Plots and numerical outputs will be saved in the results/ directory.

## Example Workflow

**Load Simulation Data**:

from scripts.load_mco import load_mco

hydrogen_data, nx, ny = load_mco("data/hydrogen/density_1.mco")
deuterium_data, _, _ = load_mco("data/deuterium/density_1.mco")

**Generate Comparison Plots**:

from scripts.compare_simulations import compare_datasets

compare_datasets(hydrogen_data, deuterium_data, output_dir="results/")

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bug fixes or feature enhancements.

## Acknowledgments

- Inspiration from ongoing research in plasma physics.

- Developed as part of a broader academic project.

- For questions or feedback, contact cmacke01@student.ubc.ca.

