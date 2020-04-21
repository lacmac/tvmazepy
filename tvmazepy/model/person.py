from __future__ import unicode_literals


class Person(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.url = data.get('url')
        self.name = data.get('name')
        self.country = data.get('country')
        self.birthday = data.get('birthday')
        self.deathday = data.get('deathday')
        self.gender = data.get('gender')
        self.image = data.get('image')
        self.links = data.get('_links')

    def __str__(self):
        return self.name


class Character(object):
    def __init__(self, data, person):
        self.id = data.get('id')
        self.url = data.get('url')
        self.name = data.get('name')
        self.image = data.get('image')
        self.links = data.get('_links')
        # self.self = data.get('self')
        # self.voice = data.get('voice')
        self.person = Person(person)

    def __str__(self):
        return self.name + ': ' + self.person


class Crew(Person):
    def __init__(self, data):
        super(Crew, self).__init__(data.get('person'))
        self.job = data.get('type')

    def __str__(self):
        return self.job + ': ' + str(super())
