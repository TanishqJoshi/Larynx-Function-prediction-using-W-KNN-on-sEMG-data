import os
import numpy as np

# Get directory
my_dir = input("Enter directory path: ")  # You can replace this with a dialog box for directory selection

# Get all .mat files in the directory
my_files = [f for f in os.listdir(my_dir) if f.endswith('.mat')]

# Initialize FinalData
FinalData = []

# Process each file
for file_name in my_files:
    print("Now Reading - ", file_name)
    full_file_name = os.path.join(my_dir, file_name)
    initial = np.load(full_file_name, allow_pickle=True)
    for i in range(len(initial['decomposed_Data'])):
        data = initial['decomposed_Data'][i][0].T
        FinalData.append(data)

# Save FinalData for channel 1
np.save('CoughDataControl_ch1.npy', FinalData)

# Process each file again for channel 2
FinalData = []
for file_name in my_files:
    print("Now Reading - ", file_name)
    full_file_name = os.path.join(my_dir, file_name)
    initial = np.load(full_file_name, allow_pickle=True)
    for i in range(len(initial['decomposed_Data'])):
        data = initial['decomposed_Data'][i][1].T
        FinalData.append(data)

# Save FinalData for channel 2
np.save('CoughDataControl_ch2.npy', FinalData)

# Process each file again for channel 3
FinalData = []
for file_name in my_files:
    print("Now Reading - ", file_name)
    full_file_name = os.path.join(my_dir, file_name)
    initial = np.load(full_file_name, allow_pickle=True)
    for i in range(len(initial['decomposed_Data'])):
        data = initial['decomposed_Data'][i][2].T
        FinalData.append(data)

# Save FinalData for channel 3
np.save('CoughDataControl_ch3.npy', FinalData)
