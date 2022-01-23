## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal 
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a attribute named name
        self.name = name

## Cat is-a animal 
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a attribute named name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a attribute named name
        self.name = name

        ## Person has-a pet of some kind, but None allows there to be no pet as the default
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? super exists and is-a Employee with a name attribute? --> This is how to run the _init__ method of a parent class reliably. Research "python3.6 super" and read about how it is good and evil.
        super(Employee, self).__init__(name)
        ## Employee has-a attribute named salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## From mary get the pet attribute and set it to satan
mary.pet = satan

## frank is-a Employee who has-a name of "Frank" and a salary of 120000
frank = Employee("Frank", 120000)

## From frank get the pet attribute and set it to rover
frank.pet = rover

## flipper is-a Fish 
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut() 