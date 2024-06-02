import pandas as pd
import os

def get_raw_data(filename, writefilename, myDir):
    # Import data from text file
    # Define import options for the dryswallow file
    opts1 = {
        "header": [0, 1],  # Skip first row, use second row as header
        "skipfooter": 0  # Skip footer
    }

    # Load dryswallow data
    dryswallow_file = os.path.join(myDir, "swallowTimes", filename)
    dryswallow_data = pd.read_csv(dryswallow_file, **opts1)

    # Define import options for the main data file
    opts2 = {
        "header": None,  # No header
        "skiprows": dryswallow_data.iloc[0, 0] - 1,  # Skip rows based on dryswallow data
        "nrows": dryswallow_data.iloc[0, 1] - dryswallow_data.iloc[0, 0] + 1,  # Number of rows based on dryswallow data
        "skipfooter": 0  # Skip footer
    }

    # Load main data
    data_file = os.path.join(myDir, filename)
    data = pd.read_csv(data_file, **opts2)

    # Convert to output type
    # Note: This step is not needed in Python as pandas DataFrames are already in a suitable format

    # Prepare frame data
    frame_data = []
    chunk_size = 256
    numRows = data.shape[0]

    for k in range(0, numRows, chunk_size):
        if k + chunk_size <= numRows:
            frame_data.append(data.iloc[k:k + chunk_size, :])
        else:
            frame_data.append(data.iloc[k:numRows, :])
            break

    # Prepare directory for saving
    raw_features_dir = os.path.join(myDir, 'Raw_Features_Swallow')
    if not os.path.exists(raw_features_dir):
        os.makedirs(raw_features_dir)

    # Save frame data to .mat file
    writefilename2 = os.path.join(raw_features_dir, writefilename + '.mat')
    for i, df in enumerate(frame_data):
        df.to_csv(writefilename2, mode='a', header=(i == 0), index=False)  # Append to file, omitting headers after the first chunk

# Example usage:
# myDir = "/path/to/your/directory"
# filename = "01_dryswallow1.csv"
# writefilename = "output_filename"
# get_raw_data(filename, writefilename, myDir)
