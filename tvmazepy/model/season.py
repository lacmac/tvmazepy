from .. import utils
import string


class Season:
    def __init__(self, data):
        self.id = data['id']
        self.url = data['url']
        self.number = data['number']
        self.name = data['name']
        self.num_episodes = data['episodeOrder']
        self.episodes = []
        self.premiere_date = data['premiereDate']
        self.end_date = data['endDate']
        self.network = data['network']
        self.streaming_service = data['webChannel']
        self.image = data['image']
        self.summary = utils.strip_tags(data['summary'])
        self.links = data['_links']

    def __str__(self):
        return string.capwords(' '.join(self.url.split('/')[-1].split('-')))
