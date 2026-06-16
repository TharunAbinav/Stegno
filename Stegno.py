'''This Project is about using Quantum key to secure the data 
and then using Steganography to hide the data in an image.'''
import qiskit
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root=tk.Tk()
root.withdraw()

print("Opening file section")
file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp")]
)

if file_path:
    img = Image.open(file_path)
    print(f"Successfully selected: {file_path}")
    print(f"Image Size: {img.size}")
    img.show()
else:
    print("User canceled image selection.")