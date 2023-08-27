function randomId() {
    return `00-0${Math.floor(Math.random()*9)}-${Math.floor(Math.random() * Date.now())}`
}

class Person {
    name;
    id;
    age;
    constructor(name, age=null) {
        this.name = name;
        this.age = age;
        this.id = randomId();
    }

    printInfo(){
        s = `${this.name} ${this.age} yrs`;
        console.log(s);
    }
}


module.exports = Person;