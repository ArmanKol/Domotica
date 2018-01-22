import psycopg2

try:
    conn = psycopg2.connect("dbname='idp_domotica' user='idpgroep' host='37.97.193.131' password='S67asbiMQA'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("""SELECT * from persoon """)
rows = cur.fetchall()
print( "\nShow me the databases:\n")
for row in rows:
    print ("   ", row)