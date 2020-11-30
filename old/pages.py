import tkinter as tk

def showFrame(frame):
    #show passed in frame
    frame.tkraise()

window = tk.Tk()

#set the application window in full screen
#window.attributes('-zoomed', True)

#set the window resolution
window.geometry("800x700")

#Set the window so that the frame expands to example along with the window.
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

#loop to loop through frames
for frame in (frame1, frame2, frame3):
    #nsew = north sound east west
    frame.grid(row = 0, column = 0, sticky = 'nsew')

#-----------frame 1 code-------------#
frame1_title = tk.Label(frame1, text = 'Say It Backwards!', bg = 'red')
frame1_title.pack(fill = 'x')
frame1_btn = tk.Button(frame1, text = 'Start Game', command = lambda:showFrame(frame2))
frame1_btn.pack()

frame2_title = tk.Label(frame2, text = 'Who are you playing with?', bg = 'blue')
frame2_title.pack(fill = 'x')
frame2_btn = tk.Button(frame2, text = 'Play Game', command=lambda:showFrame(frame3))
frame2_btn.pack()

frame3_title = tk.Label(frame3, text = 'Say It Backwards!', bg = 'green')
frame3_title.pack(fill = 'x')
frame3_btn = tk.Button(frame3, text = 'Start Over', command=lambda:showFrame(frame1))
frame3_btn.pack()

showFrame(frame1)

window.mainloop()
