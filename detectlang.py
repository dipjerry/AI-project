import tkinter as tk
from langdetect import detect
from iso639 import languages
def detect_language():
    text = text_entry.get("1.0", "end-1c")
    if text:
        detected_language = detect(text)
        language_name = languages.get(alpha2=detected_language).name
        result_label.config(text="Detected language: " + language_name)
    else:
        result_label.config(text="Please enter some text.")
window = tk.Tk()
window.title("Language Detection")
text_entry = tk.Text(window, height=10, width=40)
text_entry.pack()
detect_button = tk.Button(window, text="Detect Language", command=detect_language)
detect_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()
