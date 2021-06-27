class Person(object):
    # 限定person object只可以綁定_name, _age, _gender attribute
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age


    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name} is playing chess.')
        else:
            print(f'{self._name} is playing dick.')


def main():
    person = Person('Mars', 12)
    person.play()
    person._gender = '男生'

    #person._is_gay = False
    #slot is be like the variable in Java, so class can't add another variable


if __name__ == '__main__':
    main()
