import numpy as np
from scipy.io import loadmat, savemat

# Placeholder functions for signal frequency feature extraction
def signal_frequency_feature_extractor(column, sample_rate=1024000):
    features = []
    mean_freq = np.mean(np.fft.fftfreq(len(column), 1/sample_rate))
    features.append(mean_freq)
    median_freq = np.median(np.fft.fftfreq(len(column), 1/sample_rate))
    features.append(median_freq)
    return features

def jLogTeagerKaiserEnergyOperator(X):
    N = len(X)
    Y = 0
    for j in range(1, N-1):
        Y += (X[j] ** 2) - (X[j-1] * X[j+1])
    return np.log(Y) if Y > 0 else 0

def jSlopeSignChange(X, opts=None):
    thres = opts.get('thres', 0.01) if opts else 0.01
    N = len(X)
    SSC = 0
    for k in range(1, N-1):
        if ((X[k] > X[k-1] and X[k] > X[k+1]) or (X[k] < X[k-1] and X[k] < X[k+1])) and \
           (abs(X[k] - X[k+1]) >= thres or abs(X[k] - X[k-1]) >= thres):
            SSC += 1
    return SSC

def jWaveformLength(X):
    N = len(X)
    WL = 0
    for k in range(1, N):
        WL += abs(X[k] - X[k-1])
    return WL

def jWillisonAmplitude(X, opts=None):
    thres = opts.get('thres', 0.01) if opts else 0.01
    N = len(X)
    WA = 0
    for k in range(N-1):
        if abs(X[k] - X[k+1]) > thres:
            WA += 1
    return WA

def jMeanAbsoluteValue(X):
    return np.mean(np.abs(X))

def FeatureExtractor(data):
    FeatureEx = []

    for cell in data:
        for col in range(1):
            column = cell[:, col]
            
            features = signal_frequency_feature_extractor(column)
            row_features = np.zeros(8)  # Adjust size as needed
            row_features[6] = features[0]
            row_features[7] = features[1]
            
            opts = {'thres': 5E-6}
            row_features[0] = jLogTeagerKaiserEnergyOperator(column)
            row_features[1] = jMeanAbsoluteValue(column)
            row_features[2] = jSlopeSignChange(column, opts)
            row_features[3] = jWaveformLength(column)
            row_features[4] = jWaveformLength(column)
            row_features[5] = jWillisonAmplitude(column, opts)
            
            FeatureEx.append(row_features)
    
    return np.array(FeatureEx)

# Define labels for Control and Control_L data
labels_control = np.concatenate([
    np.zeros(49625),
    np.ones(3464),
    2 * np.ones(18606),
    3 * np.ones(25752)
])

labels_control_L = np.concatenate([
    np.zeros(55888),
    np.ones(3929),
    2 * np.ones(17461),
    3 * np.ones(34069)
])

def process_files(mat_files, labels, output_file):
    FeatureEx = []

    for mat_file in mat_files:
        data = loadmat(mat_file)['data']
        features = FeatureExtractor(data)
        FeatureEx.append(features)

    FeatureEx = np.vstack(FeatureEx)
    FeatureEx = np.column_stack((FeatureEx, labels))
    savemat(output_file, {'FeatureEx': FeatureEx})

# Process Control Channel 1
control_ch1_files = [
    "NullDataControl_ch1.mat",
    "Control_Compiled_Data_ch1.mat",
    "CoughDataControl_ch1.mat",
    "SpeechDataControl_ch1.mat"
]
process_files(control_ch1_files, labels_control, 'FeatureEx_Control_Ch1.mat')

# Process Control Channel 2
control_ch2_files = [
    "NullDataControl_ch2.mat",
    "Control_Compiled_Data_ch2.mat",
    "CoughDataControl_ch2.mat",
    "SpeechDataControl_ch2.mat"
]
process_files(control_ch2_files, labels_control, 'FeatureEx_Control_Ch2.mat')

# Process Control Channel 3
control_ch3_files = [
    "NullDataControl_ch3.mat",
    "Control_Compiled_Data_ch3.mat",
    "CoughDataControl_ch3.mat",
    "SpeechDataControl_ch3.mat"
]
process_files(control_ch3_files, labels_control, 'FeatureEx_Control_Ch3.mat')

# Process Control_L Channel 1
control_L_ch1_files = [
    "NullDataControl_L_ch1.mat",
    "Control_Compiled_Data_L_ch1.mat",
    "CoughDataControl_L_ch1.mat",
    "SpeechDataControl_L_ch1.mat"
]
process_files(control_L_ch1_files, labels_control_L, 'FeatureEx_Control_L_Ch1.mat')

# Process Control_L Channel 2
control_L_ch2_files = [
    "NullDataControl_L_ch2.mat",
    "Control_Compiled_Data_L_ch2.mat",
    "CoughDataControl_L_ch2.mat",
    "SpeechDataControl_L_ch2.mat"
]
process_files(control_L_ch2_files, labels_control_L, 'FeatureEx_Control_L_Ch2.mat')

# Process Control_L Channel 3
control_L_ch3_files = [
    "NullDataControl_L_ch3.mat",
    "Control_Compiled_Data_L_ch3.mat",
    "CoughDataControl_L_ch3.mat",
    "SpeechDataControl_L_ch3.mat"
]
process_files(control_L_ch3_files, labels_control_L, 'FeatureEx_Control_L_Ch3.mat')
