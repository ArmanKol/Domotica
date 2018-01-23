import tkinter as tk
import psycopg2
from tkinter.ttk import Separator

def hoofdmenu():
    global kamer1roodlicht
    global kamer1roodcamerastatus
    global kamer1roodnoodlicht

    global kamer2roodlicht
    global kamer2roodcamerastatus
    global kamer2roodnoodlicht

    #KAMER 1
    kamer1label = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Kamer 1", font=("",12))
    kamer1label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    kamer1lichtlabel = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Licht: ")
    kamer1lichtlabel.grid(row=1, column=0, padx=10, pady=10)

    kamer1roodlicht = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer1roodlicht.grid(row= 1, column=1, padx=2, pady=5)

    kamer1camerastatus = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Camera-status: ")
    kamer1camerastatus.grid(row=2, column=0, padx=10, pady=10)

    kamer1roodcamerastatus = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer1roodcamerastatus.grid(row=2, column=1, padx=2, pady=5)

    kamer1camerabeelden = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Camerabeelden")
    kamer1camerabeelden.grid(row=3, column=0, padx=10 ,pady=10)

    kamer1camerabeeldenknop = tk.Button(master=hoofdmenuframe, width=2)
    kamer1camerabeeldenknop.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

    kamer1nood = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Noodknop: ")
    kamer1nood.grid(row=4, column=0, padx=10, pady=10)

    kamer1roodnoodlicht = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer1roodnoodlicht.grid(row=4, column=1, padx=3, pady=5)

    kamer1noodinformatie = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Noodinformatie: ")
    kamer1noodinformatie.grid(row=5, column=0, padx=5, pady=5)

    kamer1noodknop = tk.Button(master=hoofdmenuframe, width=2, command=toonnoodmenuframe1)
    kamer1noodknop.grid(row=5, column=1, padx=5, pady=5)

    #KAMER 2
    kamer2label = tk.Label(master=hoofdmenuframe, text="Kamer 2", background="gainsboro", font=("",12))
    kamer2label.grid(row=0, column=4, columnspan=3, padx=10, pady=10)

    kamer2lichtlabel = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Licht: ")
    kamer2lichtlabel.grid(row=1, column=4, padx=10, pady=10)

    kamer2roodlicht = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer2roodlicht.grid(row=1, column=5, padx=3, pady=5)

    kamer2camerastatus = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Camera-status: ")
    kamer2camerastatus.grid(row=2, column=4, padx=10, pady=10)

    kamer2roodcamerastatus = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer2roodcamerastatus.grid(row=2, column=5, padx=2, pady=5)

    kamer2camerabeelden = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Camerabeelden: ")
    kamer2camerabeelden.grid(row=3, column=4, padx=10, pady=10)

    kamer2camerabeeldenknop = tk.Button(master=hoofdmenuframe, width=2)
    kamer2camerabeeldenknop.grid(row=3, column=5, columnspan=2, padx=10, pady=10)

    kamer2nood = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Noodknop: ")
    kamer2nood.grid(row=4, column=4, padx=10, pady=10)

    kamer2roodnoodlicht = tk.Label(master=hoofdmenuframe, background="red", width=2)
    kamer2roodnoodlicht.grid(row=4, column=5, padx=3, pady=5)

    kamer2noodinformatie = tk.Label(master=hoofdmenuframe, background="gainsboro", text="Noodinformatie: ")
    kamer2noodinformatie.grid(row=5, column=4, padx=5, pady=5)

    kamer2noodknop = tk.Button(master=hoofdmenuframe, width=2, command=toonnoodmenuframe2)
    kamer2noodknop.grid(row=5, column=5, padx=5, pady=5)

    #Separater
    sep = Separator(hoofdmenuframe, orient="vertical")
    sep.grid(row=0, rowspan=6, column=3, sticky="ns")

def noodvensterkamer1():
    hoofdmenuterugknop = tk.Button(master=noodmenuframe1, width=5, text="Terug", command=toonhoofdmenuframe)
    hoofdmenuterugknop.grid(row=11, column=0)

    noodvenstercamerabeeldentabel = tk.Label(master=noodmenuframe1, background="gainsboro",text="Camerabeelden: ")
    noodvenstercamerabeeldentabel.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstercameralicht = tk.Label(master=noodmenuframe1, background="red", width=2)
    noodvenstercameralicht.grid(row=0, column=1)

    noodvenstercameraknop = tk.Button(master=noodmenuframe1, width=2)
    noodvenstercameraknop.grid(row=0, column=2, padx=5, pady=5)

    noodvenstercontactgegevenslabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Noodcontactgegevens", font=("",15))
    noodvenstercontactgegevenslabel.grid(row=1, column=0, padx=5, pady=5)

    noodvenstervoornaamlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Voornaam: \t\t"+ databasereader("""SELECT voornaam from persoon where noodpersoonid = 1"""))
    noodvenstervoornaamlabel.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstertussenvoegsellabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Tussenvoegsel: \t\t" + str(databasereader("""SELECT tussenvoegsel from persoon where noodpersoonid = 1""")))
    noodvenstertussenvoegsellabel.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterachternaamlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Achternaam: \t\t"+ databasereader("""SELECT achternaam from persoon where noodpersoonid = 1"""))
    noodvensterachternaamlabel.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstergeslachtlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Geslacht: \t\t"+ databasereader("""SELECT geslacht from persoon where noodpersoonid = 1"""))
    noodvenstergeslachtlabel.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstergeboortedatumlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Geboortedatum: \t\t"+ str(databasereader("""SELECT geboortedatum from persoon where noodpersoonid = 1""")))
    noodvenstergeboortedatumlabel.grid(row=6, column=0, padx=5, pady=5 ,sticky=tk.W)

    noodvenstertelefoonnummerlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Telefoonnummer: \t"+ databasereader("""SELECT telefoonnummer from persoon where noodpersoonid = 1"""))
    noodvenstertelefoonnummerlabel.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterplaatsnaamlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Plaatsnaam: \t\t" + databasereader("""SELECT plaatsnaam from persoon where noodpersoonid = 1"""))
    noodvensterplaatsnaamlabel.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterhuisnummerlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Huisnummer: \t\t" + databasereader("""SELECT huisnummer from persoon where noodpersoonid = 1"""))
    noodvensterhuisnummerlabel.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterpostcodelabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Postcode: \t\t" + databasereader("""SELECT postcode from persoon where noodpersoonid = 1"""))
    noodvensterpostcodelabel.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)

def noodvensterkamer2():
    hoofdmenuterugknop = tk.Button(master=noodmenuframe2, width=5, text="Terug", command=toonhoofdmenuframe)
    hoofdmenuterugknop.grid(row=11, column=0)

    noodvenstercamerabeeldentabel = tk.Label(master=noodmenuframe2, background="gainsboro", text="Camerabeelden: ")
    noodvenstercamerabeeldentabel.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstercameralicht = tk.Label(master=noodmenuframe2, background="red", width=2)
    noodvenstercameralicht.grid(row=0, column=1)

    noodvenstercameraknop = tk.Button(master=noodmenuframe2, width=2)
    noodvenstercameraknop.grid(row=0, column=2, padx=5, pady=5)

    noodvenstercontactgegevenslabel = tk.Label(master=noodmenuframe2, background="gainsboro",
                                               text="Noodcontactgegevens", font=("", 15))
    noodvenstercontactgegevenslabel.grid(row=1, column=0, padx=5, pady=5)

    noodvenstervoornaamlabel = tk.Label(master=noodmenuframe2, background="gainsboro", text="Voornaam: \t\t" + databasereader("""SELECT voornaam from persoon where noodpersoonid = 2"""))
    noodvenstervoornaamlabel.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstertussenvoegsellabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Tussenvoegsel: \t\t" + str(databasereader("""SELECT tussenvoegsel from persoon where noodpersoonid = 2""")))
    noodvenstertussenvoegsellabel.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterachternaamlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Achternaam: \t\t" + databasereader("""SELECT achternaam from persoon where noodpersoonid = 2"""))
    noodvensterachternaamlabel.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstergeslachtlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Geslacht: \t\t" + databasereader("""SELECT geslacht from persoon where noodpersoonid = 2"""))
    noodvenstergeslachtlabel.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstergeboortedatumlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Geboortedatum: \t\t" + str(databasereader("""SELECT geboortedatum from persoon where noodpersoonid = 2""")))
    noodvenstergeboortedatumlabel.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstertelefoonnummerlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Telefoonnummer: \t" + databasereader("""SELECT telefoonnummer from persoon where noodpersoonid = 2"""))
    noodvenstertelefoonnummerlabel.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterplaatsnaamlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Plaatsnaam: \t\t" + databasereader("""SELECT plaatsnaam from persoon where noodpersoonid = 2"""))
    noodvensterplaatsnaamlabel.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterhuisnummerlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Huisnummer: \t\t" + databasereader("""SELECT huisnummer from persoon where noodpersoonid = 2"""))
    noodvensterhuisnummerlabel.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterpostcodelabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Postcode: \t\t" + databasereader("""SELECT postcode from persoon where noodpersoonid = 2"""))
    noodvensterpostcodelabel.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)

def toonhoofdmenuframe():
    hoofdmenu()
    noodmenuframe1.pack_forget()
    noodmenuframe2.pack_forget()
    hoofdmenuframe.pack()

def toonnoodmenuframe1():
    noodvensterkamer1()
    hoofdmenuframe.pack_forget()
    noodmenuframe1.pack()

def toonnoodmenuframe2():
    noodvensterkamer2()
    hoofdmenuframe.pack_forget()
    noodmenuframe2.pack()

def frames():
    global hoofdmenuframe
    global noodmenuframe1
    global noodmenuframe2
    hoofdmenuframe = tk.Frame(root)
    hoofdmenuframe.configure(background="gainsboro")
    hoofdmenuframe.pack()

    noodmenuframe1 = tk.Frame(root)
    noodmenuframe1.configure(background="gainsboro")
    noodmenuframe1.pack()

    noodmenuframe2 = tk.Frame(root)
    noodmenuframe2.configure(background="gainsboro")
    noodmenuframe2.pack()

#database reader
def databasereader(x):
    try:
        conn = psycopg2.connect("dbname='idp_domotica' user='idpgroep' host='37.97.193.131' password='S67asbiMQA'")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()
    cur.execute(x)
    rows = cur.fetchall()
    for row in rows:
        informatie = row[0]
    return informatie

def statuslamp():
    if kamer1roodlicht["background"] == "red":
        kamer1roodlicht["background"]="green"

def startgui():
    global root

    root = tk.Tk()
    root.title("Domotica systeem")
    root.configure(background="white")
    root.resizable(False, False)

    frames()
    toonhoofdmenuframe()

    root.mainloop()


startgui()
