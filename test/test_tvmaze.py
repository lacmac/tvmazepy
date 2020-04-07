import unittest

from tvmazepy import tvmaze


class TestTVmaze(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.maze = tvmaze.TVmaze()

    def test_get_show(self):
        show = self.maze.get_show(82, populated=True)
        print(show)
        for season in show.seasons:
            print(season)
            for episode in season.episodes:
                print(f'\t{episode}')
        for c in show.cast:
            print(c)
        for c in show.crew:
            print(c)
