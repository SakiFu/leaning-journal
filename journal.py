# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from pyramid.config import Configurator
from pyramid.view import view_config
from waitress import serve
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Unicode, UnicodeText
import datetime

Base = declarative_base()

DATABASE_URL = os.environ.get(
    'DATABASE_URL',
    'postgresql://sakiukaji@localhost:5432/learning-journal'
)


class Entry(Base):
    __tablename__ = 'entries'
    id = sa.Column(Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.Unicode(100), nullable=False)
    text = sa.Column(sa.UnicodeText, nullable=False)
    date = sa.Column(DateTime, nullable=False, default=datetime.datetime.utcnow)


@view_config(route_name='home', renderer='string')
def home(request):
    return "Hello World"


def main():
    """Create a configured wsgi app"""
    settings = {}
    debug = os.environ.get('DEBUG', True)
    settings['reload_all'] = debug
    settings['debug_all'] = debug
    # configuration setup
    config = Configurator(
        settings=settings
    )
    config.add_route('home', '/')
    config.scan()
    app = config.make_wsgi_app()
    return app

def init_db():
    engine = sa.create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)



if __name__ == '__main__':
    app = main()
    port = os.environ.get('PORT', 5000)
    serve(app, host='0.0.0.0', port=port)
