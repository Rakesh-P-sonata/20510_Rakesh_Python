import db_connect


class Patient:
    def __init__(self, patient_name, gender, age):
        self.patient_name = patient_name
        self.gender = gender
        self.age = age

    def add_patient(self):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = "INSERT INTO patient (patient_name, gender,age) VALUES (%s, %s,%s)"
        val = (self.patient_name, self.gender, self.age)
        cursor.execute(sql, val)
        mycon.commit()

    def update_patient(self, gender):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = "UPDATE patient SET gender= %s WHERE patient_id=1"
        val = (gender,)
        cursor.execute(sql, val)
        mycon.commit()


p = Patient("sam", "Male", 35)
p.add_patient()
