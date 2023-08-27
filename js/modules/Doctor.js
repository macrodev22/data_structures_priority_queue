const Person = require("./Person")
const Appointment = require("./Appointment")

class Doctor extends Person {
    static counter = 0;
    appointments;
    constructor(name, age=null) {
        super(name, age)
        // this.counter = 0;
        this.appointments = [];
    }

    isAvailable(hrs, mins) {
        const existent = this.appointments.find(a => a.hours == hrs && a.mins == mins)
        return existent ? false : true;
    }

    getAppointment(hrs, mins, patient) {
        const appointment = new Appointment(hrs, mins);
        this.appointments.push(appointment);
        patient.doctorId = this.id;
        this.counter++;
    }
}

module.exports = Doctor;