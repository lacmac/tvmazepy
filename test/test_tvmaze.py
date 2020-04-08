import unittest

from tvmazepy import tvmaze


class TestTVmaze(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maze = tvmaze.TVmaze()

    def test_get_show(self):
        show_id = self.maze.search_show_best_match("Game of Thrones").id
        show = self.maze.get_show(show_id, populated=True)
        print(show)
        [print(special) for special in show.specials.values()]
        for season in show.seasons.values():
            print(season)
            [print(f'\t{episode}') for episode in season.episodes.values()]
        # for c in show.cast:
        #     print(c)
        # for c in show.crew:
        #     print(c)

    def test_get_show_specials(self):
        show_id = self.maze.search_show_best_match("Breaking Bad").id
        specials = self.maze.get_show_specials(show_id)
        [print(special) for special in specials]
