Feature: Detail
    Detail page displays an entry

Scenario: Display a detailed entry linked from index page
    Given I am an anonymous user
    And I have a journal entry
    When I go to the detail page from index page
    Then I see the entry