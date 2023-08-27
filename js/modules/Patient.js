const { disconnect } = require('process');
const Person = require('./Person')
const Doctor = require("./Doctor");
const { start } = require('repl');

class Patient extends Person {
    doctorId;
    appointment;
    constructor(name, age=null) {
        super(name, age);
        this.appointment = null;
        this.doctorId = null;
    }

    getAppointment(hrs, mins, doctors) {
        if(doctors) {
            let start = Doctor.counter;
            for(let i = start; i < doctors.length; i++) {
                let doc = doctors[i];
                if(doc.isAvailable(hrs, mins)) {
                    doc.getAppointment(hrs, mins, this)
                    ++Doctor.counter
                    return true;
                }
            }
            for(let i = 0; i < start; i++) {
                let doc = doctors[i];
                if(doc.isAvailable(hrs, mins)) {
                    doc.getAppointment(hrs, mins, this)
                    ++Doctor.counter
                    return true;
                }
            }
            ++Doctor.counter;
            return false;
        }
    }
}

module.exports = Patient;