from __future__ import absolute_import, unicode_literals

from .. import utils


class Episode(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.url = data.get('url')
        self.name = data.get('name')
        self.season = data.get('season')
        self.number = data.get('number') if data.get('number') is not None else 0
        self.airdate = data.get('airdate')
        self.airtime = data.get('airtime')
        self.timestamp = data.get('airstamp')
        self.duration = data.get('runtime')
        self.images = data.get('image')
        self.summary = utils.strip_tags(data.get('summary'))
        self.links = data.get('_links')
        self.special = self.number == 0

    def __str__(self):
        return 'S{}E{} {}'.format(self.season, self.number, self.name)
        # return f'S{self.season}E{self.number} {self.name}' if not self.special else f'Special: {self.name}'
