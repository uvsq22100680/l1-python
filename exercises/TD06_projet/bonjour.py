import tkinter as tk

racine = tk.Tk()
racine.title('apllication01')
label1 = tk.Label(racine,text ="Bonjour tout le monde!",fg="red")
label1.grid()

button1= tk.Button(racine,text ="Quitter",bg="blue",borderwidth= 5,relief="sunken")
button1.grid()

racine.mainloop()