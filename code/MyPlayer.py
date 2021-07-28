import os
import sys

import pygame #used to create video games
import tkinter as tk #used to develop GUI
from tkinter.filedialog import askdirectory #it permit to select dir


def play():
    filename = play_list.get(tk.ACTIVE)
    try:
        pygame.mixer.music.load(filename)
    except:
        print(f'ERROR: Invalid file - {filename}')
        return
    var.set(play_list.get(tk.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


# Create the interface
music_player = tk.Tk() 
music_player.title('Life In Music') 
music_player.geometry('500x310')

Button1 = tk.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='PLAY', command=play, bg='blue', fg='white')
Button2 = tk.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='STOP', command=stop, bg='red', fg='white')
Button3 = tk.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='PAUSE', command=pause, bg='purple', fg='white')
Button4 = tk.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='UNPAUSE', command=unpause, bg='orange', fg='white')

Button1.pack(fill='x')
Button2.pack(fill='x')
Button3.pack(fill='x')
Button4.pack(fill='x')

# prompt the user to choose the folder where the music files are listed
directory = askdirectory()
if directory == '':
    print('ERROR: No directory selected!')
    sys.exit(9)

print(f'Directory is: {directory}')
os.chdir(directory) # permits to change the current dir
song_list = os.listdir() # returns the list of files

# Resize the window
music_player.geometry('500x700')

# display the items to the user
play_list = tk.Listbox(music_player, font='Helvetica 12 bold', bg='yellow', selectmode=tk.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

# for loading and playing sounds - use pygame
pygame.init()
pygame.mixer.init()

var = tk.StringVar() 
song_title = tk.Label(music_player, font='Helvetica 12 bold', textvariable=var)

song_title.pack()
play_list.pack(fill='both', expand='yes')

music_player.mainloop()
print('Done!')
