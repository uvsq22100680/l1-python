import tkinter as tk

racine = tk.Tk()

txt = tk.StringVar()
e = tk.Entry(racine,textvariable = txt)
e.pack()






def  affiche(txt):
    label.config(text=txt)




label = tk.Label(text="-_-")
bouton1= tk.Button(racine,text="B1",command=lambda:affiche("B1"))
bouton2= tk.Button(racine,text="B2",command=lambda:affiche("B2"))
bouton3= tk.Button(racine,text="B3",command=lambda:affiche(txt.get()))
bouton1.pack()
bouton2.pack()
bouton3.pack()
label.pack()

racine.mainloop()