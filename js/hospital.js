const PriorityQueue = require("./modules/PriorityQueue")
const Patient = require("./modules/Patient")
const Doctor = require("./modules/Doctor")
const Appointment = require("./modules/Appointment")
const fs = require("fs")


let patients = fs.readFileSync(`${__dirname}/../data/patients.txt`, 'utf-8')
let doctors = fs.readFileSync(`${__dirname}/../data/doctors.txt`, 'utf-8')

doctors = doctors.split('\n').map(dName => new Doctor(dName));

// console.log(patients, doctors)
patients = patients.split('\n').map(pString => {
    const [name, _, time] = pString.split(' ');
    const [hrs, mins] = time.split(':');
    p = new Patient(name, 30);
    p.getAppointment(hrs, mins, doctors);
    return p;
});

// console.log(doctors, patients)
doctors.forEach(element => {
    console.log(element.appointments)
});