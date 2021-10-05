import db_connect
import getallid

class Review:
    def __init__(self, review, rdate):
        self.patient_id = getallid.get_p_id()
        self.rdate = rdate
        self.review = review

    def add_review(self):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = "INSERT INTO review (patient_id,review,rdate) VALUES (%s, %s,%s)"
        val = (self.patient_id, self.review, self.rdate)
        cursor.execute(sql, val)
        mycon.commit()

    def update_review(self, rid, review):
        mycon = db_connect.connect_sql()
        cursor = mycon.cursor()
        sql = f"UPDATE review SET review= %s WHERE review_id= {rid}"
        val = (review,)
        cursor.execute(sql, val)
        mycon.commit()


r = Review("Good", '2021-05-15')
r.add_review()
