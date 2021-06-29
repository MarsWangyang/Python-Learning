class Person(object):

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
        print(f'{self._name} is playing piano,')

    def watch_tv(self):
        if self._age >= 18:
            print(f'{self._name} is watching av.')
        else:
            print(f'{self._name} is watching spongebob')

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f'{self._grade} {self._name} enrolled in {course}.')

class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name,age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print(f'{self._title}: {self._name} is teaching {course}')

def main():
    stu = Student('Mars', 15, 'third-grade')
    stu.study('Math')
    stu.watch_tv()
    print(stu.age)
    stu.age = 19
    print(stu.age)
    stu.watch_tv()
    teacher = Teacher('Teacher', 59, 'expert in Math')
    teacher.teach('Python Fuckin Math')
    teacher.watch_tv()
    teacher.play()

if __name__ == '__main__':
    main()