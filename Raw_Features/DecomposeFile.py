import os
import numpy as np
from tqwt_functions import tunable_q_filter_s3, tqwt_radix2, itqwt_radix2
import scipy.io

def DecomposeFile(filename):
    data = loadmat(filename)
    frameData = data['frameData']
    
    decomposed_Data = {}
    
    for k in range(frameData.shape[1] - 1):
        x = frameData[0, k]  # x is a signal to be decomposed by a TQWT based filter bank
        x = x[:, 0]  # Assuming x is a 2D array, take the first column
        
        # Decompose signal x
        de, q, band, re, Jl = tunable_q_filter_s3(x)
        x_decompose = []
        for J_component in range(len(de)):
            decomposed = tqwt_radix2(np.random.rand(len(x)), q[J_component], re[J_component], Jl[J_component])
            highband = [np.zeros_like(decomposed[j]) for j in range(Jl[J_component] + 1)]
            highband[band[J_component]] = de[J_component]
            x_decompose.append(itqwt_radix2(highband, q[J_component], re[J_component], len(x)))
        
        ans1 = np.array(x_decompose)
        
        # Repeat the above process for x2 and x3
        x = frameData[0, k + 1][:, 0]  # Assuming x2 is in the next column
        de, q, band, re, Jl = tunable_q_filter_s3(x)
        x_decompose = []
        for J_component in range(len(de)):
            decomposed = tqwt_radix2(np.random.rand(len(x)), q[J_component], re[J_component], Jl[J_component])
            highband = [np.zeros_like(decomposed[j]) for j in range(Jl[J_component] + 1)]
            highband[band[J_component]] = de[J_component]
            x_decompose.append(itqwt_radix2(highband, q[J_component], re[J_component], len(x)))
        
        ans2 = np.array(x_decompose)
        
        x = frameData[0, k + 2][:, 0]  # Assuming x3 is in the column after x2
        de, q, band, re, Jl = tunable_q_filter_s3(x)
        x_decompose = []
        for J_component in range(len(de)):
            decomposed = tqwt_radix2(np.random.rand(len(x)), q[J_component], re[J_component], Jl[J_component])
            highband = [np.zeros_like(decomposed[j]) for j in range(Jl[J_component] + 1)]
            highband[band[J_component]] = de[J_component]
            x_decompose.append(itqwt_radix2(highband, q[J_component], re[J_component], len(x)))
        
        ans3 = np.array(x_decompose)
        
        decomposed_Data[k, 0] = ans1
        decomposed_Data[k, 1] = ans2
        decomposed_Data[k, 2] = ans3
    
    # Save decomposed data
    save_path = os.path.join("Decomposed_Data", 'DC_' + os.path.basename(filename))
    np.save(save_path, decomposed_Data)
    print("Decomposed data saved at:", save_path)

    return decomposed_Data

# Example usage:
# Specify your directory here
directory_path = "/path/to/your/directory"

# Get all .mat files in the specified directory
for filename in os.listdir(directory_path):
    if filename.endswith(".mat"):
        full_filename = os.path.join(directory_path, filename)
        print(f"Now Decomposing - {full_filename}")
        DecomposeFile(full_filename)

