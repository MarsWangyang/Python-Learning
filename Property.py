class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # visitor -- getter methods
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    #revisor
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name} is playing chess.')
        else:
            print(f'{self._name} is playing dick.')

def main():
    person = Person('Mars', 20)
    person2 = Person('Header', 12)
    person.age = 22
    person2.age = 15
    person.play()
    person2.play()

if __name__ == '__main__':
    main()