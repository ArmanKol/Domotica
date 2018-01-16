import tkinter as tk
from tkinter.ttk import Separator, Style

def hoofdmenuframe():
    global hoofdmenuframe
    hoofdmenuframe = tk.Frame(root)
    hoofdmenuframe.configure(background="white")

    #KAMER 1
    kamer1label = tk.Label(master=hoofdmenuframe, background="white", text="Kamer 1", font=("",12))
    kamer1label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    kamer1lichtlabel = tk.Label(master=hoofdmenuframe, background="white", text="Licht: ")
    kamer1lichtlabel.grid(row=1, column=0, padx=10, pady=10)

    kamer1roodlicht = tk.Label(master=hoofdmenuframe, background="red4", width=2)
    kamer1roodlicht.grid(row= 1, column=1, padx=2, pady=5)

    kamer1groenlicht = tk.Label(master=hoofdmenuframe, background="green4", width=2)
    kamer1groenlicht.grid(row=1, column=2, padx=3)

    kamer1camerastatus = tk.Label(master=hoofdmenuframe, background="white", text="Camera-status: ")
    kamer1camerastatus.grid(row=2, column=0, padx=10, pady=10)

    kamer1roodcamerastatus = tk.Label(master=hoofdmenuframe, background="red4", width=2)
    kamer1roodcamerastatus.grid(row=2, column=1, padx=2, pady=5)

    kamer1groencamerastatus = tk.Label(master=hoofdmenuframe, background="green4", width=2)
    kamer1groencamerastatus.grid(row=2, column=2, padx=3)

    kamer1camerabeelden = tk.Label(master=hoofdmenuframe, background="white", text="Camerabeelden")
    kamer1camerabeelden.grid(row=3, column=0, padx=10 ,pady=10)

    kamer1camerabeeldenknop = tk.Button(master=hoofdmenuframe, width=5)
    kamer1camerabeeldenknop.grid(row=3, column=1, columnspan=2, padx=10, pady=10)


    #KAMER 2
    kamer2label = tk.Label(master=hoofdmenuframe, text="Kamer 2", background="white", font=("",12))
    kamer2label.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

    kamer2lichtlabel = tk.Label(master=hoofdmenuframe, background="white", text="Licht: ")
    kamer2lichtlabel.grid(row=1, column=3, padx=10, pady=10)

    kamer2roodlicht = tk.Label(master=hoofdmenuframe, background="red4", width=2)
    kamer2roodlicht.grid(row=1, column=4, padx=3, pady=5)

    kamer2groenlicht = tk.Label(master=hoofdmenuframe, background="green4", width=2)
    kamer2groenlicht.grid(row=1, column=5, padx=2)

    kamer2camerastatus = tk.Label(master=hoofdmenuframe, background="white", text="Camera-status: ")
    kamer2camerastatus.grid(row=2, column=3, padx=10, pady=10)

    kamer2roodcamerastatus = tk.Label(master=hoofdmenuframe, background="red4", width=2)
    kamer2roodcamerastatus.grid(row=2, column=4, padx=2, pady=5)

    kamer2groencamerastatus = tk.Label(master=hoofdmenuframe, background="green4", width=2)
    kamer2groencamerastatus.grid(row=2, column=5, padx=3, pady=5)

    kamer2camerabeelden = tk.Label(master=hoofdmenuframe, background="white", text="Camerabeelden: ")
    kamer2camerabeelden.grid(row=3, column=3, padx=10, pady=10)

    kamer2camerabeeldenknop = tk.Button(master=hoofdmenuframe, width=5)
    kamer2camerabeeldenknop.grid(row=3, column=4, columnspan=2, padx=10, pady=10)


def toonhoofdmenuframe():
    hoofdmenuframe()
    hoofdmenuframe.pack()


root = tk.Tk()
root.title("Domotica systeem")
root.configure(background="white")

toonhoofdmenuframe()


root.mainloop()