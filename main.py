BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas

window = Tk()
window.title('Flashy')
window.config(padx= 50,pady= 50, bg= BACKGROUND_COLOR)
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient= "records")
else:
    to_learn = data.to_dict(orient= "records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "French")
    canvas.itemconfig(card_word, text= current_card["French"])
    flip_timer= window.after(3000, flip_card)

card_back = PhotoImage(file='images/card_back.png')
def flip_card():
    canvas.itemconfig(canvas_image, image= card_back)
    canvas.itemconfig(card_title, text= "English", fill= 'white')
    canvas.itemconfig(card_word, text= current_card["English"], fill= 'white')
def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index= False)
    next_card()

flip_timer = window.after(3000, flip_card)
canvas = Canvas(width= 800, height= 526, highlightthickness= 0)
card_front = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(400,263, image = card_front)
card_title = canvas.create_text(400,150,text= "", font= ("Ariel", 40, 'italic'), fill= 'black')
card_word = canvas.create_text(400,263,text= "", font= ('Ariel', 60, 'bold'), fill= 'black')
canvas.config(background= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column= 0, row= 0,columnspan= 2)

right_button_img = PhotoImage(file= 'images/right.png')
right_button = Button(image= right_button_img, highlightthickness= 0, borderwidth= 0, command= is_known)
right_button.grid(column= 1, row= 1)

wrong_button_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image= wrong_button_img, highlightthickness= 0,borderwidth=0, command= next_card)
wrong_button.grid(column= 0, row= 1)

next_card()
window.mainloop()