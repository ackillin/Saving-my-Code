import sqlite3
from sqlite3 import Error

get_row = lambda conn,table,id : list(conn.execute(f"SELECT * FROM {table} WHERE id = '{id}'"))

def create_conn(file):
    conn = None
    try:
        conn = sqlite3.connect(file)
        print("Connected")
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn,table_name):
    try:
        cur = conn.cursor()
        cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), pay INTEGER);')
        print("Table created")
        conn.commit()
    except Error as e:
        print(e)

def insert_multi(conn,insert_list):
    try:
        cur = conn.cursor()
        for i in insert_list:
            cur.execute(i)
        conn.commit()
    except Error as e:
        print(e)

def select_all(conn,table_name):
    cur=conn.cursor()
    print(f"Printing all rows in {table_name}")
    cur.execute(f"SELECT * FROM {table_name} ORDER BY pay DESC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def get_file():
    with open('accounts.txt','r') as file:
        ret = []
        for li in file:
            li = li.strip()
            li = li.split(',')
            ret.append(li)
        return ret

def creat():
    try:
        f = open('commands.txt','x')
    except:
        f = open('commands.txt','w')
    return f

def conv_multi(conn,listy,table):
    ret = []
    #Adds non-duplicates to the list of rows to insert.
    for i in listy:
        if not get_row(conn,table,i[0]):
            ret.append(f"INSERT INTO {table}(name,pay) VALUES ('{str((i[0]))}',{float(i[1])});")
    print("Converted Texts")
    return ret

def drop_all(conn,table_name):
    #Drops all within a connection and a given table name
    cur = conn.cursor()
    if (input(f"Are you sure you want to drop the {table_name} table? y/n")) == "y":
        cur.execute(f"DROP TABLE {table_name}")
    print("Dropped all")
    conn.commit()

def rolling_input(conn):
    #Gets the input directly from the user
    cur = ""
    while True:
        cur = cur + " " + input("> ")
        lol = (f'cur[-4:-1]cur[-1]').lower()
        if lol == "exit" or lol == "exit()":
            break
        #Checks if it is the end of the statement
        if cur[-1].strip() == ';':
            try:
                sel = conn.execute(cur)
                if cur.split()[0] == "SELECT":
                    for i in sel:
                        print(i)
                    cur = ""
            except Error as e:
                print(e)

if __name__ == '__main__':
    loc = "/home/toor/random/python.db"
    mem = ":memory:"
    con = input("In memeory (mem) or file (loc) ")
    if con.lower() == 'loc':
        print("Saving to file")
        con = "/home/toor/random/python.db"
    else:
        print("Creating with default (memory)")
        con = ':memory:'
    conn = create_conn(con)
    table_name = 'Accounts'
    #Create table and read from insert file.
    create_table(conn,table_name)
    file = get_file()
    writ = creat()
    #Convert file to useable data and insert into table
    seqls = conv_multi(conn,file,table_name)
    
    insert_multi(conn,seqls)

    #Print out all data from that table
    rolling_input(conn)
    #select_all(conn,table_name)
    print("Job Done")
    conn.close()
