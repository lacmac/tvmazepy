import requests
import urllib
import endpoints
from model.show import Show


class TVmaze:
    def __init__(self):
        print('TVmaze object created.')

    def query_api(self, url, params=None):
        res = requests.get(url, params)
        print(res.url)
        if res.status_code != requests.codes.OK:
            # print(res.url)
            print(f'Page request was unsuccessful: {res.status_code}', res.reason)
            return None
        return res.json()

    def search_show_name(self, show_name):
        print(f'Searching Shows With Name: {show_name}')
        res = self.query_api(endpoints.search_show_name, {'q': show_name})
        return [Show(show) for show in res] if res is not None else []

    def single_search_show_name(self, show_name, embed=None):
        print(f'Searching A Show With Name: {show_name}')
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
        print(f'Searching Show With {external_name} ID: {external_id}')
        res = self.query_api(endpoints.search_external_show_id, {external_name: external_id})
        return Show(res) if res is not None else None
