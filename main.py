from tkinter import Tk, Button
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

def update_image_dimensions(event):
    new_width = int(event.width * 0.8)  # Adjust the scaling factor as desired
    new_height = int(event.height * 0.8)
    resized_image = resize_image(image_path, new_width, new_height)
    button.configure(image=resized_image)

root = Tk()

# Define the desired initial width and height for the button image
button_width = 200
button_height = 100

# Load and resize the image
image_path = '1.png'  # Replace with the actual path to your image
resized_image = resize_image(image_path, button_width, button_height)

# Create a button and set the resized image on it
button = Button(root, image=resized_image)
button.grid(row=0, column=0)

# Bind the <Configure> event of the window to the update_image_dimensions function
root.bind('<Configure>', update_image_dimensions)
print("Hello")
root.mainloop()