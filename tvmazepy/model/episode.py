from .. import utils


class Episode:
    def __init__(self, data):
        self.id = data['id']
        self.url = data['url']
        self.name = data['name']
        self.season = data['season']
        self.number = data['number']
        self.airdate = data['airdate']
        self.airtime = data['airtime']
        self.timestamp = data['airstamp']
        self.duration = data['runtime']
        self.image = data['image']
        self.summary = utils.strip_tags(data['summary'])
        self.links = data['_links']
        self.special = self.number is None

    def __str__(self):
        return f'S{self.season}E{self.number} {self.name}'
