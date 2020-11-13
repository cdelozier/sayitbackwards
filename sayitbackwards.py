import os
import sox
import sounddevice
import time
import random
#from pygame import mixer
#import pygame
import simpleaudio as sa
from playsound import playsound
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#define global variables
totalPlayers = 0
totalPlayersLoop = 0
totalPlayersPlayGame = 0
playerList = []
playerCountIterator = 0
firstPick = ""
#Function to show specified frame
def showFrame(frame):
    #show passed in frame
    frame.tkraise()

def showFrameAndFunction(frame):
    #show passed in frame
    displayPlayerNames()
    frame.tkraise()
#--------------------FRAME TWO FUNCTIONS START--------------------#

#Add player function to control the add player menu and max number of players.
def addPlayer():
    global totalPlayers
    global playerList
    #Assign PlayerName to the currently entered value.
    playerName = enterPlayerName.get()
    whoAreYouPlayingWithTitle.config(text="Who are you playing with?")
    #Check the length of the name entered to ensure it is atleast 1.
    if ((len(playerName)) < 1):
        whoAreYouPlayingWithTitle.config(text="Please enter a name with atleast one character.")
        return
    if ((len(playerName)) > 12):
        frame2_title7 = tk.Label(frame2, text = '', bg = '#080808')
        frame2_title7.pack(fill = 'x')
        frame3BlackFiller = tk.Label(frame2, text = '', bg = '#080808', font=("Courier", 20))
        frame3BlackFiller.pack(fill = 'x', side = "bottom")
        whoAreYouPlayingWithTitle.config(text="Sorry, try a shorter name.")
        return

    for players in playerList:
        print (players[0])
        if players == playerName:
            whoAreYouPlayingWithTitle.config(text="Sorry that name is already taken.")
            return

    totalPlayers += 1
    #Call this function to make sure there is atleast one player before displaying play button.
    ifEnoughPlayersForGame()
    #If max number of players has been reached.
    if (totalPlayers > 4):
        global totalPlayersLoop
        #This code runs one time to inform the user the max number of players has been met.
        if (totalPlayersLoop < 1):
            totalPlayersLoop += 1
            frame2_title7 = tk.Label(frame2, text = '', bg = '#080808')
            frame2_title7.pack(fill = 'x')
            frame2_maxPlayers = Label(frame2, text="Sorry, you have exceeded the maximum amount of players", bg = '#080808', fg = 'white', font=("Courier", 17))
            frame2_maxPlayers.pack()
    else:
        #global playerList
        frame2_playerLabel = Label(frame2, text=enterPlayerName.get(), bg = '#080808', fg = 'white', font=("Courier", 30))
        frame2_playerLabel.pack()
        #append entered player names at the end of the PlayerList list.
        playerList.append(playerName)
    #clear the text box in the program to remove previously entered name.
    enterPlayerName.delete(0, END)

#Function to detect if the enter key was pressed.
def enterKeyPress(event):
    addPlayer()

#Check to see if there is atleast one player before displaying the play button
def ifEnoughPlayersForGame():
    global totalPlayers
    global totalPlayersPlayGame
    totalPlayersPlayGame += 1
    if (totalPlayers >= 1):
        if (totalPlayersPlayGame == 1):
            frame2BlackFiller = tk.Label(frame2, text = '', bg = '#080808', font=("Courier", 20))
            frame2BlackFiller.pack(fill = 'x', side = "bottom")
            frame2PlayGameButton = tk.Button(frame2, text = 'Play Game', font=("Courier", 20), bg = '#0099ff', command=playGame)
            frame2PlayGameButton.pack(side = "bottom")

#Clear the text entry box after each entry
def delete():
    enterPlayerName.delete(0, END)

def playGame():
    showFrame(frame3)
    displayRandomUser()

#--------------------FRAME THREE FUNCTIONS START --------------------#
def displayRandomUser():
    global playerList
    global firstPick
    listIndex = (len(playerList))
    #Get random player
    for x in range(1):
        randomUser = (random.randint(1,listIndex)) - 1
        firstPick = playerList[randomUser]
        firstPickString = firstPick + " records first!"
    frame3Title5 = tk.Label(frame3, text = '', bg = '#080808')
    frame3Title5.pack(fill = 'x')
    frame3Title5 = tk.Label(frame3, text = firstPickString, bg = '#080808', fg = 'white', font= ("Courier", 30))
    frame3Title5.pack(side = "top")
    frame3Title5 = tk.Label(frame3, text = '', bg = '#080808')
    frame3Title5.pack(fill = 'x')
    startRecordingButtonF3.pack(side = "top")
    frame3BlackFiller = tk.Label(frame3, text = '', bg = '#080808', font=("Courier", 20))
    frame3BlackFiller.pack(fill = 'x', side = "bottom")
    frame2PlayGameButton = tk.Button(frame2, text = 'Play Game', font=("Courier", 20), bg = '#0099ff', command=playGame)
    frame2PlayGameButton.pack(side = "bottom")


def displayPlayerNames():
    #showFrame(frame3)
    global playerCountIterator
    #Check for how many players there are and display them on frame 3 accordingly.
    for players in playerList:
        playerCountIterator += 1
        frame3Title5 = tk.Label(frame4, text = '', bg = '#080808')
        frame3Title5.pack(fill = 'x')
        frame3_title6 = tk.Label(frame4, text = playerList[playerCountIterator - 1], bg = '#080808', fg = 'white', font=("Courier", 30))
        frame3_title6.pack(fill = 'x')

def firstRecording():
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
    #Change text of button after it is pressed
    startRecordingButtonF3.config(text="Click To Retake")
    showFirstRecordingPlayButton()
    playGameButtonF3.pack(side = "bottom")

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
    frame3Title5 = tk.Label(frame3, text = '', bg = '#080808')
    frame3Title5.pack(fill = 'x')
    showPlayButton()

def showFirstRecordingPlayButton():
    global firstPick
    frame3BlackFiller = tk.Label(frame4, text = '', bg = '#080808', font=("Courier", 20))
    frame3BlackFiller.pack(fill = 'x', side = "top")
    playReversedWordText = "Play " + firstPick + "'s word in reverse"
    frame3BlackFiller = tk.Label(frame3, text = '', bg = '#080808', font=("Courier", 20))
    frame3BlackFiller.pack(fill = 'x', side = "top")
    playButtonF3 = Button(frame3, text = playReversedWordText, font=("Courier", 20), command=playRecording1, bg = '#0099ff')
    playButtonF3.pack(side = "top")

#Show play it backwards button once recording has finished.
def showPlayButton():
    frame3Title5 = tk.Label(frame3, text = '', bg = '#080808')
    frame3Title5.pack(fill = 'x', side = "bottom")
    playButtonF3.pack(side = "top")

#Play recording after it has been reversed.
def playRecording1():
    playsound(outputFileName)

def restart_program():
    """Restarts the current program."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Navigate to the home user directory for cody.
os.chdir('/home/cody/playitbackwards')

inputFileName = 'user1.wav'
#Grab the fourth character of the input file name to grab what user it's from.
i = inputFileName[4]

#Output file name with the correct output name for given user.
outputFileName = 'reverse' + i + '.wav'
#has to be set at the beginning of tkinter program root = Tk() // improt tkinter as tk
window = tk.Tk()

#Bind the return key to the window to later use when entering information with the enter key.
window.bind('<Return>', enterKeyPress)

#set the application window in full screen
window.attributes('-zoomed', True)

#set the window resolution
canvas = Canvas(window, width = 800, height = 700)
window.geometry("800x700")

#Set the window so that the frame expands to example along with the window.
window.title("Say It Backwards App")
window.configure(background='black')
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)

frame1 = tk.Frame(window, bg = '#080808')
frame2 = tk.Frame(window, bg = '#080808')
frame3 = tk.Frame(window, bg = '#080808')
frame4 = tk.Frame(window, bg = '#080808')

#loop to loop through frames
for frame in (frame1, frame2, frame3, frame4):
    #nsew = north sound east west
    frame.grid(row = 0, column = 0, sticky = 'nsew')

#-----------frame 1 code-------------#
frame1_title1 = tk.Label(frame1, text = '', bg = '#6600cc')
frame1_title1.pack(fill = 'x')
frame1_title2 = tk.Label(frame1, text = 'Say It Backwards!', bg = '#6600cc', font=("Courier", 23))
frame1_title2.pack(fill = 'x')
frame1_title3 = tk.Label(frame1, text = '', bg = '#6600cc')
frame1_title3.pack(fill = 'x')
frame1_title4 = tk.Label(frame1, text = '', bg = '#080808', font=("Courier", 20))
frame1_title4.pack(fill = 'x')
frame1_btn = tk.Button(frame1, text = 'Start Game', font=("Courier", 20), bg = '#0099ff', command = lambda:showFrame(frame2))
frame1_btn.pack()

#-----------frame 2 code-------------#
frame2_title1 = tk.Label(frame2, text = '', bg = '#6600cc')
frame2_title1.pack(fill = 'x')
whoAreYouPlayingWithTitle = tk.Label(frame2, text = 'Who are you playing with?', bg = '#6600cc', font=("Courier", 23))
whoAreYouPlayingWithTitle.pack(fill = 'x')
frame2_title3 = tk.Label(frame2, text = '', bg = '#6600cc')
frame2_title3.pack(fill = 'x')
frame2BlackFiller = tk.Label(frame2, text = '', bg = '#080808', font=("Courier", 20))
frame2BlackFiller.pack(fill = 'x')
enterPlayerName = Entry(frame2, width = 12, font=("Courier", 30))
enterPlayerName.pack()
frame2_title5 = tk.Label(frame2, text = '', bg = '#080808', font=("Courier", 20))
frame2_title5.pack(fill = 'x')
frame2_btn1 = tk.Button(frame2, text = 'Add Player', font=("Courier", 20), command=addPlayer, bg = '#0099ff')
frame2_btn1.pack()
frame2_title6 = tk.Label(frame2, text = '', bg = '#080808')
frame2_title6.pack(fill = 'x')

#-----------frame 3 code-------------#
frame3_title1 = tk.Label(frame3, text = '', bg = '#6600cc')
frame3_title1.pack(fill = 'x')
frame3_title2 = tk.Label(frame3, text = "Who's up first?", bg = '#6600cc', font=("Courier", 23))
frame3_title2.pack(fill = 'x')
frame3_title3 = tk.Label(frame3, text = '', bg = '#6600cc')
frame3_title3.pack(fill = 'x')
frame3_title4 = tk.Label(frame3, text = '', bg = '#080808')
frame3_title4.pack(fill = 'x')


#Creating a text label widget
startRecordingButtonF3 = Button(frame3, text = "Start Recording", font=("Courier", 20), command=firstRecording, bg = '#0099ff')
playButtonF3 = Button(frame3, text = "Play It Backwards", font=("Courier", 20), command=playRecording1, bg = '#0099ff')
playGameButtonF3 = tk.Button(frame3, text = 'Start Round', font=("Courier", 20), bg = '#0099ff', command = lambda:showFrameAndFunction(frame4))

#-----------frame 3 END code-------------#

#-----------frame 4 START code-------------#
frame4_title1 = tk.Label(frame4, text = '', bg = '#6600cc')
frame4_title1.pack(fill = 'x')
frame4_title2 = tk.Label(frame4, text = 'Say It Backwards!', bg = '#6600cc', font=("Courier", 23))
frame4_title2.pack(fill = 'x')
frame4_title3 = tk.Label(frame4, text = '', bg = '#6600cc')
frame4_title3.pack(fill = 'x')
frame4_title4 = tk.Label(frame4, text = '', bg = '#080808')
frame4_title4.pack(fill = 'x')
frame4BlackFiller = tk.Label(frame4, text = '', bg = '#080808', font=("Courier", 20))
frame4BlackFiller.pack(fill = 'x', side = "bottom")
frame4_btn = tk.Button(frame4, text = 'Start Over', font=("Courier", 20), bg = '#800000', command=restart_program)
frame4_btn.pack(side = "bottom")

#Creating a text label widget
startRecordingButtonF4 = Button(frame4, text = "Start Recording", font=("Courier", 20), command=startRecording1, bg = '#0099ff')
playButtonF4 = Button(frame4, text = "Play It Backwards", font=("Courier", 20), command=playRecording1, bg = '#0099ff')
#-----------frame 4 END code-------------#

showFrame(frame1)

window.mainloop()
