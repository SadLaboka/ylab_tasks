#!/usr/bin/env python3
"""Solution of task5 from the lecture3."""
from heroes import ChuckNorris, Superman, SuperHero
from news import NewsCreator
from places import Place, Kostroma, Tokyo
from random import choice


def save_the_place(hero: SuperHero, place: Place):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()

    news = NewsCreator(hero, place)
    make_news = choice([news.create_newspaper, news.create_tv_news])
    make_news()


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo())
