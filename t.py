import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

###
# pip install pyttsx3
import pyttsx3
speaker = pyttsx3.init()

#---
# pip install gTTS
from gtts import gTTS
import os
language = 'en'

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Speech Synthesizer Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Speech Synthesizer Text Editor - {filepath}")

def speak_text():
    ###
    text = txt_edit.get("1.0", tk.END)
    speaker.say(text)
    speaker.runAndWait()

def synthesize_text():
    #---
    text = txt_edit.get("1.0", tk.END)
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("speech.mp3")


window = tk.Tk()
window.title("Speech Synthesizer Text Editor")

window.rowconfigure(1, minsize=800, weight=1)
window.columnconfigure(0, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_speak = tk.Button(fr_buttons, text="Speak...", command=speak_text)
btn_synth = tk.Button(fr_buttons, text="Synthesize...", command=synthesize_text)

btn_open.grid(row=0, column=0, sticky="ew")
btn_save.grid(row=0, column=1, sticky="ew")
btn_speak.grid(row=0, column=2, sticky="ew")
btn_synth.grid(row=0, column=3, sticky="ew")

fr_buttons.grid(row=0, column=0, sticky="ew")
txt_edit.grid(row=1, column=0, sticky="nsew")

window.mainloop()
