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
from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

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

    @classmethod
    def write(cls, title=None, text=None, session=None):
        if session is None:
            session = DBSession
        instance = cls(title=title, text=text)
        session.add(instance)
        return instance

    @classmethod
    def all(cls, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).order_by(cls.date.desc()).all()


@view_config(route_name='home', renderer='templates/list.jinja2')
def list_view(request):
    entries = Entry.all()
    return {'entries':entries}

def main():
    """Create a configured wsgi app"""
    settings = {}
    debug = os.environ.get('DEBUG', True)
    settings['reload_all'] = debug
    settings['debug_all'] = debug
    if not os.environ.get('TESTING', False):
        # only bind the session if we are not testing
        engine = sa.create_engine(DATABASE_URL)
        DBSession.configure(bind=engine)
    # configuration setup
    config = Configurator(
        settings=settings
    )
    config.include('pyramid_jinja2')
    config.include('pyramid_tm')
    config.add_route('home', '/')
    config.add_route('other', '/other/{special_val')
    config.scan()
    app = config.make_wsgi_app()
    return app

def init_db():
    engine = sa.create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

def test_empty_listing(app):
    response = app.get('/')
    assert response.status_code == 200
    actual = response.body
    expected = 'No entries here so far'
    assert expected in actual


def test_listing(app, entry):
    response = app.get('/')
    assert response.status_code == 200
    actual = response.body
    for field in ['title', 'text']:
        expected = getattr(entry, field, 'absent')
        assert expected in actual

if __name__ == '__main__':
    app = main()
    port = os.environ.get('PORT', 5000)
    serve(app, host='0.0.0.0', port=port)
