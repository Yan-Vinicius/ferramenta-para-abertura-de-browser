import webbrowser
from tkinter import *


root = Tk( )

root.title("Abrir browser")
root.geometry("400x300")

def webSite():

    webbrowser.open("https://google.com")

my_web_site = Button(root, text="Abrir site", command=webSite).pack(pady=30)

root.mainloop()