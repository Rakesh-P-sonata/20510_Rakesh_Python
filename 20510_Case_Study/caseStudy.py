class Patient:
    def __init__(self, patientid, patientname, address, sex):
        self.patientid = patientid
        self.patientname = patientname
        self.address = address
        self.sex = sex

    def pdetails(self):
        print("Patient id:", self.patientid)
        print("Patient name:", self.patientname)
        print("Patient Gender:", self.sex)
        print("Patient address:", self.address)


class Appointment:
    def __init__(self, reqid, adate, slot, problem, description, previous_visit):
        self.reqid = reqid
        self.adate = adate
        self.slot = slot
        self.problem = problem
        self.description = description
        self.previous_visit = previous_visit

    def appointments(self):
        print("Id:", self.reqid)
        print("date:", self.adate)
        print("No of Hours:", self.slot)
        print("problem:", self.problem)
        print("description:", self.description)
        print("previous_visit:", self.previous_visit)


class Doctor:
    def __init__(self,docid, doctorname, specialization, dschedule):
        self.docid=docid
        self.doctorname = doctorname
        self.specialization = specialization
        self.dschedule = dschedule

    def ddisplay(self):
        print("doctor name: ", self.doctorname)
        print("specialization:", self.specialization)
        print("schedule :", self.dschedule)


class Prescription:
    def __init__(self, name, type, dosage, usage, stop_date):
        self.name = name
        self.type = type
        self.dosage = dosage
        self.usage = usage
        self.stop_date = stop_date


class Review:
    def __init__(self,Doctor_name, Rating,Experience,Review_description,improvements):
        self.Doctor_name=Doctor_name
        self.Rating=Rating
        self.Experience=Experience
        self.Review_description=Review_description
        self.improvements=improvements