from src.lib.artist import index_artists
from setproctitle import setthreadtitle
import time


def run():
    setthreadtitle('KINDEXER')
    print('Indexer is starting!')
    while True:
        index_artists()
        time.sleep(300)
