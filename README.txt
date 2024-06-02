Notes on dataset:

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

P1-5: Control participants
P6-10: Laryngectomy participants

3 recording sessions for each participant

During each session the following were recorded:

    15 recordings of swallowing: 5 dry; 5 water; 5 solid (e.g. banana or biscuit).
    3 recordings of coughing, with each recording containing 5 coughs.
    3 recordings of speech, in which the participant read aloud 10 sentences from the Harvard sentences (IEEE, "IEEE Recommended Practice for Speech Quality Measurements, " IEEE Trans. Audio Electroacoust., vol. 17, no. 3, pp. 225-246, 1969).
    6 recordings of movements typical of daily life (standing, sitting, reaching, twisting and walking).

Additionally, high speed video was recorded during swallowing, pneumotachometry during coughing and sound during speech.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Data is structured as follows:

If there are 6 columns:

EMG-intercostal,EMG-submental,pneumotachometry,EMG-diaphragm,trigger,microphone
mV,mV,cmH20,mV,N/A,V

If there are 7 columns:

EMG-intercostal,EMG-submental,pneumotachometry,EMG-diaphragm,pressure,trigger,microphone
mV,mV,cmH20,mV,V,N/A,V

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sampling rate for EMG, pneumotachometry & sound = 2000 Hz

Conversion from cmH20 to L/min: L/min = cmH20 x 479

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Each session folder contains a subfolder "swallowTimes". This contains the timestamps (given in samples) of each swallow in a recording, based on the high speed video data.
First column is Onset, second column is Offset.
Protocol specified just 1 swallow per recording, but on occassion participants may have attempted multiple.
Timestamps are subjective, and have only been determined by one assessor.
Video data and sEMG started at same time, but did not end at same time (if a video timestamp exceeds length of sEMG it can be ignored).

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Protocol specified 5 coughs per recodings, but in some cases a different number is present. Pneumotachometry is corrupted in a small number of recordings.
Cough recordings titled "with_box" indicate use of a device with pressure threshold. The participant aimed to exceed this threshold with their cough, to open the device.
In pneumotachometry data: Positive values = exhalation, negative values = inhalation.
