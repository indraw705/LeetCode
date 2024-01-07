import cx_Oracle

ADDRESS = "psdb.p01.eng.sjc01.qualys.com"
PORT = 1521
# (SERVER = DEDICATED)
SERVICE_NAME ="edr"
METHOD = "BASIC"
RETRIES = 180
DELAY = 5

dsn_tns = cx_Oracle.makedsn(ADDRESS, PORT, SERVICE_NAME)
conn = cx_Oracle.connect(user=r'edr', password='edr', dsn=dsn_tns)
c = conn.cursor()
c.execute("select * from epp_profile where customer_uuid='55da184b-3392-d251-80b9-73232fb00dd4'")
 # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
conn.close()