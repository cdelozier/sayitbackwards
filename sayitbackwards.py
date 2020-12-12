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
secondRecordingIterator = 1
roundNumber = 1
fs = 48000
second = 2.5
playReversedWordText = ""
fontColor = 'white'
frameNumber = 'frame'
frameIterator = 3
startingScore = ""
player1Points = 0
player2Points = 0
player3Points = 0
player4Points = 0
player1Name = ""
player2Name = ""
player3Name = ""
player4Name = ""
totalPoints = 0
winner = ""
winnerScore = 0

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
    global fontColor
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
            fontColor = "yellow"
        elif totalPlayers == 2:
            dingSound3.play()
            fontColor = "orange"
        elif totalPlayers == 3:
            dingSound4.play()
            fontColor = "red"
    else:
        menuClickSound.play()

    totalPlayers += 1
    if totalPlayers > 0 and totalPlayers < 5:
        playerCountTitleText = str(totalPlayers) +"/4 players"
        playerCountTitle.config(text=playerCountTitleText, fg = fontColor, font=(font, 30))
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
        frame2_title7 = tk.Label(frame2, text = '', bg = background, font=(font, 15))
        frame2_title7.pack(fill = 'x')
        frame2_playerLabel = Label(frame2, text=enterPlayerName.get(), bg = background, fg = 'white', font=(font, 40))
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
    frame3Title5 = tk.Label(frame3, text = '', bg = background, font=(font, 10))
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
    global playerCountIterator
    global playReversedWordText
    global startRecordingButtonF4User1
    #Check for how many players there are and display them on frame 3 accordingly.
    frame3Title5 = tk.Label(frame4, text = '', bg = background, font=(font, 27))
    frame3Title5.pack(fill = 'x')
    frame4_title2 = tk.Label(frame4, text = "Reversed Word:", bg = background, fg = 'white', font=(font, 30, 'italic'))
    frame4_title2.pack()
    playButtonF3 = Button(frame4, image = PlayImageButton, text = "Play", font=(font, 20), command=playRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
    playButtonF3.pack()
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    frame3_title6 = tk.Label(frame4, text = playerList[0], bg = background, fg = 'white', font=(font, 38))
    frame3_title6.pack(fill = 'x')
    startRecordingButtonF4User1 = Button(frame4, image = RecordButton, text = "Record", font=(font, 20), command=user1Recording, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
    startRecordingButtonF4User1.pack()
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    #playButtonF4User1 = Button(frame4, image = PlayImageButton, text = "Play", font=(font, 20), command=playUser1ReversedAudio, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
    playerCountIterator += 1;

def user1Recording():
    global playerCountIterator
    global fs
    global second
    global startRecordingButtonF4User1
    global startRecordingButtonF4User2
    global frameNumber
    global frameIterator
    global roundNumber
    frameIterator += 1;
    frameNumber = frameNumber + str(frameIterator)
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
    startRecordingButtonF4User1.config(image = PlayImageButton, text = "Play", command=playUser1ReversedAudio)
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    if (len(playerList)) > 1 and playerCountIterator == 1:
        frame3_title6 = tk.Label(frame4, text = playerList[1], bg = background, fg = 'white', font=(font, 38))
        frame3_title6.pack(fill = 'x')
        startRecordingButtonF4User2 = Button(frame4, image = RecordButton, text = "Record", font=(font, 20), command=user2Recording, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        startRecordingButtonF4User2.pack()
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        playerCountIterator += 1;
    else:
        if roundNumber < 4 and (len(playerList)) < 1:
            frame4_btn = tk.Button(frame4, image = VoteButton, text = 'Start Over', font=(font, 20), command=lambda:votes(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        elif roundNumber < 3 and (len(playerList)) == 1:
            roundNumber += 1
            frame4_btn = tk.Button(frame4, image = NextRoundButton, text = 'Start Over', font=(font, 20), command=lambda:all_children(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        elif roundNumber == 3 and (len(playerList)) == 1:
            frame4_btn = tk.Button(frame4, image = EndGameButton, text = 'Start Over', font=(font, 20), command=lambda:endGame(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        frame4_btn.pack(side = "bottom")

def user2Recording():
    global playerCountIterator
    global fs
    global second
    global startRecordingButtonF4User2
    global startRecordingButtonF4User3
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
    startRecordingButtonF4User2.config(image = PlayImageButton, text = "Play", command=playUser2ReversedAudio)
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    if (len(playerList)) > 2 and playerCountIterator == 2:
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        frame3_title6 = tk.Label(frame4, text = playerList[2], bg = background, fg = 'white', font=(font, 38))
        frame3_title6.pack(fill = 'x')
        startRecordingButtonF4User3 = Button(frame4, image = RecordButton, text = "Record", font=(font, 20), command=user3Recording, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        startRecordingButtonF4User3.pack()
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        playerCountIterator += 1;
    else:
        if roundNumber < 4:
            frame4_btn = tk.Button(frame4, image = VoteButton, text = 'Start Over', font=(font, 20), command=lambda:votes(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        frame4_btn.pack(side = "bottom")

def user3Recording():
    global playerCountIterator
    global fs
    global second
    global startRecordingButtonF4User3
    global startRecordingButtonF4User4
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
    startRecordingButtonF4User3.config(image = PlayImageButton, text = "Play", command=playUser3ReversedAudio)
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    if (len(playerList)) > 3 and playerCountIterator == 3:
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        frame3_title6 = tk.Label(frame4, text = playerList[3], bg = background, fg = 'white', font=(font, 38))
        frame3_title6.pack(fill = 'x')
        startRecordingButtonF4User4 = Button(frame4, image = RecordButton, text = "Record", font=(font, 20), command=user4Recording, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        startRecordingButtonF4User4.pack()
        frame3Title5 = tk.Label(frame4, text = '', bg = background)
        frame3Title5.pack(fill = 'x')
        playerCountIterator += 1;
    else:
        if roundNumber < 4:
            frame4_btn = tk.Button(frame4, image = VoteButton, text = 'Start Over', font=(font, 20), command=lambda:votes(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
        frame4_btn.pack(side = "bottom")

def user4Recording():
    global fs
    global second
    global startRecordingButtonF4User4
    bingSound1.play()
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
    bingSound2.play()
    startRecordingButtonF4User4.config(image = PlayImageButton, text = "Play", command=playUser4ReversedAudio)
    frame3Title5 = tk.Label(frame4, text = '', bg = background)
    frame3Title5.pack(fill = 'x')
    if roundNumber < 4:
        frame4_btn = tk.Button(frame4, image = VoteButton, text = 'Start Over', font=(font, 20), command=lambda:votes(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
    frame4_btn.pack(side = "bottom")

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
    global secondRecordingIterator
    global playReversedWordText
    #frame3BlackFiller = tk.Label(frame3, text = '', bg = background, font=(font, 20))
    #frame3BlackFiller.pack(fill = 'x', side = "top")
    playReversedWordText = "Play " + firstPick + "'s word in reverse:"
    frame3BlackFiller = tk.Label(frame3, text = '', bg = background, font=(font, 50))
    frame3BlackFiller.pack(fill = 'x', side = "top")
    frame3_title2 = tk.Label(frame3, text = playReversedWordText, bg = background, fg = 'white', font=(font, 30))
    playButtonF3 = Button(frame3, image = PlayImageButton, text = "Play", font=(font, 20), command=playRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
    if secondRecordingIterator == 1:
        secondRecordingIterator+=1
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

def close_window():
    window.destroy()

#Remove all widgets from page
def all_children():
    global roundNumber
    pygame.mixer.music.fadeout(2500)
    for widget in frame3.winfo_children():
        widget.pack_forget()
    for widget in frame4.winfo_children():
        widget.pack_forget()
    #Frame 3 code repack
    frame3_title1 = tk.Label(frame3, text = '', bg = background2)
    frame3_title1.pack(fill = 'x')
    frame3_title2 = tk.Label(frame3, text = "Who's up next?", bg = background2, fg = white, font=(font, 30, 'italic'))
    frame3_title2.pack(fill = 'x')
    frame3_title3 = tk.Label(frame3, text = '', bg = background2)
    frame3_title3.pack(fill = 'x')
    frame3_title4 = tk.Label(frame3, text = '', bg = background)
    frame3_title4.pack(fill = 'x')
    startRecordingButtonF3.config(image = RecordButton, text="Record", bg = background)
    playButtonF3 = Button(frame3, text = "Play It Backwards", font=(font, 20), command=playRecording1, bg = yellow)
    #Frame 4 code repack
    frame4_title1 = tk.Label(frame4, text = '', bg = background2)
    frame4_title1.pack(fill = 'x')
    if roundNumber == 2:
        frame4_title2 = tk.Label(frame4, text = 'Round 2', bg = background2, fg = white, font=(font, 30, 'italic'))
        frame4_title2.pack(fill = 'x')
    elif roundNumber == 3:
        frame4_title2 = tk.Label(frame4, text = 'Round 3', bg = background2, fg = white, font=(font, 30, 'italic'))
        frame4_title2.pack(fill = 'x')
    frame4_title3 = tk.Label(frame4, text = '', bg = background2)
    frame4_title3.pack(fill = 'x')
    playButtonF3 = Button(frame4, image = PlayImageButton, text = "Play", font=(font, 20), command=playRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
    frame4BlackFiller = tk.Label(frame4, text = '', bg = background, font=(font, 20))
    frame4BlackFiller.pack(fill = 'x', side = "bottom")
    playGame()

def votes():
    global secondRecordingIterator
    global roundNumber
    global playerCountIterator
    global startingScore
    global player1Points
    global player2Points
    global player3Points
    global player4Points
    global playerNumber
    global player1Name
    global player2Name
    global player3Name
    global player4Name
    menuClickSound.play()
    mixer.music.load('sounds/intensemusic.wav')
    mixer.music.set_volume(.5)
    mixer.music.play()
    playerCountIterator = 0;
    roundNumber += 1
    secondRecordingIterator = 1
    playerNumber = 1
    if roundNumber == 2:
        frame5_title1 = tk.Label(frame5, text = '', bg = background2)
        frame5_title1.pack(fill = 'x')
        frame5_title2 = tk.Label(frame5, text = 'Who said it best?', bg = background2, fg = white, font=(font, 40, 'italic'))
        frame5_title2.pack(fill = 'x')
        frame5_title3 = tk.Label(frame5, text = '', bg = background2)
        frame5_title3.pack(fill = 'x')
        frame5_title4 = tk.Label(frame5, text = '', bg = background)
        frame5_title4.pack(fill = 'x')
        for players in playerList:
            startingScore  = players + ": " + str(player1Points)
            if playerNumber == 1:
                player1Name = players
                player1ScoreTitle.config(text=startingScore)
                player1ScoreTitle.pack()
                addPointButton1 = Button(frame5, image = AddPointButton, text = "Play", font=(font, 20), command=lambda:addPoints1(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
                addPointButton1.pack()
                subtractPointButton = Button(frame5, image = SubtractPointButton, text = "Play", font=(font, 20), command=lambda:subtractPoints1(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
                subtractPointButton.pack()
            if playerNumber == 2:
                player2Name = players
                player2ScoreTitle.config(text=startingScore)
                player2ScoreTitle.pack()
                addPointButton2 = Button(frame5, image = AddPointButton, text = "Play", font=(font, 20), command=lambda:addPoints2(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
                addPointButton2.pack()
                subtractPointButton = Button(frame5, image = SubtractPointButton, text = "Play", font=(font, 20), command=lambda:subtractPoints2(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
                subtractPointButton.pack()
            if playerNumber == 3:
                player3Name = players
                player3ScoreTitle.config(text=startingScore)
                player3ScoreTitle.pack()
                addPointButton3 = Button(frame5, image = AddPointButton, text = "Play", font=(font, 20), command=lambda:addPoints3(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
                addPointButton3.pack()
                subtractPointButton = Button(frame5, image = SubtractPointButton, text = "Play", font=(font, 20), command=lambda:subtractPoints3(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
                subtractPointButton.pack()
            if playerNumber == 4:
                player4Name = players
                player4ScoreTitle.config(text=startingScore)
                player4ScoreTitle.pack()
                addPointButton3 = Button(frame5, image = AddPointButton, text = "Play", font=(font, 20), command=lambda:addPoints4(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
                addPointButton3.pack()
                subtractPointButton = Button(frame5, image = SubtractPointButton, text = "Play", font=(font, 20), command=lambda:subtractPoints4(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
                subtractPointButton.pack()
            frame5_title4 = tk.Label(frame5, text = '', bg = background)
            frame5_title4.pack(fill = 'x')
            playerNumber += 1
        frame3Title5 = tk.Label(frame5, text = '', bg = background, font=(font, 20))
        frame3Title5.pack(side = "bottom", fill = 'x')
        frame5_btn.pack(side = "bottom")
    if roundNumber == 4:
        frame5_btn.config(image=EndGameButton, command=lambda:endGame())
    showFrame(frame5)

def addPoints1():
    global player1Points
    global player1Name
    global roundNumber
    if player1Points >= 0:
        player1Points += 1
        fullScore = player1Name + ": " + str(player1Points)
        player1ScoreTitle.config(text=fullScore)

def subtractPoints1():
    global player1Points
    global player1Name
    if player1Points > 0:
        player1Points -= 1
        fullScore = player1Name + ": " + str(player1Points)
        player1ScoreTitle.config(text=fullScore)

def addPoints2():
    global player2Points
    global player2Name
    if player2Points >= 0:
        player2Points += 1
        fullScore = player2Name + ": " + str(player2Points)
        player2ScoreTitle.config(text=fullScore)

def subtractPoints2():
    global player2Points
    global player2Name
    if player2Points > 0:
        player2Points -= 1
        fullScore = player2Name + ": " + str(player2Points)
        player2ScoreTitle.config(text=fullScore)

def addPoints3():
    global player3Points
    global player3Name
    if player3Points >= 0:
        player3Points += 1
        fullScore = player3Name + ": " + str(player3Points)
        player3ScoreTitle.config(text=fullScore)

def subtractPoints3():
    global player3Points
    global player3Name
    if player3Points > 0:
        player3Points -= 1
        fullScore = player3Name + ": " + str(player3Points)
        player3ScoreTitle.config(text=fullScore)

def addPoints4():
    global player4Points
    global player4Name
    if player4Points >= 0:
        player4Points += 1
        fullScore = player4Name + ": " + str(player4Points)
        player4ScoreTitle.config(text=fullScore)

def subtractPoints4():
    global player4Points
    global player4Name
    if player4Points > 0:
        player4Points -= 1
        fullScore = player4Name + ": " + str(player4Points)
        player4ScoreTitle.config(text=fullScore)

def endGame():
    global winner
    global winnerScore
    pygame.mixer.music.fadeout(0)
    mixer.music.load('sounds/winningmusic.wav')
    mixer.music.set_volume(.5)
    mixer.music.play()
    menuClickSound.play()
    if (len(playerList)) > 1:
        whoWon()
        winnerScoreString = str(winnerScore) + " points!"
        WhoWonLogo.pack(fill = 'x')
        frame6_title4.pack(fill = 'x')
        frame3_title4 = tk.Label(frame6, text = '', bg = background)
        frame3_title4.pack(fill = 'x')
        frame6_title5.config(text=winner, fg = 'white', font=(font, 45))
        frame6_title5.pack()
        frame3_title4 = tk.Label(frame6, text = '', bg = background)
        frame3_title4.pack(fill = 'x')
        frame6_title6.config(fg = 'white', font=(font, 45))
        frame6_title6.pack()
        frame3_title4 = tk.Label(frame6, text = '', bg = background)
        frame3_title4.pack(fill = 'x')
        frame6_title7.config(text=winnerScoreString, fg = 'white', font=(font, 45))
        frame6_title7.pack()
        frame3_title4 = tk.Label(frame6, text = '', bg = background, font=(font, 20))
        frame3_title4.pack(side = "top", fill = 'x')
        frame6_title8.config(font=(font, 28, "italic"))
        frame6_title8.pack()
        frame3_title4 = tk.Label(frame6, text = '', bg = background, font=(font, 20))
        frame3_title4.pack(side = "top", fill = 'x')
        frame6_btn.pack(side="top")
        frame3_title4 = tk.Label(frame6, text = '', bg = background, font=(font, 20))
        frame3_title4.pack(side = "bottom", fill = 'x')
        frame6_btn2.pack(side="bottom")

    else:
        frame6_title1.pack(fill = 'x')
        frame6_title2.config(text = "Thanks for playing!")
        frame6_title2.pack(fill = 'x')
        frame6_title3.pack(fill = 'x')
        frame3_title4 = tk.Label(frame6, text = '', bg = background, font=(font, 20))
        frame3_title4.pack(side = "top", fill = 'x')
        frame6_title5.config(text="Would you like to play again?", fg = 'white', font=(font, 32))
        frame6_title5.pack()
        frame3_title4 = tk.Label(frame6, text = '', bg = background, font=(font, 20))
        frame3_title4.pack(side = "top", fill = 'x')
        frame6_btn.pack(side="top")
        frame3_title4 = tk.Label(frame6, text = '', bg = background, font=(font, 20))
        frame3_title4.pack(side = "bottom", fill = 'x')
        frame6_btn2.pack(side="bottom")
    showFrame(frame6)

def whoWon():
    global winner
    global winnerScore
    if len(playerList) == 2:
        players = {playerList[0]: player1Points, playerList[1]: player2Points}
    elif len(playerList) == 3:
        players = {playerList[0]: player1Points, playerList[1]: player2Points, playerList[2]: player3Points}
    elif len(playerList) == 4:
        players = {playerList[0]: player1Points, playerList[1]: player2Points, playerList[2]: player3Points, playerList[3]: player4Points}
    winner = max(players, key=players.get)
    winnerScore = players[winner]

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

window.bind('<KP_Enter>', enterKeyPress)

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
frame5 = tk.Frame(window, bg = background)
frame6 = tk.Frame(window, bg = background)

#rounded button png's
startGameButton = PhotoImage(file='photos/Start_Game.png')
startRoundButton = PhotoImage(file='photos/Start_Round.png')
RecordButton = PhotoImage(file='photos/Record.png')
PlayGameButton = PhotoImage(file='photos/Play_Game.png')
AddPlayerButton= PhotoImage(file='photos/Add_Player.png')
PlayImageButton = PhotoImage(file='photos/Play.png')
RetakeButton = PhotoImage(file='photos/Retake.png')
StartOverButton = PhotoImage(file='photos/Start_Over.png')
NextRoundButton = PhotoImage(file='photos/Next_Round.png')
VoteButton = PhotoImage(file='photos/Vote.png')
AddPointButton = PhotoImage(file='photos/add.png')
SubtractPointButton = PhotoImage(file='photos/subtract.png')
EndGameButton = PhotoImage(file='photos/End_Game.png')
gameLogo = PhotoImage(file='photos/logo.png')
endGameLogo = PhotoImage(file='photos/End_Game_Logo.png')

#loop to loop through frames
for frame in (frame1, frame2, frame3, frame4, frame5, frame6):
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
player1ScoreTitle = Label(frame5, text = startingScore, bg = background, fg = 'white', font=(font, 40))
player2ScoreTitle = Label(frame5, text = startingScore, bg = background, fg = 'white', font=(font, 40))
player3ScoreTitle = Label(frame5, text = startingScore, bg = background, fg = 'white', font=(font, 40))
player4ScoreTitle = Label(frame5, text = startingScore, bg = background, fg = 'white', font=(font, 40))
playButtonF3 = Button(frame4, image = PlayImageButton, text = "Play", font=(font, 20), command=playRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
frame4BlackFiller = tk.Label(frame4, text = '', bg = background, font=(font, 20))
frame4BlackFiller.pack(fill = 'x', side = "bottom")
frame4_btn = tk.Button(frame4, image = NextRoundButton, text = 'Start Over', font=(font, 20), command=lambda:showFrame(frame5), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
#Creating a text label widget
startRecordingButtonF4 = Button(frame4, image=RecordButton, text = "Start Recording", font=(font, 20), command=startRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
playButtonF4 = Button(frame4, text = "Play It Backwards", font=(font, 20), command=playRecording1, bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
#-----------frame 4 END code-------------#

#-----------frame 5 START code-------------#
frame5_title1 = tk.Label(frame5, text = '', bg = background2)
frame5_title2 = tk.Label(frame5, text = 'Who said it best?', bg = background2, fg = white, font=(font, 40, 'italic'))
frame5_title3 = tk.Label(frame5, text = '', bg = background2)
frame5_btn = tk.Button(frame5, image = NextRoundButton, text = 'Start Over', font=(font, 20), command=lambda:all_children(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
#-----------frame 5 END code-------------#

#-----------frame 6 START code-------------#
frame6_title1 = tk.Label(frame6, text = '', bg = background2)
frame6_title2 = tk.Label(frame6, text = 'Who won?', bg = background2, fg = white, font=(font, 40, 'italic'))
frame6_title3 = tk.Label(frame6, text = '', bg = background2)
WhoWonLogo = tk.Label(frame6, image=endGameLogo, text = '', bg = background2)
frame6_title4 = tk.Label(frame6, text = '', bg = background)
frame6_title5 = tk.Label(frame6, text = '', bg = background)
frame6_title6 = tk.Label(frame6, text = 'with', bg = background)
frame6_title7 = tk.Label(frame6, text = '', bg = background)
frame6_title8= tk.Label(frame6, text="Would you like to play again?", fg = 'white', font=(font, 32), bg = background)
frame6_btn = tk.Button(frame6, image = StartOverButton, text = 'Start Over', font=(font, 20), command=lambda:restart_program(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
frame6_btn2 = tk.Button(frame6, image = EndGameButton, text = 'End Game', font=(font, 20), command=lambda:close_window(), bg = background, activebackground=background, borderwidth=0, highlightthickness=0)
#-----------frame 6 END code-------------#

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
