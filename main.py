from flask import *
from functools import partial
app = Flask(__name__)


class Options:
    def __new__(cls, *a, **kw):
        return None

    session = session
    cookies = cookies
    database = g
    redirect = redirect
    abort = abort


def add_module(*names):
    for name in names:
        module = __import__(name)
        app.route(module.rule, **module.options)(partial(module.main, Options))


add_module("example")


app.run(host="0.0.0.0", port=1471)

