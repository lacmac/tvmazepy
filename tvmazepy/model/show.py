from .. import utils
from .season import Season
from .episode import Episode
from .person import Crew, Character


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
        self.seasons = []
        self.cast = []
        self.crew = []
        self._handle_embedded(data['_embedded']) if '_embedded' in data else None
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

    def _handle_embedded(self, embedded):
        self.seasons = [Season(season) for season in embedded['seasons']] if 'seasons' in embedded else []
        episodes = [Episode(episode) for episode in embedded['episodes']] if 'episodes' in embedded else []
        if len(self.seasons) != 0:
            for episode in episodes:
                if episode.season <= len(self.seasons):
                    self.seasons[episode.season - 1].episodes.append(episode)
        self.cast = [Character(c['character'], c['person']) for c in embedded['cast']] if 'cast' in embedded else []
        self.crew = [Crew(c) for c in embedded['crew']] if 'crew' in embedded else []

    def __str__(self):
        return f'{self.id}: {self.name}'


class Alias:
    def __init__(self, data):
        self.name = data['name']
        if data['country'] is not None:
            self.country = data['country']
        else:
            self.country = {}
            self.country['name'] = 'Original Country'
            self.country['code'] = 'OG'
            self.country['timezome'] = 'Original Country Timezone'

    def __str__(self):
        return f'{self.country["name"]}: {self.name}'
