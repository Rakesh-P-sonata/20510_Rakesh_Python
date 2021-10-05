import db_connect
import getallid


class Prescription:
    def __init__(self, prescription, dosage):
        self.prescription = prescription
        self.dosage = dosage
        self.doctor_id = getallid.get_d_id()
        self.patient_id = getallid.get_p_id()
        self.schedule_id = getallid.get_s_id()

    def add_prescription(self):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = "INSERT INTO prescription (patient_id,doctor_id,schedule_id,prescription, Dosage) VALUES (%s, %s,%s, " \
              "%s,%s) "
        val = (self.patient_id, self.doctor_id, self.schedule_id, self.prescription, self.dosage)
        cursor.execute(sql, val)
        mycon.commit()

    def update_prescription(self, dosage, pid):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = f"UPDATE prescription SET dosage=%s WHERE patient_id={pid}"
        val = (dosage,)
        cursor.execute(sql, val)
        mycon.commit()


pr = Prescription("Dolo 650", "3 times ")
pr.add_prescription()
