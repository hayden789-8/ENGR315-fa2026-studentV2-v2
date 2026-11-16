"""
CULMINATING ASSIGNMENT 3: Musical Note Detection

Create a program which detects the note being played from the given audio file based on its frequency.
It is up to you to employ an appropriate methodology to process the audio signal and detect the note.
The relevant data file is named "Guitar-note-1.wav" and is located in data > musical-notes.
In the same directory, we also provide a reference for the corresponding frequencies of each note.

Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
We have provided a possible method for converting the .wav file to usable data below.
All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""
#########Task 1***********
from scipy.io import wavfile

import numpy as np
import matplotlib.pyplot as plt

#read WAV file
sample_rate,audio=wavfile.read("data/musical-notes/Guitar-note-1.wav")

#time values
time=np.arange(len(audio))/sample_rate

#original audio graph
plt.figure(figsize=(10,5))
plt.plot(time,audio,color="blue",linewidth=0.5,label="Original Audio")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Audio Signal Over Time (Guitar Note 1)")
plt.legend(loc="upper right")
plt.grid(alpha=0.3)
plt.tight_layout()


###################task 2#####################

#signal processing functions
from scipy.signal import butter,sosfiltfilt

#filter audio
sos=butter(4,1000,btype="lowpass",fs=sample_rate,output="sos")
filtered=sosfiltfilt(sos,audio.astype(float))

#short section
start=int(0.3*sample_rate)
end=int(0.315*sample_rate)

#plot both signals
plt.figure(figsize=(10,5))
plt.plot(time[start:end],audio[start:end],label="Original Audio",alpha=0.6)
plt.plot(time[start:end],filtered[start:end],label="Filtered Audio")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original vs Filtered Audio (Guitar Note 1)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()





##############task 3#####################

import csv
from scipy.signal import find_peaks

#read frequency file
notes=[]
frequencies=[]

with open("data/musical-notes/note-frequencies-reference.csv") as file:
    reader=csv.reader(file)
    next(reader)
    next(reader)
    for row in reader:
        notes.append(row[0])
        frequencies.append(float(row[1]))

#print table headings
print(f"{'Audio File':<22}{'Frequency (Hz)':<20}{'Musical Note'}")
print("-"*55)

#analyze all guitar recordings
for i in range(1,6):

    #read audio file
    filename=f"Guitar-note-{i}.wav"
    rate,signal=wavfile.read("data/musical-notes/"+filename)

    #convert audio to mono
    if signal.ndim>1:
        signal=signal.mean(axis=1)

    #select short section of recording
    start=int(0.3*rate)
    end=int(0.5*rate)
    section=signal[start:end].astype(float)

    #low pass filter
    sos=butter(4,600,btype="lowpass",fs=rate,output="sos")
    filtered=sosfiltfilt(sos,section)

    #detect peaks in the filtered signal
    peaks,_=find_peaks(filtered,distance=int(rate/550),
                       prominence=0.3*np.std(filtered))

    #calculate average period
    periods=np.diff(peaks)/rate
    average_period=np.median(periods)

    #convert period to frequency
    detected=1/average_period

    #find closest musical note
    closest=np.argmin(np.abs(np.array(frequencies)-detected))
    note=notes[closest]

    #print results in table
    print(f"{filename:<22}{detected:<20.2f}{note}")

plt.show()
