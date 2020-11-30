import os
import sox
import sounddevice
import time
from playsound import playsound
from scipy.io.wavfile import write

#Navigate to the home user directory for cody.
os.chdir('/home/cody/playitbackwards')

inputFileName = 'user1.wav'
#Grab the fourth character of the input file name to grab what user it's from.
i = inputFileName[4]

#Output file name with the correct output name for given user.
outputFileName = 'reverse' + i + '.wav'

fs = 44100
second = 3
print("Recording Audio for", second, "seconds")
record_voice = sounddevice.rec(int(second * fs),samplerate = fs,channels = 2)
sounddevice.wait()
write(inputFileName, fs,record_voice)

#Set TFM to the sox.transformer()
tfm = sox.Transformer()

#Call the reverse function within Sox.
tfm.reverse()

#Take in input file, export to home directory.
tfm.build(inputFileName, outputFileName)

print('The', inputFileName, 'file was reversed and saved as the', outputFileName, 'file.')

print("Playing back sound in reverse!")
playsound(outputFileName)
print("One more time in case you missed it!")
time.sleep(0.5)
playsound(outputFileName)

print("Now try to say it backwards!")
time.sleep(0.5)
print("GO!")
record_voice = sounddevice.rec(int(second * fs),samplerate = fs,channels = 2)
sounddevice.wait()
write(inputFileName, fs,record_voice)

#Set TFM to the sox.transformer()
tfm = sox.Transformer()

#Call the reverse function within Sox.
tfm.reverse()

#Take in input file, export to home directory.
tfm.build(inputFileName, outputFileName)

print('The', inputFileName, 'file was reversed and saved as the', outputFileName, 'file.')

time.sleep(0.5)

playsound(outputFileName)

time.sleep(0.5)

playsound(outputFileName)
