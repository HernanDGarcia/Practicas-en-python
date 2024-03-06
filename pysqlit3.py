import sqlite3 as sql 

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers(
            name text,
            followers integer,
            subs integer
        )"""
    )
    conn.commit()
    conn.close()

def insertROW(nombre, followers, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()#devuelve todos los datos selecccionados
    conn.commit()
    conn.close()
    print(datos)

def insertRows(streamerList):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?,?,?)"
    cursor.executemany(instruccion, streamerList)
    conn.commit()
    conn.close()

def readOrdered(fields):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {fields} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()#devuelve todos los datos selecccionados
    conn.commit()
    conn.close()
    print(datos)

def search():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name like 'Alex%'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()#devuelve todos los datos selecccionados
    conn.commit()
    conn.close()
    print(datos)


def updateFields():
    #acutalizar datos
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE streamers SET followers=12200000 WHERE name like 'elxo%'"
    cursor.execute(instruccion)
    
    conn.commit()
    conn.close()
   
def delteRows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM streamers WHERE name like 'Ib%'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ ==  "__main__":
    #createDB()
    #createTable()
    #insertROW("Ibai", 7000000, 25000)
    #insertROW("AlexElcapo", 80000, 10000)
    #readRows()
    streamers = [
        ("Elxokas", 10000000, 9500),
        ("Cristinini", 300000, 5500),
        ("Auronplay", 800000000, 200000)
    ]
    #insertRows(streamers)
    #readOrdered('subs')
    #search()
    #updateFields()
    #delteRows()