from PIL import Image
import tkinter
from tkinter import messagebox
from pygame import mixer
import time

print("POTATO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(5)

mixer.init()
mixer.music.load("potato.mp3")
mixer.music.play()

root = tkinter.Tk()
root.withdraw()

messagebox.showerror("GET POTATOED!!!!!!!", "😂😂😂😂🤣🤣🤣🤣🤣")

image = Image.open("potato.png")
image2 = Image.open("potato2.png")
image3 = Image.open("potato3.png")

image.show()
image2.show()
image3.show()

messagebox.showerror("GET POTATOED!!!!!!!", "😂😂😂😂🤣🤣🤣🤣🤣")
messagebox.showwarning("GET POTATOED!!!!!!!", "😂😂😂😂🤣🤣🤣🤣🤣")
messagebox.showinfo("GET POTATOED!!!!!!!", "😂😂😂😂🤣🤣🤣🤣🤣")