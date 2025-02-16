from __future__ import unicode_literals


class Embed(object):
    def __init__(self, data):
        self.key = 'embed'
        self.value = None
        if isinstance(data, str):
            self.key = 'embed'
            self.value = data
        if isinstance(data, list) and len(data) > 0:
            if all(isinstance(item, str) for item in data):
                self.key = 'embed[]'
                self.value = data

    def __str__(self):
        return self.key + ': ' + self.value
