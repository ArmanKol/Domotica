import tkinter as tk
import psycopg2, socket, threading, time
from tkinter.ttk import Separator
from PIL import Image, ImageTk


class kamer:
    def __init__(self, kamerid):
        self.kamerid = kamerid
        self.connected = False
        cur.execute('''SELECT voornaam, tussenvoegsel, achternaam FROM persoon WHERE persoonsid = (SELECT persoonsid FROM kamer WHERE kamerid = %s)''', (self.kamerid,))
        self.bewoner = cur.fetchall()[0]
        cur.execute('''SELECT * FROM Persoon WHERE noodpersoonid = (SELECT persoonsid FROM kamer WHERE kamerid = %s)''', (self.kamerid,))
        self.noodcontacten = cur.fetchall()
        cur.execute('''SELECT hardwareid, typehardware FROM hardware WHERE kamerid = %s''', (self.kamerid,))
        self.hardware = dict()
        for hw in cur.fetchall():
            self.hardware[hw[0]]= hardware(hw[0], hw[1])


    def acceptClientsocket(self, clientsocket):
        self.clientsocket = clientsocket
        self.listenerThread = threading.Thread(target=self.listener)
        self.listenerThread.start()
        self.connected = True


    def listener(self):
        while 1:
            time.sleep(2)
            try:
                message = self.clientsocket.recv(5).decode().split(';', 2)
                hardwareID = int(message[0])
                state = int(message[1])
            except ConnectionResetError:
                self.clientsocket.close()
                self.connected = False
                self.listenerThread._stop()
            if hardwareID == 0:
                pass                    # SET KEEPALIVE THINGY
            else:
                self.hardware[hardwareID].setState(state)
                databaseWriter(self.kamerid, hardwareID, state)

    def keepAliveTimeout(self):
        pass

    def keepAlive(self):
        pass


class hardware:
    def __init__(self, hardwareID, description):
        self.hardwareID = hardwareID
        self.description = description
        cur.execute('''SELECT status FROM kameractiviteit WHERE activiteitid = (SELECT MAX(activiteitid) FROM kameractiviteit WHERE hardwareid = %s)''', (hardwareID, ))
        self.state = cur.fetchall()[0][0]

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
        kamers[int(kamerid)].acceptClientsocket(clientsocket)


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
        self.master.rowconfigure(0, minsize=50, weight=10)
        self.master.rowconfigure(1, weight=85)
        self.master.rowconfigure(2, minsize=50, weight=5)

        self.menuFrame.grid(column=1,row=0,columnspan=2, sticky='new')
        self.contentFrame.grid(column=1,row=1, sticky='news')
        self.brandingFrame.grid(column=2,row=1, sticky='news')
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

        label = tk.Label(self.brandingFrame, image=photo)
        label.image = photo  # keep a reference!
        label.pack()

        imageV = Image.open('.\img\Vision.gif')
        photoV = ImageTk.PhotoImage(imageV)

        labelV = tk.Label(self.brandingFrame, image=photoV)
        label.imageV = photoV  # keep a reference!
        labelV.pack()

    def buildFooter(self):
        text = 'Dit programma is geschreven in opdracht van Hogeschool Utrecht, door studenten Marc, Lars, Arman, Teun en Bart. Klas V1H. Vision Domotica \u00a9 2018'
        tk.Label(self.footerFrame, text=text).pack()


    def callRoomOverview(self):
        'Builds an overview of all rooms'
        self.resetContent()
        roomOverview(self.contentFrame)

    def callDataReadings(self, ):
        'Calls the customers GUI'
        self.resetContent()
        dataReadings(self.contentFrame)
        #guiCustomers.customers(self.master)

    def callDatamanipulation(self):
        'calls the products GUI'
        self.resetContent()
        print('datawritings')
        #guiProducts.productMain(self.master)

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
        tk.Label(self, text="Kamer "+str(room.kamerid)).grid(row=0, column=0)
        if room.connected == True:
            tk.Label(self, text='Verbonden', foreground='green').grid(row=0, column=1)
        else:
            tk.Label(self, text='Geen verbinding', background='red', ).grid(row=0, column=1)
        r = 1
        for key in room.hardware:
            hw = room.hardware[key]
            tk.Label(self, text=hw.description[0].upper()+hw.description[1:]).grid(row=r, column=0)
            if hw.state == 0:
                tk.Label(self, text='O', foreground='red').grid(row=r, column=1)
            else:
                tk.Label(self, text='|', foreground='green').grid(row=r, column=1)
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
        pass


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

my_gui = domoticaWindow(root)
root.mainloop()




