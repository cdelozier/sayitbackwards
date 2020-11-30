import os
import sox
import sounddevice
import time
from playsound import playsound
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import *

#testing for GitHub push
#has to be set at the beginning of tkinter program root = Tk() // improt tkinter as tk
root = tk.Tk()

background_image = tk.PhotoImage(file='/home/cody/playitbackwards/bg.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

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
frame = tk.Frame(root)#, bg='grey')
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

def startRecording1():
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
    showPlayButton()

def playRecording1():
    print("Playing", outputFileName)
    playsound(outputFileName)

def showPlayButton():
    myLabel4.pack(side = "top")
    playButton.pack(side = "top")

#Creating a text label widget
myLabel1 = Label(frame, text="Play It Backwards!")
myLabel2 = Label(frame, text="by Cody DeLozier")
myLabel3 = Label(frame, text="")
myLabel4 = Label(frame, text="                  ")

myButton = Button(frame, text = "Start Recording", command=startRecording1)

playButton = Button(frame, text = "Play It Backwards", command=playRecording1)

#Put label widget onto the screen
myLabel1.pack(side = "top")
myLabel2.pack(side = "top")
myLabel3.pack(side = "top")
myButton.pack(side = "top")

#main loop for tkinter gui program
root.mainloop()
