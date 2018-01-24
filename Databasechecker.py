import psycopg2

while True:
    try:
        conn = psycopg2.connect("dbname='idp_domotica' user='idpgroep' host='37.97.193.131' password='S67asbiMQA'")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()
    cur.execute("select * from kameractiviteit order by activiteitid desc limit 1")
    rows = cur.fetchall()
    print(rows[0])

    #KAMER 1
    if rows[0][1] == 1:
        if rows[0][2] == 9:
            print("Hond")

    elif rows[0][1] == 2:
        print("Krokodil")

