import os
import pygame
import tkinter as tk
from tkinter import filedialog
# Initialize the pygame mixer
pygame.mixer.init()

# Define the MusicPlayer class
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        # Create the song listbox
        self.song_listbox = tk.Listbox(self.root, height=5, width=50)
        self.song_listbox.pack(pady=5)

        # Create the buttons
        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song)
        self.prev_button = tk.Button(self.root, text="<< Prev", command=self.prev_song)
        self.next_button = tk.Button(self.root, text="Next >>", command=self.next_song)
        self.vol_up_button = tk.Button(self.root, text="Vol +", command=self.vol_up)
        self.vol_down_button = tk.Button(self.root, text="Vol -", command=self.vol_down)

        self.play_button.pack(side=tk.LEFT, padx=5)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        self.next_button.pack(side=tk.LEFT, padx=5)
        self.vol_up_button.pack(side=tk.LEFT, padx=5)
        self.vol_down_button.pack(side=tk.LEFT, padx=5)

        # Initialize the current song index and volume
        self.current_song = 0
        self.volume = 0.5

        # Populate the song listbox with files from the current directory
        self.populate_song_listbox()

    def populate_song_listbox(self):
        for filename in os.listdir("."):
            if filename.endswith(".mp3"):
                self.song_listbox.insert(tk.END, filename)

    def play_song(self):
        # Load the selected song
        song = self.song_listbox.get(self.song_listbox.curselection())
        pygame.mixer.music.load(song)

        # Set the volume and start playing the song
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def prev_song(self):
        self.current_song -= 1
        if self.current_song < 0:
            self.current_song = self.song_listbox.size() - 1
        self.song_listbox.selection_clear(0, tk.END)
        self.song_listbox.activate(self.current_song)
        self.song_listbox.selection_set(self.current_song)
        self.play_song()

    def next_song(self):
        self.current_song += 1
        if self.current_song >= self.song_listbox.size():
            self.current_song = 0
        self.song_listbox.selection_clear(0, tk.END)
        self.song_listbox.activate(self.current_song)
        self.song_listbox.selection_set(self.current_song)
        self.play_song()

    def vol_up(self):
        self.volume = min(1.0, self.volume + 0.1)
        pygame.mixer.music.set_volume(self.volume)

    def vol_down(self):
        self.volume = max(0.0, self.volume - 0.1)
        pygame.mixer.music.set_volume(self.volume)

# Create the Tkinter root window
root = tk.Tk()

# Create the MusicPlayer instance
music_player = MusicPlayer(root)

# Start the Tkinter event loop
root.mainloop()
