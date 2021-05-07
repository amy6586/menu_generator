DB_HOST = "menu-generator.cagfzhepmugi.eu-central-1.rds.amazonaws.com"
DB_NAME = "menu_generator"
DB_USER = "postgres"
DB_PASS = "J6dgs9L5oTwAmtmtklPF"
DB_PORT = "5432"

import psycopg2
import psycopg2.extras
#import io

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port = DB_PORT)

cur = conn.cursor()

#create table with same headers as csv file
cur.execute("CREATE TABLE IF NOT EXISTS test(**** text, **** float, **** float, ****
text)")

#open the csv file using python standard file I/O
#copy file into the table just created
with open('******.csv', 'r') as f:
next(f) # Skip the header row.
    #f , <database name>, Comma-Seperated
    cur.copy_from(f, 'menu_generator', sep=',')
    #Commit Changes
    conn.commit()
    #Close connection
    conn.close()


f.close()

conn.close()