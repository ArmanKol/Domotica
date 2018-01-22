import tkinter as tk
from tkinter.ttk import Separator

def hoofdmenu():
    #KAMER 1
    kamer1label = tk.Label(master=hoofdmenuframe, background="royal blue", text="Kamer 1", font=("",12))
    kamer1label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    kamer1lichtlabel = tk.Label(master=hoofdmenuframe, background="royal blue", text="Licht: ")
    kamer1lichtlabel.grid(row=1, column=0, padx=10, pady=10)

    kamer1roodlicht = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer1roodlicht.grid(row= 1, column=1, padx=2, pady=5)

    kamer1camerastatus = tk.Label(master=hoofdmenuframe, background="royal blue", text="Camera-status: ")
    kamer1camerastatus.grid(row=2, column=0, padx=10, pady=10)

    kamer1roodcamerastatus = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer1roodcamerastatus.grid(row=2, column=1, padx=2, pady=5)

    kamer1camerabeelden = tk.Label(master=hoofdmenuframe, background="royal blue", text="Camerabeelden")
    kamer1camerabeelden.grid(row=3, column=0, padx=10 ,pady=10)

    kamer1camerabeeldenknop = tk.Button(master=hoofdmenuframe, width=2)
    kamer1camerabeeldenknop.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

    kamer1nood = tk.Label(master=hoofdmenuframe, background="royal blue", text="Noodknop: ")
    kamer1nood.grid(row=4, column=0, padx=10, pady=10)

    kamer1roodnoodlicht = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer1roodnoodlicht.grid(row=4, column=1, padx=3, pady=5)

    kamer1noodinformatie = tk.Label(master=hoofdmenuframe, background="royal blue", text="Noodinformatie: ")
    kamer1noodinformatie.grid(row=5, column=0, padx=5, pady=5)

    kamer1noodknop = tk.Button(master=hoofdmenuframe, width=2, command=toonnoodmenuframe)
    kamer1noodknop.grid(row=5, column=1, padx=5, pady=5)

    #KAMER 2
    kamer2label = tk.Label(master=hoofdmenuframe, text="Kamer 2", background="royal blue", font=("",12))
    kamer2label.grid(row=0, column=4, columnspan=3, padx=10, pady=10)

    kamer2lichtlabel = tk.Label(master=hoofdmenuframe, background="royal blue", text="Licht: ")
    kamer2lichtlabel.grid(row=1, column=4, padx=10, pady=10)

    kamer2roodlicht = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer2roodlicht.grid(row=1, column=5, padx=3, pady=5)

    kamer2camerastatus = tk.Label(master=hoofdmenuframe, background="royal blue", text="Camera-status: ")
    kamer2camerastatus.grid(row=2, column=4, padx=10, pady=10)

    kamer2roodcamerastatus = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer2roodcamerastatus.grid(row=2, column=5, padx=2, pady=5)

    kamer2camerabeelden = tk.Label(master=hoofdmenuframe, background="royal blue", text="Camerabeelden: ")
    kamer2camerabeelden.grid(row=3, column=4, padx=10, pady=10)

    kamer2camerabeeldenknop = tk.Button(master=hoofdmenuframe, width=2)
    kamer2camerabeeldenknop.grid(row=3, column=5, columnspan=2, padx=10, pady=10)

    kamer2nood = tk.Label(master=hoofdmenuframe, background="royal blue", text="Noodknop: ")
    kamer2nood.grid(row=4, column=4, padx=10, pady=10)

    kamer2roodnoodlicht = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer2roodnoodlicht.grid(row=4, column=5, padx=3, pady=5)

    kamer2noodinformatie = tk.Label(master=hoofdmenuframe, background="royal blue", text="Noodinformatie: ")
    kamer2noodinformatie.grid(row=5, column=4, padx=5, pady=5)

    kamer2noodknop = tk.Button(master=hoofdmenuframe, width=2)
    kamer2noodknop.grid(row=5, column=5, padx=5, pady=5)

    #Separater
    sep = Separator(hoofdmenuframe, orient="vertical")
    sep.grid(row=0, rowspan=6, column=3, sticky="ns")

def noodvenster():
    hoofdmenuterugknop = tk.Button(master=noodmenuframe, width=5, text="Terug", command=toonhoofdmenuframe)
    hoofdmenuterugknop.grid(row=11, column=0)

    noodcamerabeeldentabel = tk.Label(master=noodmenuframe, background="royal blue",text="Camerabeelden: ")
    noodcamerabeeldentabel.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    noodcameralicht = tk.Label(master=noodmenuframe, background="red", width=2)
    noodcameralicht.grid(row=0, column=1)

    noodcameraknop = tk.Button(master=noodmenuframe, width=2)
    noodcameraknop.grid(row=0, column=2, padx=5, pady=5)

    noodcontactgegevenslabel = tk.Label(master=noodmenuframe, background="royal blue", text="Noodcontactgegevens", font=("",15))
    noodcontactgegevenslabel.grid(row=1, column=0, padx=5, pady=5)

    noodvoornaamlabel = tk.Label(master=noodmenuframe, background="royal blue", text="Voornaam: ")
    noodvoornaamlabel.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

    noodtussenvoegsellabel = tk.Label(master=noodmenuframe, background="royal blue", text="Tussenvoegsel: ")
    noodtussenvoegsellabel.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    noodachternaamlabel = tk.Label(master=noodmenuframe, background="royal blue", text="Achternaam: ")
    noodachternaamlabel.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

    noodgeslachtlabel = tk.Label(master=noodmenuframe, background="royal blue", text="Geslacht: ")
    noodgeslachtlabel.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

    noodgeboortedatumlabel = tk.Label(master=noodmenuframe, background="royal blue", text="Geboortedatum: ")
    noodgeboortedatumlabel.grid(row=6, column=0, padx=5, pady=5 ,sticky=tk.W)

    noodtelefoonnummerlabel = tk.Label(master=noodmenuframe, background="royal blue", text="Telefoonnummer: ")
    noodtelefoonnummerlabel.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

    noodplaatsnaamlabel = tk.Label(master=noodmenuframe, background="royal blue", text="Plaatsnaam: ")
    noodplaatsnaamlabel.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

    noodhuisnummerlabel = tk.Label(master=noodmenuframe, background="royal blue", text="Huisnummer: ")
    noodhuisnummerlabel.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)

    noodpostcodelabel = tk.Label(master=noodmenuframe, background="royal blue", text="Postcode: ")
    noodpostcodelabel.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)

def toonhoofdmenuframe():
    hoofdmenu()
    noodmenuframe.pack_forget()
    hoofdmenuframe.pack()

def toonnoodmenuframe():
    noodvenster()
    hoofdmenuframe.pack_forget()
    noodmenuframe.pack()

def frames():
    global hoofdmenuframe
    global noodmenuframe
    hoofdmenuframe = tk.Frame(root)
    hoofdmenuframe.configure(background="royal blue")
    hoofdmenuframe.pack()

    noodmenuframe = tk.Frame(root)
    noodmenuframe.configure(background="royal blue")
    noodmenuframe.pack()

def startgui():
    global root

    root = tk.Tk()
    root.title("Domotica systeem")
    root.configure(background="white")

    frames()
    toonhoofdmenuframe()

    root.mainloop()

startgui()
