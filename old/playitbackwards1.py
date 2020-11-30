import os
import sox
import sounddevice
import time
from playsound import playsound
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import *

#has to be set at the beginning of tkinter program root = Tk() // improt tkinter as tk
root = tk.Tk()

#Navigate to the home user directory for cody.
os.chdir('/home/cody/playitbackwards')

inputFileName = 'user1.wav'
#Grab the fourth character of the input file name to grab what user it's from.
i = inputFileName[4]

#Output file name with the correct output name for given user.
outputFileName = 'reverse' + i + '.wav'

screenHeight = 700
screenWidth = 800

#set the height and width of the window size.
canvas = tk.Canvas(root, height = screenHeight, width = screenWidth)
canvas.pack()

#set the frame(s) to determine color, size and position
frame = tk.Frame(root, bg='grey')
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

def startRecording1():
    fs = 44100
    second = 3
    print("Recording Audio for", second, "seconds")
    record_voice = sounddevice.rec(int(second * fs),samplerate = fs,channels = 2)
    sounddevice.wait()
    write(inputFileName, fs,record_voice)
    showPlayButton()

def playRecording1():
    print("Playing", outputFileName)
    playsound(inputFileName)

def showPlayButton():
    myLabel4.grid(row = 4, column = 0)
    playButton.grid(row = 5, column = 0)

#Creating a text label widget
myLabel1 = Label(root, text="Play It Backwards!")
myLabel2 = Label(root, text="by Cody DeLozier")
myLabel3 = Label(root, text="                  ")
myLabel4 = Label(root, text="                  ")

myButton = Button(root, text = "Start Recording", command=startRecording1)

playButton = Button(root, text = "Play It Backwards", command=playRecording1)

#Put label widget onto the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)
myLabel3.grid(row = 2, column = 0)
myButton.grid(row = 3, column = 0)

#main loop for tkinter gui program
root.mainloop()
