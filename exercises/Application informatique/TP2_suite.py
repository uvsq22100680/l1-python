import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog



create=True

def charger(widg):
    global create
    global photo
    global img
    global canvas
    filename= filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    print(photo)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.pack()
        create=False
        
    else:
        canvas.pack_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.pack()

racine = tk.Tk()
racine.title("image")
bouton_1 = tk.Button(racine,text="charger image",commmand=lambda: charger(racine))
bouton_1.pack()

racine.mainloop()