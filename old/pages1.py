import os
import sox
import sounddevice
import time
import random
from playsound import playsound
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

totalPlayers = 0
totalPlayersLoop = 0
totalPlayersPlayGame = 0
playerList = []
#function to show specified frame
def showFrame(frame):
    #show passed in frame
    frame.tkraise()

def addPlayer():
    global totalPlayers
    totalPlayers += 1
    ifEnoughPlayersForGame()
    if (totalPlayers > 4):
        global totalPlayersLoop
        if (totalPlayersLoop < 1):
            totalPlayersLoop += 1
            frame2_title7 = tk.Label(frame2, text = '', bg = '#080808')
            frame2_title7.pack(fill = 'x')
            frame2_maxPlayers = Label(frame2, text="Sorry, you have exceeded the maximum amount of players")
            frame2_maxPlayers.pack()
    else:
        global playerList
        frame2_playerLabel = Label(frame2, text=enterPlayerName.get())
        frame2_playerLabel.pack()
        playerName = enterPlayerName.get()
        playerList.append(playerName)
        #delete():
        #print(playerName)
        #print(playerList[2])

def ifEnoughPlayersForGame():
    global totalPlayers
    global totalPlayersPlayGame
    totalPlayersPlayGame += 1
    if (totalPlayers >= 1):
        if (totalPlayersPlayGame == 1):
            frame2_btn2 = tk.Button(frame2, text = 'Play Game', command=lambda:showFrame(frame3))
            frame2_btn2.pack(side = "bottom")

#def delete():
#    enterPlayerName.delete(1)

def startRecording1():
    for x in range(1):
        global playerList
        randomUser = random.randint(1,4) - 1
        print (randomUser)
        print (randomUser - 1)
        print(playerList[randomUser])
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
    frame3_title5 = tk.Label(frame3, text = '', bg = '#080808')
    frame3_title5.pack(fill = 'x')
    playButton.pack(side = "top")

#Navigate to the home user directory for cody.
os.chdir('/home/cody/playitbackwards')

inputFileName = 'user1.wav'
#Grab the fourth character of the input file name to grab what user it's from.
i = inputFileName[4]

#Output file name with the correct output name for given user.
outputFileName = 'reverse' + i + '.wav'
#has to be set at the beginning of tkinter program root = Tk() // improt tkinter as tk
window = tk.Tk()

#background_image = tk.PhotoImage(file='/home/cody/playitbackwards/bg.png')
#background_label = tk.Label(window, image = background_image)
#background_label.place(relwidth = 1, relheight = 1)

#load = Image.open('/home/cody/playitbackwards/bg.png')
#render = ImageTk.PhotoImage(load)
#img = Label(window, image = render)
#img.place(x = 0, y = 0)

#set the application window in full screen
#window.attributes('-zoomed', True)
#set the window resolution
window.geometry("800x700")

#Set the window so that the frame expands to example along with the window.
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)

frame1 = tk.Frame(window, bg = '#080808')
frame2 = tk.Frame(window, bg = '#080808')
frame3 = tk.Frame(window, bg = '#080808')

#loop to loop through frames
for frame in (frame1, frame2, frame3):
    #nsew = north sound east west
    frame.grid(row = 0, column = 0, sticky = 'nsew')

#-----------frame 1 code-------------#
frame1_title1 = tk.Label(frame1, text = '', bg = '#6600cc')
frame1_title1.pack(fill = 'x')
frame1_title2 = tk.Label(frame1, text = 'Say It Backwards!', bg = '#6600cc')
frame1_title2.pack(fill = 'x')
frame1_title3 = tk.Label(frame1, text = '', bg = '#6600cc')
frame1_title3.pack(fill = 'x')
frame1_title4 = tk.Label(frame1, text = '', bg = '#080808')
frame1_title4.pack(fill = 'x')
frame1_btn = tk.Button(frame1, text = 'Start Game', command = lambda:showFrame(frame2))
frame1_btn.pack()

#-----------frame 2 code-------------#
frame2_title1 = tk.Label(frame2, text = '', bg = '#6600cc')
frame2_title1.pack(fill = 'x')
frame2_title2 = tk.Label(frame2, text = 'Who are you playing with?', bg = '#6600cc')
frame2_title2.pack(fill = 'x')
frame2_title3 = tk.Label(frame2, text = '', bg = '#6600cc')
frame2_title3.pack(fill = 'x')
frame2_title4 = tk.Label(frame2, text = '', bg = '#080808')
frame2_title4.pack(fill = 'x')
enterPlayerName = Entry(frame2, width = 12)
enterPlayerName.pack()

frame2_title5 = tk.Label(frame2, text = '', bg = '#080808')
frame2_title5.pack(fill = 'x')
frame2_btn1 = tk.Button(frame2, text = 'Add Player', command=addPlayer)
frame2_btn1.pack()
frame2_title6 = tk.Label(frame2, text = '', bg = '#080808')
frame2_title6.pack(fill = 'x')



#-----------frame 3 code-------------#
frame3_title1 = tk.Label(frame3, text = '', bg = '#6600cc')
frame3_title1.pack(fill = 'x')
frame3_title2 = tk.Label(frame3, text = 'Say It Backwards!', bg = '#6600cc')
frame3_title2.pack(fill = 'x')
frame3_title3 = tk.Label(frame3, text = '', bg = '#6600cc')
frame3_title3.pack(fill = 'x')
frame3_title4 = tk.Label(frame3, text = '', bg = '#080808')
frame3_title4.pack(fill = 'x')
frame3_btn = tk.Button(frame3, text = 'Start Over', command=lambda:showFrame(frame1))
frame3_btn.pack(side = "bottom")

#Creating a text label widget
myButton = Button(frame, text = "Start Recording", command=startRecording1, bg = '#0099ff')
playButton = Button(frame, text = "Play It Backwards", command=playRecording1)

#Put label widget onto the screen
myButton.pack(side = "top")

#-----------frame 3 END code-------------#

showFrame(frame1)

window.mainloop()
