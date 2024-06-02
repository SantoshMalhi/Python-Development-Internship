import os
import pygame
from tkinter import filedialog, Tk, Button, Label, Listbox, Scrollbar, Scale
from tkinter.font import Font

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Python Music Player")
        master.geometry("600x400")
        master.config(bg="#f0f0f0")

        self.playlist = []
        self.current_track_index = 0

        self.label_font = Font(family="Arial", size=12, weight="bold")

        self.load_button = Button(master, text="Load Playlist", command=self.load_playlist, bg="#3498db", fg="white", font=self.label_font)
        self.load_button.pack(pady=10)

        self.previous_button = Button(master, text="Previous", command=self.previous_track, bg="#2980b9", fg="white", font=self.label_font)
        self.previous_button.pack(side="left", padx=10)

        self.rewind_button = Button(master, text="Rewind", command=self.rewind_track, bg="#2980b9", fg="white", font=self.label_font)
        self.rewind_button.pack(side="left", padx=10)

        self.play_button = Button(master, text="Play", command=self.play, bg="#27ae60", fg="white", font=self.label_font)
        self.play_button.pack(side="left", padx=10)

        self.pause_button = Button(master, text="Pause", command=self.pause, bg="#e67e22", fg="white", font=self.label_font)
        self.pause_button.pack(side="left", padx=10)

        self.stop_button = Button(master, text="Stop", command=self.stop, bg="#c0392b", fg="white", font=self.label_font)
        self.stop_button.pack(side="left", padx=10)

        self.forward_button = Button(master, text="Forward", command=self.forward_track, bg="#2980b9", fg="white", font=self.label_font)
        self.forward_button.pack(side="left", padx=10)

        self.next_button = Button(master, text="Next", command=self.next_track, bg="#2980b9", fg="white", font=self.label_font)
        self.next_button.pack(side="left", padx=10)

        self.progress_scale = Scale(master, from_=0, to=100, orient="horizontal", command=self.set_track_position, bg="#f0f0f0")
        self.progress_scale.pack(fill="x", padx=10, pady=(20, 0))

        self.track_listbox = Listbox(master, width=60, font=("Arial", 10), selectbackground="#3498db", selectforeground="white")
        self.track_listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.scrollbar = Scrollbar(master, orient="vertical", command=self.track_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.track_listbox.config(yscrollcommand=self.scrollbar.set)

        self.playback_label = Label(master, text="", bg="#f0f0f0", font=self.label_font)
        self.playback_label.pack(pady=10)

    def load_playlist(self):
        playlist_directory = filedialog.askdirectory()
        self.playlist = [os.path.join(playlist_directory, file) for file in os.listdir(playlist_directory) if file.endswith(".mp3")]
        self.update_track_listbox()

    def update_track_listbox(self):
        self.track_listbox.delete(0, "end")
        for track in self.playlist:
            self.track_listbox.insert("end", os.path.basename(track))

    def play(self):
        if self.playlist:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            track_path = self.playlist[self.current_track_index]
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.play()
            self.playback_label.config(text="Now playing: " + os.path.basename(track_path))
        else:
            self.playback_label.config(text="Playlist is empty")

    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.playback_label.config(text="Playback paused")

    def stop(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.playback_label.config(text="Playback stopped")

    def next_track(self):
        if self.current_track_index < len(self.playlist) - 1:
            self.current_track_index += 1
            self.play()

    def previous_track(self):
        if self.current_track_index > 0:
            self.current_track_index -= 1
            self.play()

    def rewind_track(self):
        pygame.mixer.music.rewind()

    def forward_track(self):
        current_pos = pygame.mixer.music.get_pos() // 1000  # Current position in seconds
        new_pos = min(current_pos + 10, pygame.mixer.Sound(self.playlist[self.current_track_index]).get_length() // 1000)
        pygame.mixer.music.set_pos(new_pos)

    def set_track_position(self, value):
        new_pos = int(value) * pygame.mixer.Sound(self.playlist[self.current_track_index]).get_length() // 100
        pygame.mixer.music.set_pos(new_pos)

root = Tk()
music_player = MusicPlayer(root)
root.mainloop()
