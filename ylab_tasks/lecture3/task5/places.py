from abc import abstractmethod, ABC


class Place(ABC):
    @abstractmethod
    def get_antagonist(self):
        """Gets the antagonist"""


class Kostroma(Place):
    city_name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    city_name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')
