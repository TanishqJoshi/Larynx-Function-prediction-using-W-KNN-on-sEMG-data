import os
import numpy as np
from scipy.io import loadmat, savemat

def energy_distget(filename):
    # Load the .mat file
    mat_data = loadmat(filename)
    FinalData = mat_data['FinalData']

    data = []

    for i in range(len(FinalData)):
        d = np.zeros(40)
        for j in range(40):
            squared_signal = np.abs(FinalData[i][:, j]) ** 2
            # Sum up all the squared values
            d[j] = np.sum(squared_signal)
        
        # Assuming 'energy_matrix' contains your energy matrix
        threshold = np.max(d) * 0.10  # Set your threshold value here

        # Find indices of elements above the threshold
        above_threshold_indices = np.where(d > threshold)[0]
        signal = None

        for k in range(len(above_threshold_indices)):
            if k == 0:
                signal = FinalData[i][:, above_threshold_indices[k]]
            else:
                signal += FinalData[i][:, above_threshold_indices[k]]
        
        data.append(signal)

    # Create directory if it does not exist
    os.makedirs('EnergyDump10', exist_ok=True)

    # Create the output filename
    output_filename = os.path.join('EnergyDump10', os.path.basename(filename))

    # Save the data to a new .mat file
    savemat(output_filename, {'data': data})

    # Clear variables
    del data, FinalData

import tkinter as tk
from tkinter import filedialog
import os

# Function to process each file
def process_file(file_name):
    print("Now Finding energy of - ", file_name)
    # Call your energy_distget function here passing the file_name as an argument
    energy_distget(file_name)

# Choose directory
root = tk.Tk()
root.withdraw()  # Hide the main window
directory = filedialog.askdirectory(title="Select Directory")

# Get all files with .mat extension in the directory
if directory:
    for file_name in os.listdir(directory):
        if file_name.endswith(".mat"):
            full_file_path = os.path.join(directory, file_name)
            process_file(full_file_path)
