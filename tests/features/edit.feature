Feature: Edit Entry
    An authenticated user edit entry

    Scenario: Display edit form with existing text in it
        given: I am an authenticated user
        when: I go to the datail page
        then: I can edit the entry
