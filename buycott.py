# Get the parent company of a brand by using the command line
# to search the Buycott website. This program does not make use of an API.
# buycott.py simply searches a specific webpage for information in the HTML.

import urllib.request
import urllib.parse
import urllib.error
import string

from bs4 import BeautifulSoup


# this is the URL being formatted
link = 'https://www.buycott.com/search?term={}&type=brand'

while True:
    print('__ BUYCOTT.PY __')
    print('--QUIT to exit--\n')

    # get user input
    print('Enter name of brand as search term to '
          'receive the name of the parent company.\n')
    srch_term = input("Enter name: ")

    if srch_term.upper() == 'QUIT':
        break

    # format the URL with user input
    term = srch_term.replace(" ", "+").replace("'", "%27")
    srch_link = link.format(term.lower())

    # print formatted link to show user's intended navigatiion.
    print('.\n..\n...')
    print('Accessing Buycott at URL below:\n')
    print(srch_link, '\n')

    # enter srch_link into urllib request open &
    # create a variable for the request
    fhand = urllib.request.urlopen(srch_link).read()

    # use BeautifulSoup to parse through the html
    soup = BeautifulSoup(fhand, 'lxml')

    tags = soup.find('a', class_='subtype')
    parent_co = tags.string

    # show results!
    print('', '_'*19, '\n', '______RESULTS______\n')
    print('{} brand is owned by {}.\n\n'.format(string.capwords(srch_term),
          string.capwords(parent_co)))
