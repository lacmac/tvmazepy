from .. import utils


class Show:
    def __init__(self, data):
        self.score = data['score'] if 'score' in data else 100
        show = data['show'] if 'show' in data else data
        self.id = show['id']
        self.name = show['name']
        self.url = show['url']
        self.type = show['type']
        self.lang = show['language']
        self.genres = show['genres']
        self.status = show['status']
        self.num_episodes = show['runtime']
        self.premiere_date = show['premiered']  # datetime?
        self.official_site = show['officialSite']
        self.schedule = show['schedule']
        self.rating = show['rating']
        self.weight = show['weight']
        self.network = show['network']
        self.streaming_service = show['webChannel']
        self.external_ids = show['externals']
        self.images = show['image']
        self.summary = utils.strip_tags(show['summary'])
        self.links = show['_links']

    def __str__(self):
        return f'{self.id}: {self.name}'
