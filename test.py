m = int(input())
n = int(input())
temp = []

maxlist = []


def maxcal(li):
    maxlist.append(max(li))


for i in range(m):
    new = input().split()
    for j in new:
        temp.append(int(j))
    maxcal(temp)
    temp.clear()

print(maxlist)


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


d = Doctor("P", "Surgeon")
d.add_doctor()

class Schedule:
    def __init__(self,doctor_id,patient_id, sdate, start_time, end_time, status, remarks):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
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

s = Schedule(1,1,'2021-10-13', "5:00 PM", "6:00 PM", "Not Examined", "NA")
s.add_schedule()