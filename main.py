from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
COLOR_WHITE = '#FFFFFF'
COLOR_BLACK = '#000000'

to_learn_dict = {}
current_card = {}


def open_data():
    global to_learn_dict
    try:
        data = pd.read_csv('./data/words_to_learn.csv')
    except FileNotFoundError:
        data = pd.read_csv('./data/regular_english_words.csv')
    finally:
        to_learn_dict = data.to_dict(orient='records')


def button_right():
    global current_card, to_learn_dict
    to_learn_dict.remove(current_card)
    pd.DataFrame(to_learn_dict).to_csv('./data/words_to_learn.csv', index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    card_front()
    flip_timer = window.after(3000, func=card_back)


def card_front():
    canvas.itemconfig(card_background, image=image_card_front)
    canvas.itemconfig(card_title, text='English', fill=COLOR_BLACK)
    canvas.itemconfig(card_word, text=current_card['English'], fill=COLOR_BLACK)


def card_back():
    canvas.itemconfig(card_background, image=image_card_back)
    canvas.itemconfig(card_title, text='Português', fill=COLOR_WHITE)
    canvas.itemconfig(card_word, text=current_card['Portugues'], fill=COLOR_WHITE)


open_data()
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, card_back)


image_button_wrong = PhotoImage(file='./images/wrong.png')
image_button_right = PhotoImage(file='./images/right.png')
image_card_back = PhotoImage(file='./images/card_back.png')
image_card_front = PhotoImage(file='./images/card_front.png')


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_background = canvas.create_image(400, 263, image=image_card_front)


canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))


button_wrong = Button(image=image_button_wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
button_right = Button(image=image_button_right, bg=BACKGROUND_COLOR, highlightthickness=0, command=button_right)
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)


next_card()
window.mainloop()
