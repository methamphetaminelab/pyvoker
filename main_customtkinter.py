import customtkinter as ctk
from customtkinter import ALL, E, END, LAST, N, S, W, X, Y
import random
import tkinter as tk
from PIL import Image, ImageTk
import time
import os

spells = [
    '0COLD SNAP',
    '1GHOST WALK',
    '2TORNADO',
    '3E.M.P.',
    '4ALACRITY',
    '5CHAOS METEOR',
    '6SUN STRIKE',
    '7FORGE SPIRIT',
    '8ICE WALL',
    '9DEAFENING BLAST',
]

keys = [
    '0qqq',
    '1qqw',
    '2wwq',
    '3www',
    '4wwe',
    '5eew',
    '6eee',
    '7eeq',
    '8qqe',
    '9qwe',
]

score = 0
maxscore = 0
best_input_time = 0
last_input_time = 0
total_input_time = 0
input_count = 0

def on_key_press(event):
    global score, maxscore, best_input_time, last_input_time, total_input_time, input_count
    user_input = entry.get()
    entry.delete(0, END)

    if user_input == randkeys[1::]:
        score += 1
        if maxscore < score:
            maxscore = score
        last_input_time = time.time() - start_time
        if best_input_time > last_input_time or best_input_time == 0:
            best_input_time = last_input_time
        total_input_time += last_input_time
        input_count += 1
    else:
        score = 0

    current_score()
    update_statistics()
    rand_spell()

def current_score():
    if score >= maxscore:
        color = 'green'
    elif score >= maxscore // 2 and score < maxscore:
        color = 'yellow'
    elif score < maxscore:
        color = 'red'
    score_label.configure(text=f'SCORE: {score}', text_color=color)

def update_statistics():
    max_score_label.configure(text=f'MAX SCORE: {maxscore}')
    last_time_label.configure(text=f'LAST TIME: {last_input_time:.2f}s')
    best_time_label.configure(text=f'BEST TIME: {best_input_time:.2f}s')
    avg_time_label.configure(text=f'AVG TIME: {total_input_time / input_count:.2f}s')

def load_image(spell_name):
    image_path = f"{spell_name}.png"
    try:
        image = Image.open(image_path)
        image = image.resize((150, 150), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None



def rand_spell():
    global randspell, randkeys, start_time
    randspell = random.choice(spells)
    randspellnum = int(randspell[0:1])
    randkeys = keys[randspellnum]

    image = load_image(randspell)
    if image:
        spell_image_label.configure(image=image)
        spell_image_label.image = image

    start_time = time.time()

root = ctk.CTk()
root.title("PYVOKER GAME")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (600 / 2)
y = (screen_height / 2) - (400 / 2)

root.geometry(f'600x400+{int(x)}+{int(y)}')

score_label = ctk.CTkLabel(root, text="SCORE: 0")
entry = ctk.CTkEntry(root)
spell_image_label = ctk.CTkLabel(root, text='', image=None)

max_score_label = ctk.CTkLabel(root, text="MAX SCORE: 0")
last_time_label = ctk.CTkLabel(root, text="LAST TIME: 0s")
best_time_label = ctk.CTkLabel(root, text="BEST TIME: 0s")
avg_time_label = ctk.CTkLabel(root, text="AVG TIME: 0s")

spell_image_label.pack(pady=20)
score_label.pack()
entry.pack(pady=20)
max_score_label.pack()
last_time_label.pack()
best_time_label.pack()
avg_time_label.pack()

entry.bind("<Return>", on_key_press)

rand_spell()

root.mainloop()
