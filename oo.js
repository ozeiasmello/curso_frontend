class Animal {
    constructor(name, species) {
        this.name = name;
        this.species = species;
    }

    makeSound() {
        return "";
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name, "dog");
        this.breed = breed;
    }

    makeSound() {
        return "Woof!";
    }
}

class Cat extends Animal {
    constructor(name, breed) {
        super(name, "cat");
        this.breed = breed;
    }

    makeSound() {
        return "Meow!";
    }
}

    const dog1 = new Dog("Max", "Golden Retriever");
    const dog2 = new Dog("Buddy", "Beagle");
    const cat = new Cat("Mittens", "Siamese");
    
    console.log(dog1.makeSound());
    console.log(dog2.makeSound());
    console.log(cat.makeSound());
