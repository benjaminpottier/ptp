import re
import sys
import json
import requests
import argparse
from bs4 import BeautifulSoup

USER = ''
PASSWORD = ''
PASSKEY = ''
KEEPLOGGED = '1'

LOGIN_URL = "https://passthepopcorn.me/ajax.php?action=login"
LOGOUT_URL = "https://passthepopcorn.me/logout.php?auth={}"
TOP10_URL = "https://passthepopcorn.me/top10.php?json=1"
TORRENTS_URL = "https://passthepopcorn.me/torrents.php?id={}&json=1"
DOWNLOAD_URL = "https://passthepopcorn.me/torrents.php?action=download&id={}"
DOWNLOAD_PATH = "/opt/transmission/downloads/watch"

REGX = re.compile(r"coverViewJsonData\[ 0 \]\s+=\s+(\{.*?\});\n")

parser = argparse.ArgumentParser(description='Passthepopcorn Shortcut.')

parser.add_argument('--top10', action='store_true',
                    help='list ptp top10')
parser.add_argument('--list-torrents', help='list torrents by id')
parser.add_argument('--download', action='append', nargs=2,
                    help='download torrent, must supply release name and id')


EXAMPLE = '''
{"Good Boys": "205921"}
{"Jallikattu": "206165"}
{"Daniel Sloss: X": "206169"}
{"Oil in the Blood": "205947"}
{"Fast &amp; Furious Presents: Hobbs &amp; Shaw": "205170"}
{"47 Meters Down: Uncaged": "205888"}
{"Dulcinea": "206173"}
{"Urban Fears": "206170"}
{"The Fixer AKA Burn Country": "150759"}
{"The Bronx, USA": "206171"}
'''


def add_id(url, id):
    return url.format(id)


def logout(session, url, key):
    session.get(add_id(url, key))


def get_session(url):
    params = {'username': USER, 'password': PASSWORD,
              'passkey': PASSKEY, 'keeplogged': KEEPLOGGED}
    session = requests.Session()
    try:
        request = session.post(url, data=params)
    except Exception as e:
        raise
    return session


if __name__ == "__main__":

    args = parser.parse_args()

    if args.top10:
        session = get_session(LOGIN_URL)
        top10 = BeautifulSoup(session.get(TOP10_URL).text,
                              'html.parser').find('script', text=REGX)
        data = REGX.search(top10.text).group(1)
        top10 = json.loads(data)

        logout(session, LOGOUT_URL, top10['AuthKey'])

        titles = top10['Movies']

        top10_titles = []
        for title in titles:
            title_groupid = {title['Title']: title['GroupId']}
            top10_titles.append(title_groupid)

        for title in top10_titles:
            print(json.dumps(title))

    elif args.list_torrents:
        session = get_session(LOGIN_URL)
        torrents = session.get(add_id(TORRENTS_URL, args.list_torrents)).json()

        logout(session, LOGOUT_URL, torrents['AuthKey'])

        torrents = torrents['Torrents']
        for torrent in torrents:
            releasename_id = {
                'ReleaseName': torrent['ReleaseName'], 'Id': torrent['Id']}
            print(json.dumps(releasename_id))

    elif args.download:
        release, id = args.download[0]
        session = get_session(LOGIN_URL)
        binary = session.get(add_id(DOWNLOAD_URL, id)).content
        file = "{}/{}.{}.torrent".format(DOWNLOAD_PATH, release, id)
        with open(file, 'wb') as f:
            f.write(binary)

    else:
    	parser.print_help()
