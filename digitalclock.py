from tkinter import *
from tkinter import font
import datetime
import requests
from PIL import Image, ImageTk
import io

def quit(*args):
    root.destroy()

def clock_time():
    now = datetime.datetime.now()
    current_time = now.strftime("\n   %d %B %Y  \n\n      %H:%M:%S \n")
    canvas.itemconfig(clock_text, text=current_time)
    root.after(1000, clock_time)  # Call the function again after 1000 ms (1 second)
def load_image_from_url(url):
    response = requests.get(url)
    image_data = response.content
    image = Image.open(io.BytesIO(image_data))
    return image

root = Tk()
root.bind("x", quit)
root.geometry("1200x600")
root.title("Digital Clock by RENTALA NANDA KISHORE")

# URL of the online image
image_url = "https://media.npr.org/assets/img/2023/01/10/being-late-npr_wide-091b7547051e704678f05e8662318f6fe0de9042.jpg?s=1100&c=50&f=jpeg"

# Load the background image from the URL
background_image = load_image_from_url(image_url)

# Resize the background image to fit the window
background_image = background_image.resize((1200, 600), Image.Resampling.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas
canvas = Canvas(root, width=1200, height=600)
canvas.pack(fill="both", expand=True)

# Set the background image on the canvas
canvas.create_image(0, 0, image=background_photo, anchor="nw")

fnt = font.Font(family="helvetica", size=80, weight="bold")

# Create the text item on the canvas
clock_text = canvas.create_text(600, 300, text="", font=fnt, fill="blue", anchor=CENTER)

clock_time()  # Initial call to clock_time functionr?
root.mainloop()
