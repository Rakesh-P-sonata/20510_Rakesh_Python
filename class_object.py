class Employee:
    def __init__(self, empid, empname, empsal, empdept):
        self.empid = empid
        self.empname = empname
        self.empsal = empsal
        self.empdept = empdept

    def details(self):
        print("Employee id:", self.empid)
        print("Employee name:", self.empname)
        print("Employee Salary:", self.empsal)
        print("Employee department:", self.empdept)


class Timesheet:
    def __init__(self, date, no_of_hrs, activity, description, status):
        self.date = date
        self.no_of_hrs = no_of_hrs
        self.activity = activity
        self.description = description
        self.status = status


    def createtimesheet(self):

        print("date:", self.date)
        print("No of Hours:", self.no_of_hrs)
        print("activity:", self.activity)
        print("description:", self.description)
        print("status:", self.status)


emp = Employee("01", "Sam", 26000, "DevOps")
time = Timesheet("29 / 9 / 21", "06", "abc", "work", "done")

emp.details()
time.createtimesheet()
