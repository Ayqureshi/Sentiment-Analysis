from tkinter import *
from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text: str, *, threshold: float) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold = threshold
    hostile_threshold = -threshold
    if sentiment >= friendly_threshold:
        return Mood("🤠", sentiment)
    elif sentiment <= hostile_threshold:
        return Mood("😭", sentiment)
    else:
        return Mood("😐", sentiment)

def analyze_text():
    input_text = input_text_entry.get()
    mood = get_mood(input_text, threshold=0.2)
    result_label.config(text=f'{mood.emoji}({mood.sentiment})')

# Create the main window
window = Tk()
window.title("Text Mood Analyzer")

# Create input text entry
input_text_entry = Entry(window)
input_text_entry.pack()

# Create analyze button
analyze_button = Button(window, text="Analyze", command=analyze_text)
analyze_button.pack()

# Create result label
result_label = Label(window, text="")
result_label.pack()

# Start the main GUI loop
window.mainloop()