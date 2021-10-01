class NotFoundError(Exception):
    print("Error example")


doctor = [1, 2, 3, 4]
try:
    print(doctor[5])
except NotFoundError:
    print("Not found")
