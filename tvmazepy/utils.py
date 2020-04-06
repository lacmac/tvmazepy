from bs4 import BeautifulSoup


def strip_tags(string):
    return BeautifulSoup(string, 'html.parser').get_text()
