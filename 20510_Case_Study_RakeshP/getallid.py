import db_connect


def get_d_id():
    mycon = db_connect.connect_sql()
    cursor = mycon.cursor()
    cursor.execute("SELECT * FROM doctor")
    did = cursor.fetchall()
    mycon.commit()
    id = did[-1][0]
    return id


def get_p_id():
    mycon = db_connect.connect_sql()
    cursor = mycon.cursor()
    cursor.execute("SELECT * FROM patient")
    pid = cursor.fetchall()
    mycon.commit()
    id = pid[-1][0]
    return id


def get_s_id():
    mycon = db_connect.connect_sql()
    cursor = mycon.cursor()
    cursor.execute("SELECT * FROM schedule")
    sid = cursor.fetchall()
    mycon.commit()
    id = sid[-1][0]
    return id
