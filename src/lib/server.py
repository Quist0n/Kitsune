from flask import Flask, g

import bjoern

from configs.vars import webserver_port
from configs.derived_vars import is_development
from src.endpoints.api import api
from src.endpoints.icons import icons
from src.endpoints.banners import banners
from src.internals.database import database
from src.internals.cache import redis

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(icons)
app.register_blueprint(banners)

if is_development:
    from development import development
    app.register_blueprint(development)


def run():
    print('Webserver is starting!')
    bjoern.run(app, '0.0.0.0', int(webserver_port))


@app.teardown_appcontext
def close(e):
    cursor = g.pop('cursor', None)
    if cursor is not None:
        cursor.close()
        connection = g.pop('connection', None)
        if connection is not None:
            try:
                connection.commit()
                pool = database.get_pool()
                pool.putconn(connection)
            except:
                pass
