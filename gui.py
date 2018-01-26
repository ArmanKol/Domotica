import tkinter as tk
import psycopg2, socket, threading, time
from tkinter.ttk import Separator

class client_thread(threading.Thread):
    def __init__(self, clientsocket):
        super().__init__()
        self.clientsocket = clientsocket

    def run(self):
        while 1:
            time.sleep(2)
            try:
                self.clientsocket.send(b'KA')
                message = self.clientsocket.recv(8).decode()
            except ConnectionResetError:
                self.clientsocket.close()
                break
            '''DECODEER DE ONTVANGEN CODE EN ZORG DAT ER ACTIONS ACHTER ZITTEN'''
        self._stop()

def acceptIncomingConnections():
    while 1:
        (clientsocket, address) = serversocket.accept()
        ct = client_thread(clientsocket)
        ct.run()


#Alle labels, knoppen van het hoofdmenu staan hierin.
def hoofdmenu():
    global kamer1roodlicht
    global kamer1roodcamerastatus
    global kamer1roodnoodlicht
    global kamer1camerabeeldenknop

    global kamer2roodlicht
    global kamer2roodcamerastatus
    global kamer2roodnoodlicht
    global kamer2camerabeeldenknop

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

    kamer1camerabeeldenknop = tk.Button(master=hoofdmenuframe, width=2, command=lichtrood)
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

    #Persoon toevoegen kamer1
    persoontoevoegenknop = tk.Button(master=hoofdmenuframe, background="gainsboro", text="Persoon toevoegen", command=toonpersoontoevoegenframe)
    persoontoevoegenknop.grid(row=7, columnspan=1, column=0)

    persoonverwijderenknop = tk.Button(master=hoofdmenuframe, background="gainsboro", text="Persoon verwijderen")
    persoonverwijderenknop.grid(row=7, columnspan=1, column=1)

    #persoon toevoegen kamer2
    persoontoevoegenknop = tk.Button(master=hoofdmenuframe, background="gainsboro", text="Persoon toevoegen", command=toonpersoontoevoegenframe)
    persoontoevoegenknop.grid(row=7, columnspan=1, column=4)

    persoonverwijderenknop = tk.Button(master=hoofdmenuframe, background="gainsboro", text="Persoon verwijderen")
    persoonverwijderenknop.grid(row=7, columnspan=1, column=5)




    #Separater
    sep = Separator(hoofdmenuframe, orient="vertical")
    sep.grid(row=0, rowspan=7, column=3, sticky="ns")


#Alle labels en knoppen van noodinformatie staan hierin.
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

    noodvenstervoornaamlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Voornaam: \t\t"+ databasereadernood("""SELECT voornaam from persoon where noodpersoonid = 1"""))
    noodvenstervoornaamlabel.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstertussenvoegsellabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Tussenvoegsel: \t\t" + str(databasereadernood("""SELECT tussenvoegsel from persoon where noodpersoonid = 1""")))
    noodvenstertussenvoegsellabel.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterachternaamlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Achternaam: \t\t"+ databasereadernood("""SELECT achternaam from persoon where noodpersoonid = 1"""))
    noodvensterachternaamlabel.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstergeslachtlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Geslacht: \t\t"+ databasereadernood("""SELECT geslacht from persoon where noodpersoonid = 1"""))
    noodvenstergeslachtlabel.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstergeboortedatumlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Geboortedatum: \t\t"+ str(databasereadernood("""SELECT geboortedatum from persoon where noodpersoonid = 1""")))
    noodvenstergeboortedatumlabel.grid(row=6, column=0, padx=5, pady=5 ,sticky=tk.W)

    noodvenstertelefoonnummerlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Telefoonnummer: \t"+ databasereadernood("""SELECT telefoonnummer from persoon where noodpersoonid = 1"""))
    noodvenstertelefoonnummerlabel.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterplaatsnaamlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Plaatsnaam: \t\t" + databasereadernood("""SELECT plaatsnaam from persoon where noodpersoonid = 1"""))
    noodvensterplaatsnaamlabel.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterhuisnummerlabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Huisnummer: \t\t" + databasereadernood("""SELECT huisnummer from persoon where noodpersoonid = 1"""))
    noodvensterhuisnummerlabel.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterpostcodelabel = tk.Label(master=noodmenuframe1, background="gainsboro", text="Postcode: \t\t" + databasereadernood("""SELECT postcode from persoon where noodpersoonid = 1"""))
    noodvensterpostcodelabel.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)

#alle labels en knoppen van noodinformatie staan hierin.
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

    noodvenstervoornaamlabel = tk.Label(master=noodmenuframe2, background="gainsboro", text="Voornaam: \t\t" + databasereadernood("""SELECT voornaam from persoon where noodpersoonid = 2"""))
    noodvenstervoornaamlabel.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstertussenvoegsellabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Tussenvoegsel: \t\t" + str(databasereadernood("""SELECT tussenvoegsel from persoon where noodpersoonid = 2""")))
    noodvenstertussenvoegsellabel.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterachternaamlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Achternaam: \t\t" + databasereadernood("""SELECT achternaam from persoon where noodpersoonid = 2"""))
    noodvensterachternaamlabel.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstergeslachtlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Geslacht: \t\t" + databasereadernood("""SELECT geslacht from persoon where noodpersoonid = 2"""))
    noodvenstergeslachtlabel.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstergeboortedatumlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Geboortedatum: \t\t" + str(databasereadernood("""SELECT geboortedatum from persoon where noodpersoonid = 2""")))
    noodvenstergeboortedatumlabel.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

    noodvenstertelefoonnummerlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Telefoonnummer: \t" + databasereadernood("""SELECT telefoonnummer from persoon where noodpersoonid = 2"""))
    noodvenstertelefoonnummerlabel.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterplaatsnaamlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Plaatsnaam: \t\t" + databasereadernood("""SELECT plaatsnaam from persoon where noodpersoonid = 2"""))
    noodvensterplaatsnaamlabel.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterhuisnummerlabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Huisnummer: \t\t" + databasereadernood("""SELECT huisnummer from persoon where noodpersoonid = 2"""))
    noodvensterhuisnummerlabel.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)

    noodvensterpostcodelabel = tk.Label(master=noodmenuframe2, background="gainsboro",text="Postcode: \t\t" + databasereadernood("""SELECT postcode from persoon where noodpersoonid = 2"""))
    noodvensterpostcodelabel.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)

def bewonertoevoegen():
    global voergegevensin
    global voornaaminvoeren
    global voornaaminvoeren
    global tussenvoegselinvoeren
    global achternaaminvoeren
    global geboortedatuminvoeren
    global geslachtinvoeren


    voergegevensin = tk.Label(master=persoontoevoegenframe, background="gainsboro", text="Voer hier de gegevens in van de bewoner: ")
    voergegevensin.grid(row=0, column=0)

    voornaamlabel = tk.Label(master=persoontoevoegenframe, background="gainsboro", text="Voornaam: ")
    voornaamlabel.grid(row=1, column=0)

    voornaaminvoeren = tk.Entry(master=persoontoevoegenframe, background="gainsboro")
    voornaaminvoeren.grid(row=1, column=1)

    tussenvoegsellabel = tk.Label(master=persoontoevoegenframe, background="gainsboro", text="Tussenvoegsel: ")
    tussenvoegsellabel.grid(row=2, column=0)

    tussenvoegselinvoeren = tk.Entry(master=persoontoevoegenframe, background="gainsboro")
    tussenvoegselinvoeren.grid(row=2, column=1)

    achternaamlabel = tk.Label(master=persoontoevoegenframe, background="gainsboro", text="Achternaam: ")
    achternaamlabel.grid(row=3, column=0)

    achternaaminvoeren = tk.Entry(master=persoontoevoegenframe, background="gainsboro")
    achternaaminvoeren.grid(row=3, column=1)

    geboortedatumlabel = tk.Label(master=persoontoevoegenframe, background="gainsboro", text="Geboortedatum: ")
    geboortedatumlabel.grid(row=4, column=0)

    geboortedatuminvoeren = tk.Entry(master=persoontoevoegenframe, background="gainsboro")
    geboortedatuminvoeren.grid(row=4, column=1)

    geslachtlabel = tk.Label(master=persoontoevoegenframe, background="gainsboro", text="geslacht: ")
    geslachtlabel.grid(row=5, column=0)

    geslachtinvoeren = tk.Entry(master=persoontoevoegenframe, background="gainsboro")
    geslachtinvoeren.grid(row=5, column=1)

    terugknop = tk.Button(master=persoontoevoegenframe, background="gainsboro", text="Terug", command=toonhoofdmenuframe)
    terugknop.grid(row=6, column=0)

    uitvoerenknop = tk.Button(master=persoontoevoegenframe, background="gainsboro", text="Uitvoeren", command=databasewriterpersoon)
    uitvoerenknop.grid(row=6, column=1)

def noodpersoontoevoegen():
    global telefoonnummerinvoeren
    global postcodeinvoeren
    global plaatsnaaminvoeren
    global huisnummerinvoeren
    global soortinvoeren

    noodpersoongegevenslabel = tk.Label(master=noodpersoontoevoegenframe, background="gainsboro", text="Voer hier de gegevens in van de noodpersoon: ")
    noodpersoongegevenslabel.grid(row=0, column=0)

    telefoonnummerlabel = tk.Label(master=noodpersoontoevoegenframe, background="gainsboro", text="telefoonnummer: ")
    telefoonnummerlabel.grid(row=6, column=0)

    telefoonnummerinvoeren = tk.Entry(master=noodpersoontoevoegenframe, background="gainsboro")
    telefoonnummerinvoeren.grid(row=6, column=1)

    postcodelabel = tk.Label(master=noodpersoontoevoegenframe, background="gainsboro", text="Postcode: ")
    postcodelabel.grid(row=7, column=0)

    postcodeinvoeren = tk.Entry(master=noodpersoontoevoegenframe, background="gainsboro")
    postcodeinvoeren.grid(row=7, column=1)

    plaatsnaamlabel = tk.Label(master=noodpersoontoevoegenframe, background="gainsboro", text="Plaatsnaam: ")
    plaatsnaamlabel.grid(row=8, column=0)

    plaatsnaaminvoeren = tk.Entry(master=noodpersoontoevoegenframe, background="gainsboro")
    plaatsnaaminvoeren.grid(row=8, column=1)

    huisnummerlabel = tk.Label(master=noodpersoontoevoegenframe, background="gainsboro", text="Huisnummer: ")
    huisnummerlabel.grid(row=9, column=0)

    huisnummerinvoeren = tk.Entry(master=noodpersoontoevoegenframe, background="gainsboro")
    huisnummerinvoeren.grid(row=9, column=1)

    soortlabel = tk.Label(master=noodpersoontoevoegenframe, background="gainsboro", text="Soort: ")
    soortlabel.grid(row=10, column=0)

    soortinvoeren = tk.Entry(master=noodpersoontoevoegenframe, background="gainsboro")
    soortinvoeren.grid(row=10, column=1)

def databasewriternood():
    print("a")

def databasewriterpersoon():
    conn = psycopg2.connect("dbname='idp_domotica' user='idpgroep' host='37.97.193.131' password='S67asbiMQA'")
    cur = conn.cursor()
    cur.execute("INSERT INTO persoon(voornaam, tussenvoegsel, achternaam, geboortedatum, geslacht, telefoonnummer, postcode, plaatsnaam, huisnummer, soort) VALUES(%s, %s, %s, %s, %s, '','','','','')", (voornaaminvoeren.get(),tussenvoegselinvoeren.get(),achternaaminvoeren.get(), geboortedatuminvoeren.get(), geslachtinvoeren.get()));

    print("H")

#Zorgt ervoor dat hoofdmenu wordt geopend. Dat is het venster als de gui opstart.
def toonhoofdmenuframe():
    hoofdmenu()
    noodmenuframe1.pack_forget()
    noodmenuframe2.pack_forget()
    persoontoevoegenframe.pack_forget()
    hoofdmenuframe.pack()


#Zorgt ervoor dat de noodgegevens venster van kamer 1 wordt geopend.
def toonnoodmenuframe1():
    noodvensterkamer1()
    hoofdmenuframe.pack_forget()
    noodmenuframe1.pack()


#Zorgt ervoor dat de noodgegevens venster van kamer2 wordt geopend.
def toonnoodmenuframe2():
    noodvensterkamer2()
    hoofdmenuframe.pack_forget()
    noodmenuframe2.pack()

def toonpersoontoevoegenframe():
    bewonertoevoegen()
    hoofdmenuframe.pack_forget()
    persoontoevoegenframe.pack()

#de verschillende frames van de gui.
def frames():
    global hoofdmenuframe
    global noodmenuframe1
    global noodmenuframe2
    global persoontoevoegenframe
    global noodpersoontoevoegenframe

    hoofdmenuframe = tk.Frame(root)
    hoofdmenuframe.configure(background="gainsboro")
    hoofdmenuframe.pack()

    noodmenuframe1 = tk.Frame(root)
    noodmenuframe1.configure(background="gainsboro")
    noodmenuframe1.pack()

    noodmenuframe2 = tk.Frame(root)
    noodmenuframe2.configure(background="gainsboro")
    noodmenuframe2.pack()

    persoontoevoegenframe = tk.Frame(root)
    persoontoevoegenframe.configure(background="gainsboro")
    persoontoevoegenframe.pack()

    noodpersoontoevoegenframe = tk.Frame(root)
    noodpersoontoevoegenframe.configure(background="gainsboro")
    noodpersoontoevoegenframe.pack()

#database reader. Leest de noodgegevens.
def databasereadernood(x):
    try:
        conn = psycopg2.connect("dbname='idp_domotica' user='idpgroep' host='37.97.193.131' password='S67asbiMQA'")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()
    cur.execute(x)
    rows = cur.fetchall()
    for row in rows:
        informatie = row[0]

    if informatie == None:
        informatie = "-"

    return informatie

#dit zorgt ervoor dat de lichten van rood naar groen kunnen worden veranderd mits de status op 1 staat.
#De status moet opgevraagd worden met de sockets, database?
def lichtrood():

    if status == 1 and kamer1roodlicht["background"] == "red":
        kamer1roodlicht["background"]="green"

    elif kamer1roodcamerastatus["background"] == "red":
        kamer2roodlicht["background"]="green"

    elif kamer1roodnoodlicht["background"] == "red":
        kamer1roodnoodlicht["background"]="green"

    elif kamer2roodlicht["background"] == "red":
        kamer2roodlicht["background"]="green"

    elif kamer2roodcamerastatus["background"] == "red":
        kamer2roodcamerastatus["background"]="green"

    elif kamer2roodnoodlicht["background"] == "red":
        kamer2roodnoodlicht["background"]="green"

#De functie om de gui draaiend te houden.
def startgui():
    global root

    root = tk.Tk()
    root.title("Domotica systeem")
    root.configure(background="white")
    root.resizable(False, False)

    frames()
    toonhoofdmenuframe()

    root.mainloop()


serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 80))
serversocket.listen(5)

incomingConnectionsThread = threading.Thread(target=acceptIncomingConnections)
incomingConnectionsThread.start()


startgui()
