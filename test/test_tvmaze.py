from __future__ import print_function, absolute_import, unicode_literals
import unittest

from tvmazepy import tvmaze


class TestTVmaze(unittest.TestCase):
    def test_search_show(self):
        shows = tvmaze.search_show('The Walking Dead')
        [print(show) for show in shows]

    def test_get_show(self):
        show_id = tvmaze.search_show_best_match('Game of Thrones').id
        show = tvmaze.get_show(show_id, populated=True)
        print(show)
        [print(special) for special in show.specials.values()]
        for season in show.seasons.values():
            print(season)
            [print('\t{}'.format(episode)) for episode in season.episodes.values()]
        # for c in show.cast:
        #     print(c)
        # for c in show.crew:
        #     print(c)

    def test_get_show_specials(self):
        show_id = tvmaze.search_show_best_match('Breaking Bad').id
        specials = tvmaze.get_show_specials(show_id)
        [print(special) for special in specials]
