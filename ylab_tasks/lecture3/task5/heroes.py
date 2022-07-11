class LasersMixin:

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class GunMixin:

    def fire_a_gun(self):
        print('PIU PIU')


class RoundHouseKickMixin:

    def roundhouse_kick(self):
        print('Bump')


class SuperHero:

    def __init__(self, name: str, can_use_ultimate_attack: bool = True):
        self._name = name
        self._can_use_ultimate_attack = can_use_ultimate_attack

    def find(self, place):
        place.get_antagonist()

    def attack(self):
        print('Hero attacks!')

    def ultimate(self):
        if self.can_use_ultimate_attack:
            print('Vzzzhuh!')
        else:
            print('Not enough mana!')

    @property
    def can_use_ultimate_attack(self):
        return self._can_use_ultimate_attack

    @can_use_ultimate_attack.setter
    def can_use_ultimate_attack(self, value: bool):
        self._can_use_ultimate_attack = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


class ChuckNorris(SuperHero, GunMixin, RoundHouseKickMixin):

    def __init__(self):
        super().__init__('Chuck Norris')

    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        if self._can_use_ultimate_attack:
            self.roundhouse_kick()
        else:
            print("Ultimate is on cooldown!")


class Superman(SuperHero, LasersMixin):

    def __init__(self):
        super().__init__('Clark Kent')

    def attack(self):
        print("Kick!")

    def ultimate(self):
        if self._can_use_ultimate_attack:
            self.incinerate_with_lasers()
        else:
            print("Ultimate is on cooldown!")
