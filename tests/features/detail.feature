Feature: Detail
    Display a detailed entry linked from index page

Scenario: Detail page displays an entry 
    Given I am an anonymous user
    And I have a journal entry
    When I go to the detail page from index page
    Then I see the entry