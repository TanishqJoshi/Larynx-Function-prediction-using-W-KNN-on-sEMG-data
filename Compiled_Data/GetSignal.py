import numpy as np
import tkinter as tk
from tkinter import filedialog
import os
import glob


def summer(filename):
    data = []
    
    # Load data from filename
    loaded_data = np.load(filename, allow_pickle=True)
    
    for i in range(len(loaded_data)):
        signal = loaded_data[i][:,1]  # Assuming you want to sum the second column
        
        # Sum specified columns
        for j in range(2, 4):  # Summing columns 2 and 3
            signal += loaded_data[i][:,j]
        
        data.append(signal)
    
    # Create directory if not exists
    output_directory = "modified_Data2"
    os.makedirs(output_directory, exist_ok=True)
    
    # Save modified data
    output_filename = os.path.join(output_directory, os.path.basename(filename))
    np.save(output_filename, data)


# Choose directory
root = tk.Tk()
root.withdraw()  # Hide the main window
directory = filedialog.askdirectory(title="Select Directory")

# Get all files with .mat extension in the directory
if directory:
    file_pattern = os.path.join(directory, '*.mat')
    mat_files = glob.glob(file_pattern)
    for file_name in mat_files:
        base_file_name = os.path.basename(file_name)
        print("Now summing - ", base_file_name)
        summer(base_file_name)
