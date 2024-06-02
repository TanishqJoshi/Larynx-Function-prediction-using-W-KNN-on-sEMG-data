# Larynx Function prediction using W-KNN on sEMG data
Key Points:

1. The study aimed to analyze surface electromyography (EMG) signals from the larynx of control participants and individuals with total laryngectomy (TL), encompassing four actions: swallowing, coughing, speaking, and random movements.

2. Data processing focused on the EMG-intercostal, EMG-submental, and EMG-diaphragm signals, utilizing a frame size of 128 ms with a 64 ms overlap.

3. A tunable Q-wavelet transform (TQWT) based filter bank was employed to decompose the signals into 40 elements, with signals containing more than 20% of the total signal energy being re-merged into a filtered signal.

4. The proposed method was evaluated on an open-source dataset, assessing its efficacy in classifying swallowing, coughing, speech, and null actions for both control and TL subjects.

5. Feature extraction yielded two frequency-based features (mean frequency and median frequency) and six time-domain features (Log Teager Kaiser Energy Operator, Mean Absolute Value, Slope Sign Change, Zero Crossing, Waveform Length, and Willison Amplitude).

6. A Weighted K-nearest neighbors (WKNN) approach was utilized for classification, achieving F1-scores of 82.82% (swallows), 68.15% (coughs), and 76.00% (speech) for control participants, and 53.30% (swallows), 63.95% (coughs), and 76.19% (speech) for the Total Laryngectomy group.

7. The study demonstrated significant improvements in the F1 scores for swallowing and speech classification in the control group, as well as a marginal improvement in the speech F1 score for the TL group.

Tech Stack:
<ul>
<li>Signal Processing Libraries: Libraries for signal processing and wavelet transformation, such as PyWavelets or MATLAB Wavelet Toolbox.</li>
<li>Machine Learning Libraries: Libraries for feature extraction, dimensionality reduction, and classification algorithms, such as scikit-learn and MATLAB Machine Learning Toolbox.</li>
<li>Data Management and Visualization: Libraries for data handling, preprocessing, and visualization, such as Pandas, NumPy, and Matplotlib.</li>
<li>Open-Source Dataset: The study utilized an open-source dataset for evaluation, potentially from a public repository or provided by a research institution.</li>
</ul>
