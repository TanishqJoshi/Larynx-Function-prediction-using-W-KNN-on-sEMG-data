import numpy as np
from scipy.io import loadmat, savemat

def load_and_process_features(mat_files, save_file, slice_range):
    ans = []

    for mat_file in mat_files:
        data = loadmat(mat_file)
        FeatureEx = data['FeatureEx']

        if not ans:
            ans = FeatureEx[:, :slice_range[1]]
        else:
            ans = np.hstack((ans, FeatureEx))

    ans = ans[:, :slice_range[1]]
    savemat(save_file, {'ans': ans})

# Process FeatureEx_Control files
control_files = ["FeatureEx_Control_ch1.mat", "FeatureEx_Control_ch2.mat", "FeatureEx_Control_ch3.mat"]
load_and_process_features(control_files, 'ans_control.mat', (0, 16))

# Process FeatureEx_Control_L files
control_L_files = ["FeatureEx_Control_L_ch1.mat", "FeatureEx_Control_L_ch2.mat", "FeatureEx_Control_L_ch3.mat"]
load_and_process_features(control_L_files, 'ans_TL.mat', (0, 16))

# Clear all variables
del ans, control_files, control_L_files
