from datetime import datetime

import requests
from dateutil import parser

import endpoints
from model.show import Show
from model.episode import Episode
from model.season import Season


class TVmaze:
    def __init__(self, log=False):
        self.log = log
        print('TVmaze object created.')

    def query_api(self, url, params=None):
        res = requests.get(url, params)
        print(res.url)
        if res.status_code != requests.codes.OK:
            print(f'Page request was unsuccessful: {res.status_code}', res.reason)
            return None
        return res.json()

    def search_show_name(self, show_name):
        print(f'Searching shows with name: {show_name}')
        res = self.query_api(endpoints.search_show_name, {'q': show_name})
        return [Show(show) for show in res] if res is not None else []

    def single_search_show_name(self, show_name, embed=None):
        print(f'Searching a show with name: {show_name}')
        res = self.query_api(endpoints.single_search_show_name, {'q': show_name, 'embed': embed})
        return Show(res) if res is not None else None

    def search_imdb_id(self, imdb_id):
        return self.search_external_show_id('imdb', imdb_id)

    def search_thetvdb_id(self, tvdb_id):
        return self.search_external_show_id('thetvdb', tvdb_id)

    def search_tvrage_id(self, tvrage_id):
        return self.search_external_show_id('tvrage', tvrage_id)

    def search_external_show_id(self, external_name, external_id):
        if not external_id or external_name not in ['imdb', 'thetvdb', 'tvrage']:
            return
        print(f'Searching show with {external_name} ID: {external_id}')
        res = self.query_api(endpoints.search_external_show_id, {external_name: external_id})
        return Show(res) if res is not None else None

    def search_tvmaze_id(self, tvmaze_id, embed=None):
        print(f'Searching show with TVmaze ID: {tvmaze_id}')
        res = self.query_api(endpoints.show_information.format(str(tvmaze_id)), {'embed': embed})
        return Show(res) if res is not None else None

    def get_show_episode_list(self, tvmaze_id, specials=False):
        print(f'Episodes of show with TVmaze ID: {tvmaze_id}')
        specials = 1 if specials else None
        res = self.query_api(endpoints.show_episode_list.format(str(tvmaze_id)), {'specials': specials})
        return [Episode(episode) for episode in res] if res is not None else []

    def get_show_episode(self, tvmaze_id, season, episode):
        print(f'Episode S{season}E{episode} of show with TVmaze ID: {tvmaze_id}')
        res = self.query_api(endpoints.show_episode.format(str(tvmaze_id)), {'season': season, 'number': episode})
        return Episode(res) if res is not None else None

    def get_show_episodes_by_date(self, tvmaze_id, date_input):
        print(f'Episode released on {date_input} of show with TVmaze ID: {tvmaze_id}')
        if type(date_input) is str:
            try:
                date = parser.parse(date_input).isoformat()[:10]
            except parser._parser.ParserError:
                return []
        elif type(date_input) is datetime:
            date = date_input.isoformat()[:10]
        else:
            return []
        res = self.query_api(endpoints.show_episodes_on_date.format(str(tvmaze_id)), {'date': date})
        return [Episode(episode) for episode in res] if res is not None else []

    def get_show_season_list(self, tvmaze_id):
        print(f'Seasons of show with TVmaze ID: {tvmaze_id}')
        res = self.query_api(endpoints.show_season_list.format(str(tvmaze_id)))
        return [Season(season) for season in res] if res is not None else []
