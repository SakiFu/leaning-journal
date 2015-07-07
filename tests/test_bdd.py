# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pytest_bdd import scenario, given, when, then
import pytest
import markdown

import journal


@pytest.fixture(scope='module')
def db_session(request, connection):
    from transaction import abort
    trans = connection.begin()
    request.addfinalizer(trans.rollback)
    request.addfinalizer(abort)

    from journal import DBSession
    return DBSession


# Homepage Feature
@scenario('features/homepage.feature',
          'Display list of entries in index page')
def test_home_listing_as_anon():
    pass


@given('I am an anonymous user')
def an_anonymous_user(app):
    pass


@given('I have three entries')
def create_entries(db_session):
    title_template = "Title {}"
    text_template = "Entry Text {}"
    for x in range(3):
        journal.Entry.write(
            title=title_template.format(x),
            text=text_template.format(x),
            session=db_session
        )
        db_session.flush()


@when('I go to homepage')
def homepage(homepage):
    pass


@then('I see three entries')
def check_entry_list(homepage):
    html = homepage.html
    entries = html.find_all('article', class_='entry')
    assert len(entries) == 3


# Detail Feature
@scenario('detail.feature',
          'Display a detailed entry linked from index page')
def test_detail_listing_as_anon():
    pass


@given('I am an anonymous user')
@given('I have a journal entry')
def create_one_entry(db_session):
    journal.Entry.write(
        title='A Title',
        text='Some text',
        session=db_session
    )
    db_session.flush()


@when('I go to the detail page from index page')
def visit_detail_page(app):
    pass


@then('I see the entry')
def check_detail_entry(app):
    response = app.get('/detail/4')
    html = response.html
    assert 'Title', 'text' in html


# Edit Feature
@scenario('edit.feature',
          'Edit Entry')
def test_edit_listing_auth():
    pass


@given('I am an authenticated user')
def authenticated_user(app):
    login_data = {'username': 'admin', 'password': 'secret'}
    app.post('/login', params=login_data, status='*')
    return app


@when('I go to the datail page')
def visit_edit_page(app):
    pass


@then('I can edit the entry')
def edit_entry(authenticated_user):
    changed = {'title': 'Edited Title', 'text': 'edited text'}
    redirect = authenticated_user.post('/edit/5', params=changed)
    response = redirect.follow()
    assert 'Edited Title', 'edited text' in response.html


# Markdown Feature
@scenario('markdown.feature',
          'Enter text with markdown syntax)
def test_markdown_entry():
    pass


@given('I am an authenticated user')
def markdown_authenticated_user(app):
    login_data = {'username': 'admin', 'password': 'secret'}
    app.post('/login', params=login_data, status='*')
    return app


@when('I enter text with markdown syntax')
def enter_markdown(authenticated_user):
    title = 'Markdown Test Title'
    text = """Header 1.
    Code block:
    ```Python
    def func(str):
        return str
    ```
   """
    text = markdown.markdown(text, extensions=['codehilite',
                                               'fenced_code'])
    authenticated_user.post('/add', params={'title': title, 'text': text})


@then('I see the entry in h1 format')
def check_markdown_in_entry(app):
    response = app.get('/detail/6')
    assert '<h1>Header 1' in response.html


# Colorized Feature
@scenario('codehilite.feature',
          'Colorize code block')
def test_colorized_entry():
    pass


@given('I have an entry with code block')
def entry_code_block(app):
    return app.get('/detail/6')


@when('I go to the detail page')
def view_post():
    pass


@then('I see colorized code')
def check_colorized(entry_code_block):
    body = entry_code_block.body
    assert '<span class="k">' in body
