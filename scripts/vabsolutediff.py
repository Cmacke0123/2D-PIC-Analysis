import os
import re
import numpy as np
import matplotlib.pyplot as plt

# Input directories for hydrogen and deuterium data
hydrogen_dir = "/mnt/cedar_mount_connor/cmacke01/sim7_data/Macho/2d_data"
deuterium_dir = "/mnt/cedar_mount_connor/cmacke01/sim8_data/Macho/2d_data"

# Process files and compute max differences
hydrogen_files = sorted(os.listdir(hydrogen_dir))
max_differences = []

for h_file in hydrogen_files:
    d_file = os.path.join(deuterium_dir, h_file)  # Match by filename
    h_file_path = os.path.join(hydrogen_dir, h_file)

    if not os.path.exists(d_file):
        print(f"Deuterium file not found for {h_file}. Skipping.")
        continue

    # Load data
    h_data, _, _ = load_mco(h_file_path)
    d_data, _, _ = load_mco(d_file)

    if h_data is None or d_data is None:
        print(f"Failed to load data for {h_file}. Skipping.")
        continue

    # Check grid sizes
    if h_data.shape != d_data.shape:
        print(f"Grid size mismatch for {h_file}. Skipping.")
        continue

    # Compute difference
    difference = np.abs(h_data - d_data)

    # Compute max difference
    max_difference = np.max(difference)
    max_differences.append((h_file, max_difference))
# Display all results at the end
print("\nSummary of Maximum Differences:")
for file_name, max_diff in max_differences:
    print(f"{file_name}: {max_diff}")

