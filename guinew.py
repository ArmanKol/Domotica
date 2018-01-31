import tkinter as tk
import psycopg2, socket, threading, time, webbrowser
from tkinter.ttk import Separator
from PIL import Image, ImageTk


class kamer:
    def __init__(self, kamerid):
        self.kamerid = kamerid
        self.connected = False
        cur.execute('''SELECT voornaam, tussenvoegsel, achternaam FROM persoon WHERE persoonsid = (SELECT persoonsid FROM kamer WHERE kamerid = %s)''', (self.kamerid,))
        result = cur.fetchall()
        if len(result) > 0:
            if result[0][1] == None:
                self.bewoner = '{} {}'.format(result[0][0], result[0][2])
            else:
                self.bewoner = ' '.join(result[0])
        else:
            self.bewoner = 'Onbewoond'
        cur.execute('''SELECT soort, voornaam, tussenvoegsel, achternaam, geboortedatum, geslacht, telefoonnummer, postcode, plaatsnaam, huisnummer FROM Persoon WHERE noodpersoonid = (SELECT persoonsid FROM kamer WHERE kamerid = %s)''', (self.kamerid,))
        self.noodcontacten = cur.fetchall()
        cur.execute('''SELECT hardwareid, typehardware FROM hardware WHERE kamerid = %s''', (self.kamerid,))
        self.hardware = dict()
        for hw in cur.fetchall():
            self.hardware[hw[0]]= hardware(hw[0], hw[1])


    def acceptClientsocket(self, clientsocket, ipaddress):
        self.clientsocket = clientsocket
        self.listenerThread = threading.Thread(target=self.listener)
        self.listenerThread.start()
        self.connected = True
        self.ipaddress = ipaddress
        my_gui.refreshContent()


    def listener(self):
        while 1:
            try:
                message = self.clientsocket.recv(5).decode().split(';', 2)
                hardwareID = int(message[0])
                state = int(message[1])
                print('message is {}'.format(message))
            except ConnectionResetError:
                print('error')
                self.clientsocket.close()
                self.connected = False
                self.listenerThread._stop()
            if hardwareID == 0:
                # SET KEEPALIVE THINGY
                continue
            else:
                self.hardware[hardwareID].setState(state)
                databaseWriter(self.kamerid, hardwareID, state)
            my_gui.refreshContent()

    def keepAliveTimeout(self):
        pass

    def keepAlive(self):
        pass


class hardware:
    def __init__(self, hardwareID, description):
        self.hardwareID = hardwareID
        self.description = description
        #cur.execute('''SELECT status FROM kameractiviteit WHERE activiteitid = (SELECT MAX(activiteitid) FROM kameractiviteit WHERE hardwareid = %s)''', (hardwareID, ))
        #self.state = cur.fetchall()[0][0]
        self.state = 0

    def setState(self, state):
        self.state = state

def on_closing():
    conn.commit()
    cur.close()
    conn.close()
    root.destroy()


def acceptIncomingConnections():
    while 1:
        (clientsocket, address) = serversocket.accept()
        kamerid = clientsocket.recv(2).decode()
        kamers[int(kamerid)].acceptClientsocket(clientsocket, address[0])


def databaseWriter(kamerid, hardwareid, state):
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cur.execute('''INSERT INTO kameractiviteit(kamerid, hardwareid, status, datum_tijd) VALUES (%s, %s, %s, %s)''', (kamerid, hardwareid, state, datetime))
    conn.commit()



class domoticaWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("Vision Domotica")
        #self.master.wm_attributes('-fullscreen', 'true')
        self.menuFrame = tk.Frame(self.master, bg='lightblue')
        self.contentFrame = tk.Frame(self.master)
        self.brandingFrame = tk.Frame(self.master)
        self.footerFrame = tk.Frame(self.master)

        self.master.columnconfigure(0, minsize=50, weight=2)
        self.master.columnconfigure(1, weight=9)
        self.master.columnconfigure(2, weight=3)
        self.master.columnconfigure(3, minsize=50, weight=2)
        self.master.rowconfigure(0, minsize=50, weight=1)
        self.master.rowconfigure(1, weight=85)
        self.master.rowconfigure(2, minsize=50, weight=1)

        self.menuFrame.grid(column=1,row=0,columnspan=2, sticky='new')
        self.contentFrame.grid(column=1,row=1, sticky='news')
        self.brandingFrame.grid(column=2,row=1, sticky='nes')
        self.footerFrame.grid(column=1,row=2,columnspan=2, sticky='ews')

        self.buildMenu()
        self.callRoomOverview()
        self.buildBranding()
        self.buildFooter()

    def buildMenu(self):
        self.menuFrame.rowconfigure(0, weight=1)
        for c in range(3):  #   Pre-configures weight of all columns, so they will be sized evenly when the screen resizes
            self.menuFrame.columnconfigure(c, weight=1)
        font = ('Arial Black', 15)
        tk.Button(self.menuFrame, width=50, height=2, font=font, bg='white', text='Overzicht', command=self.callRoomOverview).grid(column=0,row=0, sticky='news')
        tk.Button(self.menuFrame, width=50, height=2, font=font, bg='white',text='DB Lezen', command=self.callDataReadings).grid(column=1,row=0, sticky='news')
        tk.Button(self.menuFrame, width=50, height=2, font=font, bg='white',text='DB Schrijven', command=self.callDatamanipulation).grid(column=2,row=0, sticky='news')

    def buildBranding(self):
        image = Image.open('.\img\illuminati33.gif')
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.brandingFrame, image=photo, justify='right')
        label.image = photo  # keep a reference!
        label.pack()

        imageV = Image.open('.\img\Vision.gif')
        photoV = ImageTk.PhotoImage(imageV)

        labelV = tk.Label(self.brandingFrame, image=photoV, justify='right')
        label.imageV = photoV  # keep a reference!
        labelV.pack()

    def buildFooter(self):
        text = 'Dit programma is geschreven in opdracht van Hogeschool Utrecht, door studenten Marc, Lars, Arman, Teun en Bart. Klas V1H. Vision Domotica \u00a9 2018'
        tk.Label(self.footerFrame, text=text).pack()


    def callRoomOverview(self):
        'Builds an overview of all rooms'
        self.resetContent()
        self.activeScreen = 'overview'
        roomOverview(self.contentFrame)

    def callDataReadings(self):
        'Calls the customers GUI'
        self.resetContent()
        self.activeScreen = 'dataread'
        print('datareading')
        dataReadings(self.contentFrame)
        #guiCustomers.customers(self.master)

    def callDatamanipulation(self):
        'calls the products GUI'
        self.resetContent()
        datamanipulations(self.contentFrame).keuzeScherm()
        self.activeScreen = 'datawrite'
        print('datawritings')
        #guiProducts.productMain(self.master)

    def refreshContent(self):
        if self.activeScreen == 'overview':
            self.callRoomOverview()

    def resetContent(self):
        'resets the contentframe, preparing it for new content'
        for widget in self.contentFrame.winfo_children():
            widget.destroy()


class roomOverview:
    def __init__(self, master):
        self.master = master
        self.buildOverview()

    def buildOverview(self):
        r = 1
        c = 0
        for key in kamers:
            room = kamers[key]
            singleRoom(self.master, room).grid(row=r, column=c)
            c += 1
            if c > 2:
                c = 0
                r += 1

class singleRoom(tk.Frame):
    def __init__(self, parent, room):
        tk.Frame.__init__(self, parent)
        self.config(width=100, bd=5, relief='raised', padx=1)
        tk.Label(self, text="Kamer "+str(room.kamerid), font=("Arial", 16), width=15).grid(row=0, column=0, columnspan=2)
        r = 1
        tk.Label(self, text=room.bewoner).grid(row=r, column=0, columnspan=2)
        r += 1
        if room.connected:
            tk.Label(self, text='Verbonden', foreground='green', width=20).grid(row=r, column=0, columnspan=2, sticky='ew')
        else:
            tk.Label(self, text='Geen verbinding', background='red', width=20).grid(row=r, column=0, columnspan=2, sticky='ew')
        r += 1
        for key in room.hardware:
            hw = room.hardware[key]
            tk.Label(self, text=hw.description[0].upper()+hw.description[1:]).grid(row=r, column=0, sticky='ew')
            if hw.state == 0:
                tk.Label(self, text='O', foreground='red').grid(row=r, column=1)
                r += 1
            else:
                tk.Label(self, text='|', foreground='green').grid(row=r, column=1)
                r += 1

        tk.Label(self, text='Camera-beelden').grid(row=r, column=0)
        if room.connected:
            tk.Button(self, state='normal', width=2, command=lambda: openStream(room.ipaddress), bg='white').grid(row=r, column=1)
            r += 1
        else:
            tk.Button(self, state='disabled', width=2, bg='gray').grid(row=r, column=1)
            r += 1
        tk.Label(self, text='Noodcontactgegevens').grid(row=r, column=0)
        tk.Button(self, state='normal', width=2, command=lambda: viewNoodcontacten(room.noodcontacten), bg='white').grid(row=r, column=1)


def openStream(ipaddress):
    google_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(google_path))
    #ipaddress = "145.89.157.189:8081"
    url = "http://{}:8081".format(ipaddress)
    webbrowser.get(using='chrome').open(url)


def viewNoodcontacten(noodcontacten):
    window = tk.Toplevel()
    window.wm_title("Noodcontactgegevens")

    if len(noodcontacten) > 0:
        r = 1
        c = 0
        for contact in noodcontacten:
            singleNoodcontact(window, contact).grid(row=r, column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1
    else:
        tk.Label(window, text='Geen noodcontacten beschikbaar', font=("Arial", 16)).grid(row=2, column=2)

    tk.Button(window, text="Terug", command=window.destroy).grid(row=3, column=2)


class singleNoodcontact(tk.Frame):
    def __init__(self, parent, noodcontact):
        tk.Frame.__init__(self, parent)
        self.config(width=100, bd=5, relief='raised', padx=1)

        tk.Label(self, text="Relatie", font=("Arial", 12), width=15, anchor='w').grid(row=0, column=0)
        tk.Label(self, text="Voornaam", font=("Arial", 12), width=15, anchor='w').grid(row=1, column=0)
        tk.Label(self, text="Tussenvoegsel", font=("Arial", 12), width=15, anchor='w').grid(row=2, column=0)
        tk.Label(self, text="Achternaam", font=("Arial", 12), width=15, anchor='w').grid(row=3, column=0)
        tk.Label(self, text="Geboortedatum", font=("Arial", 12), width=15, anchor='w').grid(row=4, column=0)
        tk.Label(self, text="Geslacht", font=("Arial", 12), width=15, anchor='w').grid(row=5, column=0)
        tk.Label(self, text="Telefoonnummer", font=("Arial", 12), width=15, anchor='w').grid(row=6, column=0)
        tk.Label(self, text="Postcode", font=("Arial", 12), width=15, anchor='w').grid(row=7, column=0)
        tk.Label(self, text="Huisnummer", font=("Arial", 12), width=15, anchor='w').grid(row=8, column=0)
        tk.Label(self, text="Plaats", font=("Arial", 12), width=15, anchor='w').grid(row=9, column=0)

        r = 0
        for eigenschap in noodcontact:
            tk.Label(self, text=eigenschap, font=("Arial", 12), width=15, anchor='w').grid(row=r, column=1)
            r += 1



class dataReadings:
    def __init__(self, master):
        self.master = master
        cur = conn.cursor()
        cur.execute('''SELECT ActiviteitID, KamerID, HardwareID, Status, Datum_tijd  FROM kameractiviteit ORDER BY ActiviteitID DESC''')
        rows = cur.fetchall()
        tk.Label(self.master, text= 'Kameractiviteit log gegevens:', font=20).grid(row=0, column=0)
        tk.Label(self.master, text= 'ActiviteitID           -        KamerID      -        HardwareID       -        status        -      Datum_tijd', font=20).grid(row=0, column=1)
        listbox = tk.Listbox(self.master, width=125, height=50)
        listbox.grid(row=1, column=1)
        for row in rows:
            x = ('                                  {}                        -                      {}               -                      {}                        -                {}                 -        {}'.format(row[0],row[1],row[2],row[3],row[4]))
            listbox.insert(tk.END, x)



class datamanipulations:
    def __init__(self, master):
        self.master = master

    def keuzeScherm(self):
        self.resetContent()
        tk.Button(self.master, text="Persoon toevoegen", font=20, command=self.pToevoegen).grid(row=1, column=0, sticky='news')
        tk.Button(self.master, text="Persoon verwijderen", font=20, command=self.pVerwijderen).grid(row=1, column=1, sticky='nsew')
        tk.Button(self.master, text="Persoon aan kamer toevoegen", font=20, command=self.pkamerToevoegen).grid(row=1, column=2, sticky='nsew')
        tk.Button(self.master, text="Persoon uit kamer halen", font=20, command=self.pkamerVerwijderen).grid(row=1, column=3, sticky='nsew')

    def pToevoegen(self):
        self.resetContent()
        tk.Label(self.master, text="Voer hier de gegevens van de nieuwe bewoner in").grid(row=1, column=0, sticky='nsew')
        tk.Label(self.master, text="Voornaam: ").grid(row=2, column=0, sticky='nsew')
        tk.Label(self.master, text="Tussenvoegsel").grid(row=3, column=0, sticky='nsew')
        tk.Label(self.master, text="Achternaam: ").grid(row=4, column=0, sticky='nsew')
        tk.Label(self.master, text="Geboortedatum(YYYY-MM-DD): ").grid(row=5, column=0, sticky='nsew')
        tk.Label(self.master, text="Geslacht: ").grid(row=6, column=0, sticky='nsew')

        self.p_naamEntry = tk.Entry(self.master)
        self.p_tussenvoegselEntry = tk.Entry(self.master)
        self.p_achternaamEntry = tk.Entry(self.master)
        self.p_geboortedatumEntry = tk.Entry(self.master)
        self.p_geslachtEntry = tk.Entry(self.master)

        self.p_naamEntry.grid(row=2, column=1, sticky='nsew')
        self.p_tussenvoegselEntry.grid(row=3, column=1, sticky='nsew')
        self.p_achternaamEntry.grid(row=4, column=1, sticky='nsew')
        self.p_geboortedatumEntry.grid(row=5, column=1, sticky='nsew')
        self.p_geslachtEntry.grid(row=6, column=1, sticky='nsew')

        tk.Button(self.master, text="Terug", command=self.keuzeScherm).grid(row=7, column=0, sticky='nsew', columnspan=1)
        tk.Button(self.master, text="Verder", command=self.p_databasewriter).grid(row=7, column=1, sticky='nsew', columnspan=2)

    def npToevoegen(self):
        self.resetContent()

        tk.Label(self.master, text="Voer hier de noodgegevens van de bewoner in").grid(row=0, column=0, sticky='nsew')
        tk.Label(self.master, text="Voornaam: ").grid(row=1, column=0, sticky='nsew')
        tk.Label(self.master, text="Tussenvoegsel: ").grid(row=2, column=0, sticky='nsew')
        tk.Label(self.master, text="Achternaam: ").grid(row=3, column=0, sticky='nsew')
        tk.Label(self.master, text="Geboortedatum(YYYY-MM-DD): ").grid(row=4, column=0, sticky='nsew')
        tk.Label(self.master, text="Geslacht: ").grid(row=5, column=0, sticky='nsew')
        tk.Label(self.master, text="Telefoonnummer: ").grid(row=6, column=0, sticky='nsew')
        tk.Label(self.master, text="Postcode: ").grid(row=7, column=0, sticky='nsew')
        tk.Label(self.master, text="Plaatsnaam: ").grid(row=8, column=0, sticky='nsew')
        tk.Label(self.master, text="Huisnummer: ").grid(row=9, column=0, sticky='nsew')
        tk.Label(self.master, text="Soort: ").grid(row=10, column=0, sticky='nsew')

        self.np_naamEntry = tk.Entry(self.master)
        self.np_tussenvoegselEntry = tk.Entry(self.master)
        self.np_achternaamEntry = tk.Entry(self.master)
        self.np_geboortedatumEntry = tk.Entry(self.master)
        self.np_geslachtEntry = tk.Entry(self.master)
        self.np_telefoonnummerEntry = tk.Entry(self.master)
        self.np_postcodeEntry = tk.Entry(self.master)
        self.np_plaatsnaamEntry = tk.Entry(self.master)
        self.np_huisnummerEntry = tk.Entry(self.master)
        self.np_soortEntry = tk.Entry(self.master)

        self.np_naamEntry.grid(row=1, column=1)
        self.np_tussenvoegselEntry.grid(row=2, column=1)
        self.np_achternaamEntry.grid(row=3, column=1)
        self.np_geboortedatumEntry.grid(row=4, column=1)
        self.np_geslachtEntry.grid(row=5, column=1)
        self.np_telefoonnummerEntry.grid(row=6, column=1)
        self.np_postcodeEntry.grid(row=7, column=1)
        self.np_plaatsnaamEntry.grid(row=8, column=1)
        self.np_huisnummerEntry.grid(row=9, column=1)
        self.np_soortEntry.grid(row=10, column=1)

        tk.Button(self.master, text="Uitvoeren", command=self.np_databasewriter).grid(row=11, column=0, sticky='nsew', columnspan=2)

    def pVerwijderen(self):
        self.resetContent()

        tk.Label(self.master, text="Vul hier gegevens in van de persoon die je wilt verwijderen").grid(row=0, column=0, sticky='nsew')
        tk.Label(self.master, text="Voornaam: ").grid(row=1, column=0, sticky='nsew')
        tk.Label(self.master, text="Achternaam: ").grid(row=2, column=0, sticky='nsew')
        tk.Label(self.master, text="Geboortedatum: ").grid(row=3, column=0, sticky='nsew')

        self.pv_naamEntry = tk.Entry(self.master)
        self.pv_achternaamEntry = tk.Entry(self.master)
        self.pv_geboortedatumEntry = tk.Entry(self.master)

        self.pv_naamEntry.grid(row=1, column=1, sticky='nsew')
        self.pv_achternaamEntry.grid(row=2, column=1, sticky='nsew')
        self.pv_geboortedatumEntry.grid(row=3, column=1, sticky='nsew')

        tk.Button(self.master, text="Terug", command=self.keuzeScherm).grid(row=4, column=0, sticky='nsew', columnspan=1)
        tk.Button(self.master, text="Uitvoeren", command=self.pv_databaseremove).grid(row=4, column=1, sticky='nsew', columnspan=2)

    def pkamerToevoegen(self):
        self.resetContent()

        tk.Label(self.master, text="Vul hier de gegevens van de persoon in ").grid(row=0, column=0, sticky='nsew')
        tk.Label(self.master, text="Kamerid: ").grid(row=1, column=0, sticky='nsew')
        tk.Label(self.master, text="Voornaam: ").grid(row=2, column=0, sticky='nsew')
        tk.Label(self.master, text="Achternaam: ").grid(row=3, column=0, sticky='nsew')
        tk.Label(self.master, text="Geboortedatum: ").grid(row=4, column=0, sticky='nsew')

        self.pinkamer_kameridEntry = tk.Entry(self.master)
        self.pinkamer_voornaamEntry = tk.Entry(self.master)
        self.pinkamer_achternaamEntry = tk.Entry(self.master)
        self.pinkamer_geboortedatumEntry = tk.Entry(self.master)

        self.pinkamer_kameridEntry.grid(row=1, column=1, sticky='nsew')
        self.pinkamer_voornaamEntry.grid(row=2, column=1, sticky='nsew')
        self.pinkamer_achternaamEntry.grid(row=3, column=1, sticky='nsew')
        self.pinkamer_geboortedatumEntry.grid(row=4, column=1, sticky='nsew')

        tk.Button(self.master, text="Terug", command=self.keuzeScherm).grid(row=6, column=1, sticky='nsew', columnspan=1)
        tk.Button(self.master, text="Uitvoeren", command=self.pinkamer_databasewriter).grid(row=5, column=1, sticky='nsew', columnspan=1)

    def pkamerVerwijderen(self):
        self.resetContent()

        tk.Label(self.master, text="Vul hier de gegevens van de persoon in ").grid(row=0, column=0, sticky='nsew')
        tk.Label(self.master, text="Kamerid: ").grid(row=1, column=0, sticky='nsew')
        tk.Label(self.master, text="Voornaam: ").grid(row=2, column=0, sticky='nsew')
        tk.Label(self.master, text="Achternaam: ").grid(row=3, column=0, sticky='nsew')
        tk.Label(self.master, text="Geboortedatum: ").grid(row=4, column=0, sticky='nsew')

        self.puitkamer_kameridEntry = tk.Entry(self.master)
        self.puitkamer_voornaamEntry = tk.Entry(self.master)
        self.puitkamer_achternaamEntry = tk.Entry(self.master)
        self.puitkamer_geboortedatumEntry = tk.Entry(self.master)

        self.puitkamer_kameridEntry.grid(row=1, column=1, sticky='nsew')
        self.puitkamer_voornaamEntry.grid(row=2, column=1, sticky='nsew')
        self.puitkamer_achternaamEntry.grid(row=3, column=1, sticky='nsew')
        self.puitkamer_geboortedatumEntry.grid(row=4, column=1, sticky='nsew')

        tk.Button(self.master, text="Terug", command=self.keuzeScherm).grid(row=6, column=1, sticky='nsew', columnspan=1)
        tk.Button(self.master, text="Uitvoeren", command=self.puitkamer_databasewriter).grid(row=5, column=1,
                                                                                            sticky='nsew', columnspan=1)

    def puitkamer_databasewriter(self):
        cur.execute("update kamer set persoonsid = NULL where kamerid = %s",
                    (self.puitkamer_kameridEntry.get()))
        conn.commit()
        self.keuzeScherm()

    def pinkamer_databasewriter(self):
        cur.execute("select persoonsid from persoon where voornaam = %s and achternaam = %s", (self.pinkamer_voornaamEntry.get(), self.pinkamer_achternaamEntry.get()))
        persoonid = cur.fetchall()[0][0]


        cur.execute("update kamer set persoonsid = %s where kamerid = %s",
                    (persoonid, self.pinkamer_kameridEntry.get()))
        conn.commit()
        self.keuzeScherm()

    def pv_databaseremove(self):
        cur.execute("delete from persoon where voornaam = %s and achternaam = %s and geboortedatum = %s",
                    (self.pv_naamEntry.get(), self.pv_achternaamEntry.get(), self.pv_geboortedatumEntry.get()))
        conn.commit()

        self.keuzeScherm()

    def p_databasewriter(self):
        cur.execute("INSERT INTO persoon(voornaam, tussenvoegsel, achternaam, geboortedatum, geslacht) "
                    "VALUES(%s, %s, %s, %s, %s)", (self.p_naamEntry.get(), self.p_tussenvoegselEntry.get(), self.p_achternaamEntry.get(),
                                                   self.p_geboortedatumEntry.get(), self.p_geslachtEntry.get()))
        conn.commit()
        self.npToevoegen()

    def np_databasewriter(self):

        cur.execute("select * from persoon order by persoonsid desc limit 1")
        noodpersoonid = cur.fetchall()[0][0]

        cur.execute(
            "INSERT INTO persoon(voornaam, tussenvoegsel, achternaam, geboortedatum, geslacht, telefoonnummer, postcode, plaatsnaam, huisnummer, noodpersoonid, soort) "
            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (self.np_naamEntry.get(), self.np_tussenvoegselEntry.get(), self.np_achternaamEntry.get(), self.np_geboortedatumEntry.get(), self.np_geslachtEntry.get(),
             self.np_telefoonnummerEntry.get(), self.np_postcodeEntry.get(), self.np_plaatsnaamEntry.get(), self.np_huisnummerEntry.get(), noodpersoonid,
             self.np_soortEntry.get()));

        conn.commit()
        self.keuzeScherm()

    def resetContent(self):
        for widget in self.master.winfo_children():
            widget.destroy()


while 1:
    # Maak een verbinding met de database. De rest van het programma wordt pas uitgevoerd zodra deze verbinding gelegd is.
    try:
        conn = psycopg2.connect("dbname='idp_domotica' user='idpgroep' host='37.97.193.131' password='S67asbiMQA'")
        cur = conn.cursor()
    except:
        print("Unable to connect to the database")
        continue
    break


# Haalt alle gegevens van de kamers op en slaat deze op in Objecten
cur.execute('''SELECT kamerid FROM kamer''')
kamers = dict()
for kmr in cur.fetchall():
    kamers[kmr[0]] = kamer(kmr[0])


serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 80))
serversocket.listen(5)


incomingConnectionsThread = threading.Thread(target=acceptIncomingConnections)
incomingConnectionsThread.daemon = True
incomingConnectionsThread.start()


root = tk.Tk()
root.title("Domotica systeem")
root.protocol("WM_DELETE_WINDOW", on_closing)

root.state('zoomed')

my_gui = domoticaWindow(root)
root.mainloop()




