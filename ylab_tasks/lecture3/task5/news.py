from heroes import SuperHero
from places import Place


class NewsCreator:

    def __init__(
            self, hero: SuperHero,
            place: Place):
        self.__place_name = self.get_place_name(place)
        self.__hero_name = self.get_hero_name(hero)

    def get_hero_name(self, hero):
        return getattr(hero, 'name', 'unknown hero')

    def get_place_name(self, place):
        if hasattr(place, 'city_name'):
            return getattr(place, 'city_name')
        elif hasattr(place, 'coordinates'):
            return getattr(place, 'coordinates')
        return 'some place'

    def create_newspaper(self):
        print(f'{self.__hero_name}'
              f' saved the {self.__place_name} this week!')

    def create_tv_news(self):
        print(f'Breaking news! Today {self.__hero_name}'
              f' saved the {self.__place_name}!')

    @property
    def hero_name(self):
        return self.__hero_name

    @hero_name.setter
    def hero_name(self, hero):
        self.__hero_name = self.get_hero_name(hero)

    @property
    def place_name(self):
        return self.__place_name

    @place_name.setter
    def place_name(self, place):
        self.__place_name = self.get_place_name(place)
