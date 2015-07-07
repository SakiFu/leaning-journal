Feature: Homepage
    Display list of entries in index page

Scenario: Homepage lists of entries
    Given I am an anonymous user
    And I have three entries
    When I go to homepage
    Then I see three entries