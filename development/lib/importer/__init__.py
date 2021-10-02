"""
Test importer.
"""
import sys
sys.setrecursionlimit(100000)

import uuid
from .posts import import_posts

if __name__ == '__main__':
    if len(sys.argv) > 1:
        import_posts(str(uuid.uuid4()), sys.argv[1])
    else:
        print('Argument required - Login token')
