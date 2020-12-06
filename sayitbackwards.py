import os
import sox
import sounddevice
import time
import random
import pygame
from pygame import mixer
import simpleaudio as sa
from playsound import playsound
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import Tk, font
from PIL import Image, ImageTk

#define global variables
totalPlayers = 0
totalPlayersLoop = 0
totalPlayersPlayGame = 0
playerList = []
playerCountIterator = 0
firstPick = ""
firstRecordingIterator = 0
fs = 48000
second = 2.5
playReversedWordText = ""

#html colors:
background = '#0c2c3b'
background2 = '#00131c'
yellow = '#dbbd35'
font = 'Comic Sans'
white ='white'

#Function to show specified frame
def showFrame(frame):
    #show passed in frame
    frame.tkraise()

def showFrameAndFunction(frame):
    #show passed in frame
    chimeSound.play()
    displayFrameThreeData()
    frame.tkraise()
#--------------------FRAME TWO FUNCTIONS START--------------------#

#Add player function to control the add player menu and max number of players.
def addPlayer():
    global totalPlayers
    global playerList
    #Assign PlayerName to the currently entered value.
    playerName = enterPlayerName.get()

    if totalPlayers < 5:
        whoAreYouPlayingWithTitle.config(text="Who are you playing with?")
    #Check the length of the name entered to ensure it is atleast 1.
    if ((len(playerName)) < 1 and totalPlayers < 4):
        menuClickSound.play()
        whoAreYouPlayingWithTitle.config(text="Please enter a name with at least one character.")
        return
    if ((len(playerName)) > 12):
        menuClickSound.play()
        frame2_title7 = tk.Label(frame2, text = '', bg = background)
        frame2_title7.pack(fill = 'x')
        frame3BlackFiller = tk.Label(frame2, text = '', bg = background, font=(font, 20))
        frame3BlackFiller.pack(fill = 'x', side = "bottom")
        whoAreYouPlayingWithTitle.config(text="Sorry, try a shorter name.")
        return

    for players in playerList:
        if players == playerName and totalPlayers < 4:
            menuClickSound.play()
            whoAreYouPlayingWithTitle.config(text="Sorry that name is already taken.")
            return

    if (totalPlayers < 4):
        if totalPlayers == 0:
            dingSound1.play()
        elif totalPlayers == 1:
            dingSound2.play()
        elif totalPlayers == 2:
            dingSound3.play()
        else:
            dingSound4.play()

    totalPlayers += 1
    if totalPlayers > 0 and totalPlayers < 5:
        playerCountTitleText = str(totalPlayers) +"/4 players"
        playerCountTitle.config(text=playerCountTitleText, fg = 'white', font=(font, 30))
    #Call this function to make sure there is atleast one player before displaying play button.
    ifEnoughPlayersForGame()
    #If max number of players has been reached.
    if (totalPlayers > 4):
        global totalPlayersLoop
        #This code runs one time to inform the user the max number of players has been met.
        if (totalPlayersLoop < 1):
            totalPlayersLoop += 1
            menuClickSound.play()
            frame2_title7 = tk.Label(frame2, text = '', bg = background)
            frame2_title7.pack(fill = 'x')
            whoAreYouPlayingWithTitle.config(text="Sorry, you have exceeded the maximum amount of players")
    else:
        frame2_playerLabel = Label(frame2, text=enterPlayerName.get(), bg = background, fg = 'white', font=(font, 30))
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
            frame2BlackFiller = tk.Label(frame2, text = '', bg = background, font=(font, 20))
            frame2BlackFiller.pack(fill = 'x', side = "bottom")
            frame2PlayGameButton = tk.Button(frame2, image = PlayGameButton, text = 'Play Game', font=(font, 20), command=playGame, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
            frame2PlayGameButton.pack(side = "bottom")

#Clear the text entry box after each entry
def delete():
    enterPlayerName.delete(0, END)

def playGame():
    chimeSound.play()
    showFrame(frame3)
    pygame.mixer.music.fadeout(2500)
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

    #Pick random word from wordlist
    lines = open('wordlist/randomwordlist.txt').read().splitlines()
    myline =random.choice(lines)
    randomWordText = "Try: " + myline
    frame3Title5 = tk.Label(frame3, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    frame3Title5 = tk.Label(frame3, text = firstPickString, bg = background, fg = 'white', font= (font, 30))
    frame3Title5.pack(side = "top")
    frame3Title5 = tk.Label(frame3, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    frame3Title5 = tk.Label(frame3, text = "Think of a word and record yourself", bg = background, fg = 'white', font= (font, 26))
    frame3Title5.pack(side = "top")
    frame3Title5 = tk.Label(frame3, text = '', bg = background, font= (font, 30))
    frame3Title5.pack(fill = 'x')
    frame3Title5 = tk.Label(frame3, text = "Can't think of a word?", bg = background, fg = 'white', font= (font, 16, "underline"))
    frame3Title5.pack(side = "top")
    frame3Title5 = tk.Label(frame3, text = randomWordText, bg = background, fg = 'white', font= (font,18, "italic"))
    frame3Title5.pack(side = "top")
    frame3Title5 = tk.Label(frame3, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    startRecordingButtonF3.pack(side = "top")
    frame3BlackFiller = tk.Label(frame3, text = '', bg = background, font=(font, 20))
    frame3BlackFiller.pack(fill = 'x', side = "bottom")
    frame2PlayGameButton = tk.Button(frame2, image = PlayGameButton, text = 'Play Game', font=(font, 20), bg = yellow, command=playGame)
    frame2PlayGameButton.pack(side = "bottom")

def firstRecording():
    global fs
    global second
    bingSound1.play()
    print("Recording " + firstPick + "'s Audio for", second, "seconds")
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
    startRecordingButtonF3.config(image = RetakeButton, text="Retake", bg = background)
    bingSound2.play()
    showFirstRecordingPlayButton()
    playGameButtonF3.pack(side = "bottom")

def displayFrameThreeData():
    #showFrame(frame3)
    global playerCountIterator
    global playReversedWordText
    #Check for how many players there are and display them on frame 3 accordingly.
    frame4_title2 = tk.Label(frame4, text = "Original Word:", bg = background, fg = 'white', font=(font, 30))
    frame4_title2.pack()
    playButtonF3.pack()
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    frame3_title6 = tk.Label(frame4, text = playerList[0], bg = background, fg = 'white', font=(font, 30))
    frame3_title6.pack(fill = 'x')
    startRecordingButtonF4User1 = Button(frame4, image = RecordButton, text = "Record", font=(font, 20), command=user1Recording, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
    startRecordingButtonF4User1.pack()
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    playButtonF4User1 = Button(frame4, image = PlayImageButton, text = "Play", font=(font, 20), command=playUser1ReversedAudio, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
    playerCountIterator += 1;

def user1Recording():
    global playerCountIterator
    global fs
    global second
    bingSound1.play()
    print("Recording Audio for", second, "seconds")
    record_voice = sounddevice.rec(int(second * fs),samplerate = fs,channels = 2)
    sounddevice.wait()
    write("user1Recording.wav", fs,record_voice)
    #Set TFM to the sox.transformer()
    tfm = sox.Transformer()
    #Call the reverse function within Sox.
    tfm.reverse()
    #Take in input file, export to home directory.
    tfm.build("user1Recording.wav", "user1Reverse.wav")
    bingSound2.play()
    playButtonF4User1.pack()
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    if (len(playerList)) > 1 and playerCountIterator == 1:
        #frame3Title5 = tk.Label(frame4, text = '', bg = background)
        #frame3Title5.pack(fill = 'x')
        frame3_title6 = tk.Label(frame4, text = playerList[1], bg = background, fg = 'white', font=(font, 30))
        frame3_title6.pack(fill = 'x')
        startRecordingButtonF4User2 = Button(frame4, image = RecordButton, text = "Record", font=(font, 20), command=user2Recording, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        startRecordingButtonF4User2.pack()
        playButtonF4User2 = Button(frame4, image = PlayImageButton, text = "Play", font=(font, 20), command=playUser2ReversedAudio, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        playerCountIterator += 1;

def user2Recording():
    global playerCountIterator
    global fs
    global second
    bingSound1.play()
    print("Recording Audio for", second, "seconds")
    record_voice = sounddevice.rec(int(second * fs),samplerate = fs,channels = 2)
    sounddevice.wait()
    write("user2Recording.wav", fs,record_voice)
    #Set TFM to the sox.transformer()
    tfm = sox.Transformer()
    #Call the reverse function within Sox.
    tfm.reverse()
    #Take in input file, export to home directory.
    tfm.build("user2Recording.wav", "user2Reverse.wav")
    bingSound2.play()
    playButtonF4User2.pack()
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    if (len(playerList)) > 2 and playerCountIterator == 2:
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        frame3_title6 = tk.Label(frame4, text = playerList[2], bg = background, fg = 'white', font=(font, 30))
        frame3_title6.pack(fill = 'x')
        startRecordingButtonF4User3 = Button(frame4, image = RecordButton, text = "Record", font=(font, 20), command=user3Recording, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        startRecordingButtonF4User3.pack()
        playButtonF4User3 = Button(frame4, image = playButtonF4User4, text = "Play", font=(font, 20), command=playUser3ReversedAudio, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        playerCountIterator += 1;

def user3Recording():
    global playerCountIterator
    global fs
    global second
    bingSound1.play()
    print("Recording Audio for", second, "seconds")
    record_voice = sounddevice.rec(int(second * fs),samplerate = fs,channels = 2)
    sounddevice.wait()
    write("user3Recording.wav", fs,record_voice)
    #Set TFM to the sox.transformer()
    tfm = sox.Transformer()
    #Call the reverse function within Sox.
    tfm.reverse()
    #Take in input file, export to home directory.
    tfm.build("user3Recording.wav", "user3Reverse.wav")
    bingSound2.play()
    playButtonF4User3.pack()
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    if (len(playerList)) > 3 and playerCountIterator == 3:
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        frame3_title6 = tk.Label(frame4, text = playerList[3], bg = background, fg = 'white', font=(font, 30))
        frame3_title6.pack(fill = 'x')
        startRecordingButtonF4User4 = Button(frame4, image = RecordButton, text = "Record", font=(font, 20), command=user4Recording, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        startRecordingButtonF4User4.pack()
        playButtonF4User4 = Button(frame4, image=PlayImageButton, text = "Play", font=(font, 20), command=playUser4ReversedAudio, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        playerCountIterator += 1;

def user4Recording():
    global playerCountIterator
    global fs
    global second
    print("Recording Audio for", second, "seconds")
    record_voice = sounddevice.rec(int(second * fs),samplerate = fs,channels = 2)
    sounddevice.wait()
    write("user4Recording.wav", fs,record_voice)
    #Set TFM to the sox.transformer()
    tfm = sox.Transformer()
    #Call the reverse function within Sox.
    tfm.reverse()

    #Take in input file, export to home directory.
    tfm.build("user4Recording.wav", "user4Reverse.wav")
    playButtonF4User4.pack()
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')

def startRecording1():
    fs = 44100
    second = 2.5
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
    frame3Title5 = tk.Label(frame3, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    showPlayButton()

def showFirstRecordingPlayButton():
    global firstPick
    global firstRecordingIterator
    global playReversedWordText
    frame3BlackFiller = tk.Label(frame4, text = '', bg = background, font=(font, 20))
    frame3BlackFiller.pack(fill = 'x', side = "top")
    playReversedWordText = "Play " + firstPick + "'s word in reverse:"
    frame3BlackFiller = tk.Label(frame3, text = '', bg = background, font=(font, 50))
    frame3BlackFiller.pack(fill = 'x', side = "top")
    frame3_title2 = tk.Label(frame3, text = playReversedWordText, bg = background, fg = 'white', font=(font, 30))
    rame3BlackFiller = tk.Label(frame4, text = '', bg = background, font=(font, 20))
    frame3BlackFiller.pack(fill = 'x', side = "top")
    playButtonF3 = Button(frame3, image = PlayImageButton, text = "Play", font=(font, 20), command=playRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
    if firstRecordingIterator < 1:
        firstRecordingIterator+=1
        frame3_title2.pack()
        playButtonF3.pack()

#Show play it backwards button once recording has finished.
def showPlayButton():
    frame3Title5 = tk.Label(frame3, text = '', bg = background)
    frame3Title5.pack(fill = 'x', side = "bottom")
    playButtonF3.pack(side = "top")

#Play recording after it has been reversed.
def playRecording1():
    playsound(outputFileName)

def playUser1ReversedAudio():
    playsound("user1Reverse.wav")
def playUser2ReversedAudio():
    playsound("user2Reverse.wav")
def playUser3ReversedAudio():
    playsound("user3Reverse.wav")
def playUser4ReversedAudio():
    playsound("user4Reverse.wav")

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
window.title("Say It Backwards")
window.configure(background=background)
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)

frame1 = tk.Frame(window, bg = background)
frame2 = tk.Frame(window, bg = background)
frame3 = tk.Frame(window, bg = background)
frame4 = tk.Frame(window, bg = background)

#rounded button png'
startGameButton = PhotoImage(file='photos/Start_Game.png')
startRoundButton = PhotoImage(file='photos/Start_Round.png')
RecordButton = PhotoImage(file='photos/Record.png')
PlayGameButton = PhotoImage(file='photos/Play_Game.png')
AddPlayerButton= PhotoImage(file='photos/Add_Player.png')
PlayImageButton = PhotoImage(file='photos/Play.png')
RetakeButton = PhotoImage(file='photos/Retake.png')
StartOverButton = PhotoImage(file='photos/Start_Over.png')
gameLogo = PhotoImage(file='photos/logo.png')

#loop to loop through frames
for frame in (frame1, frame2, frame3, frame4):
    #nsew = north sound east west
    frame.grid(row = 0, column = 0, sticky = 'nsew')

#-----------frame 1 code-------------#
frame1_title4 = tk.Label(frame1, image=gameLogo, text = '', bg = background)
frame1_title4.pack()
frame1_title2 = tk.Label(frame1, text = 'by Cody DeLozier', bg = background, fg = white, font=(font, 12,'italic'))
frame1_title2.pack(fill = 'x')
frame1_title4 = tk.Label(frame1, text = '', bg = background, font=(font, 30))
frame1_title4.pack(fill = 'x')
frame1_btn = tk.Button(frame1, image=startGameButton, text = 'Start Game', fg = background, font=(font, 20), bg = background, activebackground=background, command = lambda:showFrame(frame2), borderwidth=0, highlightthickness=0)
frame1_btn.pack()

#-----------frame 2 code-------------#
frame2_title1 = tk.Label(frame2, text = '', bg = background2)
frame2_title1.pack(fill = 'x')
whoAreYouPlayingWithTitle = tk.Label(frame2, text = 'Who are you playing with?', bg = background2, fg = white, font=(font, 30, 'italic'))
whoAreYouPlayingWithTitle.pack(fill = 'x')
frame2_title3 = tk.Label(frame2, text = '', bg = background2)
frame2_title3.pack(fill = 'x')
frame2BlackFiller = tk.Label(frame2, text = '', bg = background, font=(font, 20))
frame2BlackFiller.pack(fill = 'x')
enterPlayerName = Entry(frame2, width = 12, font=(font, 30))
enterPlayerName.pack()
frame2_title5 = tk.Label(frame2, text = '', bg = background, font=(font, 20))
frame2_title5.pack(fill = 'x')
frame2_btn1 = tk.Button(frame2, image=AddPlayerButton, text = 'Add Player', font=(font, 20), command=addPlayer, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
frame2_btn1.pack()
frame2BlackFiller = tk.Label(frame2, text = '', bg = background, font=(font, 20))
frame2BlackFiller.pack(fill = 'x')
playerCountTitle = tk.Label(frame2, text = '', bg = background, font=(font, 23))
playerCountTitle.pack()
frame2_title6 = tk.Label(frame2, text = '', bg = background)
frame2_title6.pack(fill = 'x')

#-----------frame 3 code-------------#
frame3_title1 = tk.Label(frame3, text = '', bg = background2)
frame3_title1.pack(fill = 'x')
frame3_title2 = tk.Label(frame3, text = "Who's up first?", bg = background2, fg = white, font=(font, 30, 'italic'))
frame3_title2.pack(fill = 'x')
frame3_title3 = tk.Label(frame3, text = '', bg = background2)
frame3_title3.pack(fill = 'x')
frame3_title4 = tk.Label(frame3, text = '', bg = background)
frame3_title4.pack(fill = 'x')


#Creating a text label widget
startRecordingButtonF3 = Button(frame3, image=RecordButton, text = "Record", font=(font, 20), command=firstRecording, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
playButtonF3 = Button(frame3, text = "Play It Backwards", font=(font, 20), command=playRecording1, bg = yellow)
playGameButtonF3 = tk.Button(frame3, image = startRoundButton, text = 'Start Round', font=(font, 20), command = lambda:showFrameAndFunction(frame4), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)

#-----------frame 3 END code-------------#

#-----------frame 4 START code-------------#
frame4_title1 = tk.Label(frame4, text = '', bg = background2)
frame4_title1.pack(fill = 'x')
frame4_title2 = tk.Label(frame4, text = 'Round 1', bg = background2, fg = white, font=(font, 30, 'italic'))
frame4_title2.pack(fill = 'x')
frame4_title3 = tk.Label(frame4, text = '', bg = background2)
frame4_title3.pack(fill = 'x')
frame4_title4 = tk.Label(frame4, text = '', bg = background)
frame4_title4.pack(fill = 'x')
playButtonF3 = Button(frame4, image = PlayImageButton, text = "Play", font=(font, 20), command=playRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
playButtonF4User1 = Button(frame4, image = PlayImageButton, text = "Play", font=(font, 20), command=playUser1ReversedAudio, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
playButtonF4User2 = Button(frame4, image = PlayImageButton,text = "Play", font=(font, 20), command=playUser2ReversedAudio, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
playButtonF4User3 = Button(frame4, image = PlayImageButton,text = "Play", font=(font, 20), command=playUser3ReversedAudio, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
playButtonF4User4 = Button(frame4, image = PlayImageButton,text = "Play", font=(font, 20), command=playUser4ReversedAudio, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
frame4BlackFiller = tk.Label(frame4, text = '', bg = background, font=(font, 20))
frame4BlackFiller.pack(fill = 'x', side = "bottom")
frame4_btn = tk.Button(frame4, image = StartOverButton, text = 'Start Over', font=(font, 20), command=restart_program, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
frame4_btn.pack(side = "bottom")

#Creating a text label widget
startRecordingButtonF4 = Button(frame4, image=RecordButton, text = "Start Recording", font=(font, 20), command=startRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
playButtonF4 = Button(frame4, text = "Play It Backwards", font=(font, 20), command=playRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
#-----------frame 4 END code-------------#

#pygame.mixer.pre_init(48000, 16, 2, 4096)
pygame.init()
showFrame(frame1)

dingSound1 = pygame.mixer.Sound('sounds/ding1.wav')
dingSound2 = pygame.mixer.Sound('sounds/ding2.wav')
dingSound3 = pygame.mixer.Sound('sounds/ding3.wav')
dingSound4 = pygame.mixer.Sound('sounds/ding4.wav')
menuClickSound = pygame.mixer.Sound('sounds/menuclick.wav')
chimeSound = pygame.mixer.Sound('sounds/chime.wav')
bingSound1 = pygame.mixer.Sound('sounds/bing.wav')
bingSound2 = pygame.mixer.Sound('sounds/bing2.wav')
mixer.music.load('sounds/background.wav')
mixer.music.set_volume(.5)
mixer.music.play()


window.mainloop()
