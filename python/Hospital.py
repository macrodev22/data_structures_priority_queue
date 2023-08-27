import random
from collections import namedtuple
from Heap.PriorityQueue import PriorityQueue

Appointment = namedtuple("Appointment", ['hours', 'mins'])


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.id = random.randint(100, 10000000)

    def getId(self) -> int:
        return self.id


class Patient(Person):

    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    doctorId = None
    appointment = Appointment(0, 0)
    doctors = []

    def __lt__(self, b):
        return (self.appointment.hours + (self.appointment.mins/60)) < (b.appointment.hours + (b.appointment.mins/60))

    def __str__(self) -> str:
        [doctor] = [doc for doc in self.doctors if doc.id == self.doctorId]
        return f"{self.name} has an appointment at {self.appointment.hours}:{self.appointment.mins} with {doctor}"

    def getAppointment(self, doctors: list):
        start = Doctor.counter = Doctor.counter % len(doctors)
        for i in range(start, len(doctors)):
            doc: Doctor = doctors[i]
            if (doc.isAvailable(self.appointment.hours, self.appointment.mins)):
                doc.getAppointment(self.appointment.hours,
                                   self.appointment.mins, self)
                Doctor.counter = Doctor.counter+1
                return

        for i in range(0, start):
            doc: Doctor = doctors[i]
            if (doc.isAvailable(self.appointment.hours, self.appointment.mins)):
                doc.getAppointment(self.appointment.hours,
                                   self.appointment.mins, self)
                Doctor.counter = Doctor.counter+1


class Doctor(Person):
    counter = 0

    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.appointments = []

    def isAvailable(self, hrs, mins) -> bool:
        for appointment in self.appointments:
            if appointment.hours == hrs and appointment.mins == mins:
                return False
        return True

    def getAppointment(self, hrs, mins, patient: Patient):
        self.appointments.append(Appointment(hrs, mins))
        patient.doctorId = self.id

    def __str__(self) -> str:
        return f"Dr {self.name}"


if __name__ == '__main__':
    patients = []
    doctors = []
    patientQueue = PriorityQueue(min=True)

    with open("./../data/patients.txt", '+r') as patientFile:
        patients = patientFile.readlines()

    with open("./../data/doctors.txt", '+r') as doctorFile:
        doctors = doctorFile.readlines()

    def patStringToPatient(str: str):
        [name, time] = str.split("at")
        [hrs, mins] = time.split(":")
        p = Patient(name, None)
        p.appointment = Appointment(int(hrs), int(mins))
        return p

    doctors = list(map(lambda x: Doctor(x, None), doctors))
    Patient.doctors = doctors

    patients = list(map(patStringToPatient, patients))
    for patient in patients:
        patientQueue.add(patient)

    while (patientQueue.size() > 0):
        p: Patient = patientQueue.pop()
        p.getAppointment(doctors)
        print(p)
