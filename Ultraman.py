from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        '''
        :param name: 名字
        :param hp: 生命值
        '''
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass

class Ultraman(Fighter):

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        '''
        :para name: 名字
        :para hp:   生命值
        :para mp:   魔力值
        '''
        super().__init__(name, hp)
        self._mp = mp


    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        '''終極必殺技(打掉對方至少50點或3/4的血)
        :para other: 被攻擊的對象
        :return 使用成功返回True，or return False
        '''
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * (3 // 4)
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        ''' 魔法攻擊
        :para others: 被攻擊的群集
        :return: 使用魔法成功返回True，or Fasle
        '''
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
    def resume(self):
        '''恢復魔法值'''
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point
    def __str__(self):
        return f'Ultraman: {self._name} \n生命值: {self._hp} \n魔法值: {self._mp}'

class Monster(Fighter):
    '''
    小怪獸
    '''

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return f'Monster: {self._name} \n生命值:{self.hp}'

def is_any_alive(monsters):
    '''判斷有沒有小怪獸存活'''
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    '''選中一隻活著的小怪獸'''
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    '''顯示怪獸還有鹹蛋超人的訊息'''
    print(ultraman)
    for monster in monsters:
        print(monster, end='')

def main():
    u = Ultraman('UltraMan', 1000, 120)
    m1 = Monster('Monster1', 250)
    m2 = Monster('Monster2', 500)
    m3 = Monster('Monster3', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print(f'\n=========Round {fight_round}=========')
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6: # 60%的概率使用普通攻擊
            print(f'{u.name}使用普通攻擊打了{m.name}')
            u.attack(m)
            print(f'{u.name}的魔法值恢復{u.resume()}點')
        elif skill <= 9: # 30%概率使用魔法攻擊(有可能因為魔法值不足)
            if u.magic_attack(ms):
                print(f'{u.name}使用了魔法攻擊')
            else:
                print(f'{u.name}使用魔法失敗')
        else:
            if u.huge_attack(m):
                print(f'{u.name}使用究極必殺技打了{m.name}')
            else:
                print(f'{u.name}使用了普通攻擊{m.name}')
                print(f'{u.name}的魔法值恢復{u.resume()}點')
        if m.alive > 0: # 如果被選中的小怪獸沒有死就會回擊
            print(f'{u.name}使用普通攻擊打擊{m.name}')
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n=========End=========\n')
    if u.alive > 0:
        print(f'Ultraman {u.name} Victory!')
    else:
        print('Monsters Victory!')

if __name__ == '__main__':
    main()