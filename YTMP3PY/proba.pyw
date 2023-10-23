import requests
from tkinter import messagebox
from pytube import YouTube
from tkinter import *


def convert_to_mp3():
    url = url_entry.get()
    if url == TRUE:
        audio = YouTube(url)
        audio.streams.get_audio_only().download()

    else:
        url_entry.delete(0, "end")
        messagebox.showerror(title="Error", message="INVALID URL!")


root = Tk()
root.geometry("300x300")
root.title("YT Converter")

label1 = Label(root, text="Enter YouTube Video URL:")
label1.pack()

url_entry = Entry(root)
url_entry.pack()


convert_button = Button(root, text="Convert to MP3", command=convert_to_mp3)

convert_button.pack()

root.mainloop()
