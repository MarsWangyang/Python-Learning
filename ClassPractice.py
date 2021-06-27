from time import sleep
import os
class Clock(object):
    def __init__(self, hour=0, min=0, sec=0):
        self._hour = hour
        self._min = min
        self._sec = sec
        self.flag = True

    def run(self, flag):
        self._sec -= 1
        if self._sec == -1 and (self._min > 0 or self._hour > 0):
            self._sec = 59
            self._min -= 1
            if self._min == -1 or self._hour > 0:
                self._min = 59
                self._hour -= 1
                if self._hour == -1:
                    self._hour = 0
        if not self._sec and not self._min and not self._hour:
            self.flag = False
            print('end')
            return self.flag
        else:
            return self.flag

    def show(self):
        return ('%02d:%02d:%02d' %(self._hour, self._min, self._sec))

def main():
    user = list(map(int, (input("Please enter hour, minute, second respectively with spaces: ").split())))
    clock = Clock(user[0], user[1], user[2])
    flag = True
    while flag:
        print(clock.show())
        sleep(1)
        os.system('clear')
        flag = clock.run(flag)

if __name__ == '__main__':
    main()
