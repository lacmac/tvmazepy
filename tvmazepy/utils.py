from bs4 import BeautifulSoup


def strip_tags(string):
    soup = BeautifulSoup(string, 'html.parser')
    return soup.get_text()
