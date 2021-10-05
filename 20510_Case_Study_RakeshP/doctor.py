import db_connect

class Doctor:
    def __init__(self, doctor_name, specialization):
        self.doctor_name = doctor_name
        self.specialization = specialization

    def add_doctor(self):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = "INSERT INTO doctor (doctor_name, specialization) VALUES (%s, %s)"
        val = (self.doctor_name, self.specialization)
        cursor.execute(sql, val)
        mycon.commit()

    def update_doctor(self, specialization):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = "UPDATE doctor SET specialization= %s WHERE doctor_id=1"
        val = (specialization,)
        cursor.execute(sql, val)
        mycon.commit()


d = Doctor("Rakesh", "Surgeon")
d.add_doctor()
