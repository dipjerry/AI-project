class Person {
    private name: string;

    constructor(name: string) {
        this.name = name;
    }

    greet() {
        console.log(`Hello, ${this.name}!`);
    }
}

const person = new Person("Alice");
person.greet();
