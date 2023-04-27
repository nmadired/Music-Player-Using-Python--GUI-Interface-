import tkinter as tk
import os
import pygame
from PIL import Image, ImageTk
from tkinter import ttk

class MICHIGANTECHMUSIC:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MICHIGAN TECH MUSIC")
        self.root.geometry("800x700")
        self.root.configure(bg="black")
        
        disc_image_path = "C:/Users/13312/Desktop/Muisc player/Screenshot 2023-04-17 004618.png"
        self.disc_image = Image.open(disc_image_path)
        self.disc_image = self.disc_image.resize((250, 200), Image.LANCZOS)
        self.disc_photo = ImageTk.PhotoImage(self.disc_image)

        image_path2 = "C:/Users/13312/Desktop/Muisc player/EMINEM.png-removebg-preview.png"
        self.image2 = Image.open(image_path2)
        self.image2 = self.image2.resize((340,700), Image.LANCZOS)
        self.image2_photo = ImageTk.PhotoImage(self.image2)

        self.image2_label = tk.Label(self.root, image=self.image2_photo, bg="black",)
        self.image2_label.pack(padx=10, pady=10, side=tk.RIGHT)

        self.disc_label = tk.Label(self.root, image=self.disc_photo, bg="black")
        self.disc_label.pack(padx=10, pady=10)

        pygame.mixer.init()

        self.song_listbox = tk.Listbox(self.root, height=15, width=50, font=("Times New Roman", 12), bg="#2C2C2C", fg="white", selectbackground="#004BA8", selectforeground="white")
        self.song_listbox.pack(padx=10, pady=10)

        self.songs = os.listdir('C:/Users/13312/Desktop/Muisc player/')
        
        for song in self.songs:
            self.song_listbox.insert(tk.END, song)

        self.play_button = tk.Button(self.root, text="PLAY", width=10, font=("Times New Roman", 14, "bold"), bg="#004BA8", fg="white", activebackground="#00336E", command=self.play_song)
        self.play_button.pack(side=tk.LEFT, padx=20, pady=5,)

        self.pause_button = tk.Button(self.root, text="PAUSE", width=10, font=("Times New Roman", 14, "bold"), bg="#004BA8", fg="white", activebackground="#00336E", command=self.pause_song)
        self.pause_button.pack(side=tk.LEFT, padx=20, pady=5)

        self.stop_button = tk.Button(self.root, text="STOP", width=10, font=("Times New Roman", 14, "bold"), bg="#004BA8", fg="white", activebackground="#00336E", command=self.stop_song)
        self.stop_button.pack(side=tk.LEFT, padx=20, pady=5)

        self.volume_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, length=500, sliderlength=20, width=15, font=("Times New Roman", 12), bg="blue", fg="white", highlightbackground="WHITE", troughcolor="black", command=self.set_volume)
        self.volume_slider.set(50)
        self.volume_slider.pack(side=tk.RIGHT, padx=20, pady=5)
        self.song_listbox.selection_set(first=0)
        self.themes ={
            "Default": {"bg": "black", "fg": "white", "activebg": "#00336E", "highlightbg": "WHITE", "troughcolor": "black"},
            "Dark": {"bg": "#1C1C1C", "fg": "white", "activebg": "#00336E", "highlightbg": "WHITE", "troughcolor": "#1C1C1C"},
            "Light": {"bg": "white", "fg": "black", "activebg": "#0077FF", "highlightbg": "BLACK", "troughcolor": "#F0F0F0"},
            "orange": {"bg": "orange", "fg": "white", "activebg": "orange", "highlightbg": "WHITE", "troughcolor": "orange"}
            }
        self.theme_label = tk.Label(self.root, text="Select Theme:", font=("Times New Roman", 14), bg="black", fg="white")
        self.theme_label.pack(side=tk.TOP, padx=20, pady=5)
        self.theme_var = tk.StringVar()
        self.theme_var.set("Default")
        self.theme_menu = ttk.OptionMenu(self.root, self.theme_var, *self.themes.keys(), command=self.change_theme)
        self.theme_menu.pack(side=tk.TOP, padx=20, pady=5)
        self.root.mainloop()
    def play_song(self):
        selected_song = self.song_listbox.get(tk.ACTIVE)
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()
    
    def pause_song(self):
        pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()
        
    def set_volume(self, val):
        volume = int(val) / 100
        pygame.mixer.music.set_volume(volume)

    def change_theme(self, theme):
        selected_theme = self.themes[theme]
        self.root.configure(bg=selected_theme["bg"])
        self.song_listbox.configure(bg=selected_theme["bg"], fg=selected_theme["fg"], selectbackground=selected_theme["activebg"], highlightbackground=selected_theme["highlightbg"])
        self.play_button.configure(bg=selected_theme["bg"], fg=selected_theme["fg"], activebackground=selected_theme["activebg"])
        self.pause_button.configure(bg=selected_theme["bg"], fg=selected_theme["fg"], activebackground=selected_theme["activebg"])
        self.stop_button.configure(bg=selected_theme["bg"], fg=selected_theme["fg"], activebackground=selected_theme["activebg"])
        self.volume_slider.configure(bg=selected_theme["bg"], fg=selected_theme["fg"], highlightbackground=selected_theme["highlightbg"], troughcolor=selected_theme["troughcolor"])

        pass

music_player = MICHIGANTECHMUSIC()

