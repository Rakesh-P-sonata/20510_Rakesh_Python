import db_connect
import getallid


class Schedule:
    def __init__(self, sdate, start_time, end_time, status, remarks):
        self.doctor_id = getallid.get_d_id()
        self.patient_id = getallid.get_p_id()
        self.date = sdate
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.remarks = remarks

    def add_schedule(self):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = "INSERT INTO schedule (patient_id,doctor_id,  sdate, start_time, end_time, sstatus, remarks) VALUES (" \
              "%s, %s,%s,%s, %s,%s,%s) "
        val = (self.patient_id, self.doctor_id, self.date, self.start_time, self.end_time, self.status, self.remarks)
        cursor.execute(sql, val)
        mycon.commit()

    def update_schedule(self, sid, status):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = f"UPDATE schedule SET sstatus= %s WHERE schedule_id= {sid}"
        val = (status,)
        cursor.execute(sql, val)
        mycon.commit()


s = Schedule('2021-10-13', "5:00 PM", "6:00 PM", "Not Examined", "NA")
s.add_schedule()
